from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Product, Order


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'order', 'is_active', 'created_at']
    list_editable = ['order', 'is_active']
    list_filter = ['is_active']
    search_fields = ['name', 'description']
    ordering = ['order', 'name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'image_preview', 'is_active', 'order']
    list_editable = ['is_active', 'order']
    list_filter = ['category', 'is_active']
    search_fields = ['name', 'description']
    ordering = ['category', 'order', 'name']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('category', 'name', 'description', 'price')
        }),
        ('Изображение', {
            'fields': ('image', 'telegram_file_id'),
            'description': 'Загрузите изображение или укажите Telegram File ID'
        }),
        ('Настройки', {
            'fields': ('is_active', 'order')
        }),
    )
    
    readonly_fields = ['created_at', 'updated_at']
    
    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height: 50px; max-width: 100px;" />',
                obj.image.url
            )
        return "Нет изображения"
    
    image_preview.short_description = 'Превью'