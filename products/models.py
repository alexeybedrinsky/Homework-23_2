from django.db import models


class Product(models.Model):
    name = models.CharField(
        max_length=50, verbose_name="Наименование", help_text="Введите наименование"
    )
    description = models.CharField(  # Исправлено на CharField, если это должно быть описание
        max_length=255,  # Установите подходящую длину
        verbose_name="Краткое описание",
        help_text="Краткое описание",
        blank=True,
        null=True
    )
    image_preview = models.ImageField(
        upload_to="product/photo",
        blank=True,
        null=True,
        verbose_name="Превью товара",
        help_text="Загрузите изображение товара",
    )
    category = models.ForeignKey(  # Переместили ForeignKey к категории
        'Category',
        on_delete=models.SET_NULL,
        help_text="Категория товара",
        blank=True,
        null=True,
        related_name='products'
    )
    purchase_price = models.CharField(
        max_length=50, verbose_name="Стоимость", help_text="Цена за покупку"
    )
    created_at = models.DateField(
        blank=True, verbose_name="Дата создания", help_text="Дата занесения в БД"
    )
    updated_at = models.DateField(
        blank=True,
        verbose_name="Дата последнего изменения",
        help_text="Дата последнего изменения в БД",
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "category"]  # Исправлено на существующие поля

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(
        max_length=50, verbose_name="Наименование", help_text="Введите наименование"
    )
    description = models.TextField(
        verbose_name="Описание", help_text="Краткое описание", blank=True, null=True
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name
