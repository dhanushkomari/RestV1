from .models import Category, Product
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('prod_id', 'category_id', 'quantity', 'name', 'price')