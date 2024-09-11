from django.contrib import admin
from products.models import Product, Category


@admin.register(Product)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "purchase_price", "category")
    list_filter = ("category",)
    search_fields = ("name", "description")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")

