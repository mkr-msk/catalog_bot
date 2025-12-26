from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Category, Product, Order
from .serializers import (
    CategorySerializer,
    ProductListSerializer,
    ProductDetailSerializer,
    OrderCreateSerializer
)


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """API для категорий (только чтение)"""
    queryset = Category.objects.filter(is_active=True)
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    """API для товаров (только чтение)"""
    queryset = Product.objects.filter(is_active=True).select_related('category')
    
    def get_serializer_class(self):
        """Выбор сериализатора в зависимости от действия"""
        if self.action == 'retrieve':
            return ProductDetailSerializer
        return ProductListSerializer
    
    @action(detail=False, methods=['get'], url_path='by-category/(?P<category_id>[0-9]+)')
    def by_category(self, request, category_id=None):
        """Получить товары конкретной категории"""
        products = self.get_queryset().filter(category_id=category_id)
        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data)


class OrderViewSet(viewsets.ModelViewSet):
    """API для заявок (создание и чтение)"""
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer
    
    def get_queryset(self):
        """Ограничение доступа только к своим заявкам (для будущего)"""
        return super().get_queryset()