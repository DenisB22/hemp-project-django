from django.db import models
from django.urls import reverse


# Create your models here.


class Category(models.Model):
    MAX_LEN_CATEGORY = 50
    MAX_LEN_SLUG = 100

    category_name = models.CharField(
        max_length=MAX_LEN_CATEGORY,
        unique=True,
        null=False,
        blank=False,
    )

    slug = models.SlugField(
        max_length=MAX_LEN_SLUG,
        unique=True,
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    category_image = models.ImageField(
        upload_to='photos/categories',
        blank=True,
    )

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('products_by_category', args=[self.slug])

    def __str__(self):
        return self.category_name
