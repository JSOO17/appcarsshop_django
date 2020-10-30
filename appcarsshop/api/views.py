from django.shortcuts import render
from rest_framework import viewsets
from .models import User, Product, Order, ProductOrdered
from .serializers import UserSerializer, ProductSerializer, OrderSerializer, \
    ProductOrderedSerializer
from django.shortcuts import render

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

class ProductOrderedViewSet(viewsets.ModelViewSet):
    serializer_class = ProductOrderedSerializer
    queryset = ProductOrdered.objects.all().select_related('user')


def users(request):
    users = User.objects.all()
    
    return render(request, 'users.html', {'users': users})

def products(request):
    products = Product.objects.all()
    
    return render(request, 'products.html', {'products': products})