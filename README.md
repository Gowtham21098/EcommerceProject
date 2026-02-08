# E-commerce Project

## Overview
This is a Django-based backend for an E-commerce application. It provides APIs for managing products, categories, and processing customer orders with inventory tracking.

## Features
- **Product Management**: Create, update, and retrieve products and categories.
- **Inventory Tracking**: automatically deducts stock when orders are placed.
- **Order Processing**: Create orders with multiple items and track their status.
- **Audit Logging**: Tracks creation and update times for all core models.

## Technology Stack
- **Framework**: Django 5.2.10
- **API**: Django Rest Framework
- **Database**: SQLite (default) / Configurable

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd EcommerceProject
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # Linux/Mac
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install django djangorestframework
   ```

4. **Apply migrations**
   ```bash
   python manage.py migrate
   ```

5. **Run the development server**
   ```bash
   python manage.py runserver
   ```

## API Endpoints

### Products
- **List/Create Products**: `GET /api/products/`, `POST /api/products/`
- **Retrieve/Update/Delete Product**: `GET /api/products/<id>/`, `PUT /api/products/<id>/`, `DELETE /api/products/<id>/`

### Orders
- **List Orders**: `GET /api/orders/`
- **Place Order**: `POST /api/orders/`
  ```json
  {
      "shipping_address": "123 Street Name, City",
      "order_items": [
          {
              "product_id": 1,
              "quantity": 2
          }
      ]
  }
  ```
- **Retrieve Order**: `GET /api/orders/<id>/`

## Models

### Products App
- `Products`: Represents items for sale. Includes stock tracking.
- `Category`: Categorizes products.

### Orders App
- `Order`: Represents a customer's order.
- `OrderItem`: Represents individual items within an order (captures price at purchase).
