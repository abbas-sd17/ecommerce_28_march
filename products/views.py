from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Products
from .serializers import ProductSerializer


# Create your views here.
def hello(request):
    return HttpResponse("Hello World")
def welcome(request):
    return HttpResponse("Welcome to Ecommerce")

# API to get all products
@api_view(['GET'])
def get_products(request):
    products = Products.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

# API to get single product by id
@api_view(['GET'])
def get_product(request, id):
    try:
        product = Products.objects.get(id=id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    except Products.DoesNotExist:
        return Response({"error": "Product not found"}, status=404)

# API to create product (POST)
@api_view(['POST'])
def create_product(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def get_available_products(request):
    products = Products.objects.filter(is_available=True)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)
