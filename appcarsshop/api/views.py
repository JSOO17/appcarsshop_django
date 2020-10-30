from django.shortcuts import render
from rest_framework import viewsets
from .models import User, Product
from .serializers import UserSerializer, ProductSerializer
from django.shortcuts import render

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

def users(request):
    users = User.objects.all()
    
    return render(request, 'users.html', {'users': users})

def products(request):
    products = Product.objects.all()
    
    return render(request, 'products.html', {'products': products})