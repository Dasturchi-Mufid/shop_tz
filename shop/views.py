# shop/views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from .models import Category, Product, CustomUser
from .serializers import CategorySerializer, ProductSerializer, UserSerializer
from django.contrib.auth import get_user_model


# Category Views

@swagger_auto_schema(
    method='get',
    operation_description="Get a list of categories",
    responses={200: CategorySerializer(many=True)}
)
@swagger_auto_schema(
    method='post',
    operation_description="Create a new category",
    request_body=CategorySerializer
)
@api_view(['GET', 'POST'])
def category_list(request):

    permission_classes = [IsAuthenticated]

    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    method='get',
    operation_description="Get details of a category",
    responses={200: CategorySerializer()}
)
@swagger_auto_schema(
    method='put',
    operation_description="Update a category",
    request_body=CategorySerializer
)
@swagger_auto_schema(
    method='delete',
    operation_description="Delete a category"
)
@api_view(['GET', 'PUT', 'DELETE'])
def category_detail(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Product Views

@swagger_auto_schema(
    method='get',
    operation_description="Get a list of products",
    responses={200: ProductSerializer(many=True)}
)
@swagger_auto_schema(
    method='post',
    operation_description="Create a new product",
    request_body=ProductSerializer
)
@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    method='get',
    operation_description="Get details of a product",
    responses={200: ProductSerializer()}
)
@swagger_auto_schema(
    method='put',
    operation_description="Update a product",
    request_body=ProductSerializer
)
@swagger_auto_schema(
    method='delete',
    operation_description="Delete a product"
)
@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# User Views

@swagger_auto_schema(
    method='post',
    operation_description="Create a new user",
    request_body=UserSerializer
)
@api_view(['POST'])
def create_user(request):
    data = request.data
    email = data.get('email')
    password = data.get('password')
    
    if not email or not password:
        return Response({"error": "Email and password are required"}, status=status.HTTP_400_BAD_REQUEST)
    
    user = CustomUser.objects.create_user(email=email, password=password, **data)
    return Response({"email": user.email}, status=status.HTTP_201_CREATED)
