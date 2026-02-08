from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.fields import DecimalField
from rest_framework.response import Response
from rest_framework.utils.serializer_helpers import ReturnDict

from products.models import Products, Category
from products.serializers import ProductSerializer, CategorySerializer


# Create your views here.

def hello(request):
    return HttpResponse('Hello World!')

@api_view(['GET'])
def get_products(request):
    data = Products.objects.all()
    serialized_data = ProductSerializer(data, many=True)
    return Response(serialized_data.data)

@api_view(['GET'])
def get_categories(request):
    data = Category.objects.all()
    serialized_data = CategorySerializer(data, many=True)
    return Response(serialized_data.data)

@api_view(['GET'])
def get_product(request, id):
    try:
        data = Products.objects.get(id=id)
        serialized_data = ProductSerializer(data)
        return Response(serialized_data.data)
    except Products.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_category(request, id):
    try:
        data = Category.objects.get(id=id)
        serialized_data = CategorySerializer(data)
        return Response(serialized_data.data)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def create_product(request):
    try:
        data = request.data
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_category(request):
    try:
        data = request.data
        serializer = CategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_product(request, id):
    try:
        data = Products.objects.get(id=id)
        data.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    except Products.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_category(request, id):
    try:
        data = Category.objects.get(id=id)
        data.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)




