from django.db import models


class Category(models.Model):
    objects = None
    name = models.CharField(max_length=100, verbose_name="Наименование категории")
    description = models.TextField(null=True, blank=True, verbose_name="Описание категории")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]

    @property
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=50, verbose_name="Наименование", help_text="Введите наименование"
    )
    description = models.CharField(
        max_length=255,
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
    category = models.ForeignKey(
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
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
        help_text="Дата занесения в БД"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата обновления",
        help_text="Дата последнего обновления"
    )
    views_counter = models.PositiveIntegerField(
        verbose_name="Счетчик просмотров",
        help_text="Количество просмотров",
        default=0
    )
    manufactured_at = models.DateField(
        blank=True,
        verbose_name="Дата производства",
        help_text="Дата производства продукта",
        null=True
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "category"]

    def __str__(self):
        return self.name
