from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .decorators import deny_after_10pm, allow_only_weekdays

from .models import Products
from .serializers import ProductSerializer, CategorySerializer


# Create your views here.
def hello(request):
    return HttpResponse("Hello World")
def welcome(request):
    return HttpResponse("Welcome to Ecommerce")
#
# # API to get all products
# @api_view(['GET'])
# @deny_after_10pm
# def get_products(request):
#     products = Products.objects.all()
#     serializer = ProductSerializer(products, many=True)
#     return Response(serializer.data)

# Get all products (protected after 10 PM)
@api_view(['GET'])
@deny_after_10pm
def get_products(request):
    try:
        products = Products.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({"error": "Something went wrong"}, status=500)

# API to get single product by id
# @api_view(['GET'])
# def get_product(request, id):
#     try:
#         product = Products.objects.get(id=id)
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)
#     except Products.DoesNotExist:
#         return Response({"error": "Product not found"}, status=404)

# 
# @api_view(['GET'])


# def get_product(request, id):
#     try:
#         product = Products.objects.get(id=id)
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)
#     except Products.DoesNotExist:
#         return Response({"error": "Product not found"}, status=404)
#     except Exception as e:
#         return Response({"error": "Something went wrong"}, status=500)


# Get single product by ID
@api_view(['GET'])
def get_product(request, id):
    try:
        product = Products.objects.get(id=id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    except Products.DoesNotExist:
        return Response({"error": "Product not found"}, status=404)
    except Exception as e:
        return Response({"error": "Something went wrong"}, status=500)

# # API to create product (POST)
# @api_view(['POST'])
# def create_product(request):
#     serializer = ProductSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer.errors, status=400)

# Create product (allowed only on weekdays)

@api_view(['POST'])
@allow_only_weekdays
def create_product(request):
    try:
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    except Exception as e:
        return Response({"error": "Something went wrong"}, status=500)

# @api_view(['GET'])
# def get_available_products(request):
#     products = Products.objects.filter(is_available=True)
#     serializer = ProductSerializer(products, many=True)
#     return Response(serializer.data)

# Get available products
@api_view(['GET'])
def get_available_products(request):
    try:
        products = Products.objects.filter(is_available=True)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({"error": "Something went wrong"}, status=500)

# #  New Category API
# @api_view(['POST'])
# def create_category(request):
#     serializer = CategorySerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer.errors, status=400)

# Create category (already clean, can add try-except if you want)
@api_view(['POST'])
def create_category(request):
    try:
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    except Exception as e:
        return Response({"error": "Something went wrong"}, status=500)