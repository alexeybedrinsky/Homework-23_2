from django.core.cache import cache
from django.db.models import Count
from .models import Category, Product


def get_cached_categories():
    key = 'all_categories'
    categories = cache.get(key)
    if not isinstance(categories, list) or 'product_count' not in categories[0]:
        categories = list(Category.objects.annotate(product_count=Count('products')).values())
        cache.set(key, categories, 3600)  # cache for 1 hour
    return categories


def get_cached_products():
    key = 'all_products'
    products = cache.get(key)
    if products is None:
        products = list(Product.objects.values())
        cache.set(key, products, 1800)  # кэшируем на 30 минут
    return products