# Shop Backend API

This is a backend API for a shop application built with Django. The API includes basic CRUD (Create, Read, Update, Delete) operations for categories and products, as well as user creation and retrieval functionality.

## Features

- **User Management**: Create new users and get user information.
- **Category Management**: CRUD operations for product categories.
- **Product Management**: CRUD operations for products within categories.

## Technologies Used

- **Python 3.x**
- **Django 5.x**
- **Django REST Framework** (for building the API)
- **SQLite** (default database)

## Installation

### Prerequisites

Ensure that Python 3.x is installed on your machine.

### Steps to Install

1. Clone the repository:
    ```bash
    git clone https://github.com/Dasturchi-Mufid/shop_tz.git
    cd shop_tz
    ```

2. Create a virtual environment:
    ```bash
    python3 -m venv venv
    ```

3. Activate the virtual environment:
    - On Windows:
      ```bash
      venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

4. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Apply database migrations:
    ```bash
    python manage.py migrate
    ```

6. Create a superuser (for admin access):
    ```bash
    python manage.py createsuperuser
    ```

7. Run the development server:
    ```bash
    python manage.py runserver
    ```

8. The API Swagger Documentation [http://127.0.0.1:8000/api/swagger/](http://127.0.0.1:8000/api/swagger/).

## API Documentation

### User Management
- **POST** `/api/users/`: Create a new user. (Requires `email`, `password` in request body)
  - Example request:
    ```json
    {
      "email": "john@example.com",
      "password": "password123"
    }
    ```
  
- **GET** `/api/users/{id}/`: Get details of a specific user by their ID.


### Category Management
- **GET** `/api/categories/`: Get a list of all categories.
- **POST** `/api/categories/`: Create a new category. (Requires `name` and `description` in request body)
  - Example request:
    ```json
    {
      "name": "Electronics",
      "description":"Electronic products"
    }
    ```

- **GET** `/api/categories/{id}/`: Get details of a specific category by its ID.
- **PUT** `/api/categories/{id}/`: Update an existing category. (Requires `name` and `description` in request body)
- **DELETE** `/api/categories/{id}/`: Delete a category by its ID.

### Product Management
- **GET** `/api/products/`: Get a list of all products.
- **POST** `/api/products/`: Create a new product. (Requires `name`, `price`, `category` in request body)
  - Example request:
    ```json
    {
      "name": "Laptop",
      "price": 999.99,
      "category": 1
    }
    ```

- **GET** `/api/products/{id}/`: Get details of a specific product by its ID.
- **PUT** `/api/products/{id}/`: Update an existing product. (Requires `name`, `price`, `category` in request body)
- **DELETE** `/api/products/{id}/`: Delete a product by its ID.


## Testing

To run tests for this application, use the following command:

```bash
python manage.py test
```
