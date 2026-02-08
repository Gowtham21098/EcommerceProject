from django.urls import path
from products import views

urlpatterns = [
    path('hello/' , views.hello),
    path('allProducts', views.get_products),
    path('product/<int:id>', views.get_product),
    path('product/', views.create_product),
    path('product/delete/<int:id>', views.delete_product),
    path('allCategories', views.get_categories),
    path('category/<int:id>', views.get_category),
    path('category/delete/<int:id>', views.delete_category),
    path('category/', views.create_category),

]