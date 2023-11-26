from rest_framework import serializers
from .models import CustomUser, Product, Transaction

# Serializer for CustomUser model
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'full_name', 'last_login')

# Serializer for Product model
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'price', 'stock')

# Serializer for Transaction model
class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('cashier', 'number_of_items', 'items', 'transaction_time')