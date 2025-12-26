from rest_framework import serializers
from .models import Category, Product, Order


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор для категорий"""
    products_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'products_count']
    
    def get_products_count(self, obj):
        """Количество активных товаров в категории"""
        return obj.products.filter(is_active=True).count()


class ProductListSerializer(serializers.ModelSerializer):
    """Краткий сериализатор для списка товаров"""
    category_name = serializers.CharField(source='category.name', read_only=True)
    
    class Meta:
        model = Product
        fields = ['id', 'name', 'category_name', 'price', 'telegram_file_id']


class ProductDetailSerializer(serializers.ModelSerializer):
    """Полный сериализатор для детальной информации о товаре"""
    category_name = serializers.CharField(source='category.name', read_only=True)
    category_id = serializers.IntegerField(source='category.id', read_only=True)
    
    class Meta:
        model = Product
        fields = [
            'id', 
            'name', 
            'description', 
            'price', 
            'category_id',
            'category_name',
            'telegram_file_id',
            'image'
        ]


class OrderCreateSerializer(serializers.ModelSerializer):
    """Сериализатор для создания заявки"""
    
    class Meta:
        model = Order
        fields = [
            'customer_name',
            'customer_phone',
            'customer_telegram_id',
            'customer_username',
            'product',
            'comment'
        ]