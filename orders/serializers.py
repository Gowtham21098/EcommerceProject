from rest_framework import serializers
from .models import Order, OrderItem
from products.models import Products

class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField(source='product.name')

    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'product_name', 'quantity', 'price']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    order_items = serializers.ListField(
        child=serializers.DictField(), write_only=True
    )

    class Meta:
        model = Order
        fields = ['id', 'user', 'status', 'total_price', 'shipping_address', 'created_at', 'updated_at', 'items', 'order_items']
        read_only_fields = ['user', 'total_price', 'status', 'created_at', 'updated_at']

    def create(self, validated_data):
        order_items_data = validated_data.pop('order_items')
        user = self.context['request'].user
        
        # Calculate total price and validate stock
        total_price = 0
        for item_data in order_items_data:
            product = Products.objects.get(id=item_data['product_id'])
            if product.stock_quantity < item_data['quantity']:
                raise serializers.ValidationError(f"Not enough stock for {product.name}")
            total_price += product.price * item_data['quantity']
        
        order = Order.objects.create(user=user, total_price=total_price, **validated_data)

        for item_data in order_items_data:
            product = Products.objects.get(id=item_data['product_id'])
            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=item_data['quantity'],
                price=product.price
            )
            # Deduct stock
            product.stock_quantity -= item_data['quantity']
            product.save()

        return order
