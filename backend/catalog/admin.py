from django.contrib import admin
from .models import Category, Product, Order


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'order', 'is_active', 'created_at']
    list_editable = ['order', 'is_active']
    list_filter = ['is_active']
    search_fields = ['name', 'description']
    ordering = ['order', 'name']