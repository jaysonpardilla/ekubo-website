from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'business', 'created_at')
    search_fields = ('name', 'business__name')
    list_filter = ('created_at',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock', 'is_available', 'created_at')
    search_fields = ('name', 'category__name', 'business__name')
    list_filter = ('is_available', 'created_at')
    raw_id_fields = ('category', 'business')
