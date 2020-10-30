from rest_framework import serializers
from .models import User, Product, Order, ProductOrdered

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class ProductOrderedSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOrdered
        fields = '__all__'
