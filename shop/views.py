from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from .models import Category, Product, CustomUser
from . import serializers
from django.contrib.auth import get_user_model


# Category Views

@swagger_auto_schema(
    method='get',
    operation_description="Get a list of categories",
    responses={200: serializers.CategorySerializer(many=True)}
)
@swagger_auto_schema(
    method='post',
    operation_description="Create a new category",
    request_body=serializers.CategorySerializer
)
@api_view(['GET', 'POST'])
def category_list(request):

    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = serializers.CategorySerializer(categories, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = serializers.CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    method='get',
    operation_description="Get details of a category",
    responses={200: serializers.CategorySerializer()}
)
@swagger_auto_schema(
    method='put',
    operation_description="Update a category",
    request_body=serializers.CategorySerializer
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
        serializer = serializers.CategorySerializer(category)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = serializers.CategorySerializer(category, data=request.data)
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
    responses={200: serializers.ProductSerializerResponse(many=True)}
)
@swagger_auto_schema(
    method='post',
    operation_description="Create a new product",
    request_body=serializers.ProductSerializer,
    responses={201: serializers.ProductSerializerResponse()}
)
@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = serializers.ProductSerializerResponse(products, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = serializers.ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    method='get',
    operation_description="Get details of a product",
    responses={200: serializers.ProductSerializerResponse()}
)
@swagger_auto_schema(
    method='put',
    operation_description="Update a product",
    request_body=serializers.ProductSerializer
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
        serializer = serializers.ProductSerializerResponse(product)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = serializers.ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        product.delete()
        return Response({"message":f"{pk} succesfully deleted"},status=status.HTTP_204_NO_CONTENT)


# User Views

@swagger_auto_schema(
    method='get',
    operation_description="Get all users",
    responses={200: serializers.UserSerializer()}
)
@swagger_auto_schema(
    method='post',
    operation_description="Create a new user",
    request_body=serializers.UserSerializer
)
@api_view(['POST', 'GET'])
def user_list(request):
    if request.method == 'GET':
        users = CustomUser.objects.all()
        serializer = serializers.UserSerializer(users, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        data = request.data
        email = data.get('email')
        password = data.get('password')
        
        if not email or not password:
            return Response({"error": "Email and password are required"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            CustomUser.objects.get(email=email)
            return Response({"error": "User with this email already exists"}, status=status.HTTP_400_BAD_REQUEST)
        except CustomUser.DoesNotExist:
            user = CustomUser.objects.create_user(**data)
        return Response({"email": user.email}, status=status.HTTP_201_CREATED)

@swagger_auto_schema(
    method='get',
    operation_description="Get a user's details",
    responses={200:serializers.UserSerializer()}
)
@api_view(['GET'])
def user_detail(request, pk):
    try:
        user = CustomUser.objects.get(pk=pk)
    except CustomUser.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = serializers.UserSerializer(user)
    return Response(serializer.data)