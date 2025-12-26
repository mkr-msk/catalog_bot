from django.db import models


class Category(models.Model):
    """Категория товаров/услуг"""
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')
    order = models.IntegerField(default=0, verbose_name='Порядок сортировки')
    is_active = models.BooleanField(default=True, verbose_name='Активна')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создана')
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['order', 'name']
    
    def __str__(self):
        return self.name


class Product(models.Model):
    """Товар или услуга"""
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE, 
        related_name='products',
        verbose_name='Категория'
    )
    name = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        verbose_name='Цена'
    )
    image = models.ImageField(
        upload_to='products/', 
        blank=True, 
        null=True,
        verbose_name='Изображение'
    )
    telegram_file_id = models.CharField(
        max_length=200, 
        blank=True,
        verbose_name='Telegram File ID'
    )
    is_active = models.BooleanField(default=True, verbose_name='Активен')
    order = models.IntegerField(default=0, verbose_name='Порядок сортировки')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлён')
    
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['category', 'order', 'name']
    
    def __str__(self):
        return f"{self.category.name} - {self.name}"


class Order(models.Model):
    """Заявка от клиента"""
    STATUS_CHOICES = [
        ('new', 'Новая'),
        ('processing', 'В обработке'),
        ('completed', 'Завершена'),
        ('cancelled', 'Отменена'),
    ]
    
    customer_name = models.CharField(max_length=100, verbose_name='Имя клиента')
    customer_phone = models.CharField(max_length=20, verbose_name='Телефон')
    customer_telegram_id = models.BigIntegerField(verbose_name='Telegram ID')
    customer_username = models.CharField(
        max_length=100, 
        blank=True,
        verbose_name='Telegram Username'
    )
    
    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='orders',
        verbose_name='Товар'
    )
    comment = models.TextField(blank=True, verbose_name='Комментарий')
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='new',
        verbose_name='Статус'
    )
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создана')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлена')
    
    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Заявка #{self.id} от {self.customer_name}"