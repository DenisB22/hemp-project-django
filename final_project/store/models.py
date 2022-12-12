from django.db import models
from django.db.models import Avg, Count
from django.urls import reverse

from final_project.accounts.models import Account
from final_project.category.models import Category


# Create your models here.


class Product(models.Model):
    MAX_LEN_NAME = 50
    MAX_LEN_SLUG = 50
    product_name = models.CharField(
        max_length=MAX_LEN_NAME,
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
        null=False,
        blank=False,
    )

    price = models.IntegerField(
        null=False,
        blank=False,
    )

    images = models.ImageField(
        upload_to='photos/products'
    )

    stock = models.IntegerField(
        null=False,
        blank=False,
    )

    is_available = models.BooleanField(
        default=True,
        null=False,
        blank=False,
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )

    created_date = models.DateTimeField(
        auto_now_add=True,
    )

    modified_date = models.DateTimeField(
        auto_now=True,
    )

    is_popular = models.BooleanField(
        default=False,
        null=False,
        blank=False,
    )

    class Meta:
        ordering = ('pk',)

    def get_url(self):
        return reverse('product_details', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.product_name

    def averageReview(self):
        reviews = ReviewRating.objects.filter(product=self, status=True).aggregate(average=Avg('rating'))
        avg = 0
        if reviews['average'] is not None:
            avg = float(reviews['average'])
        return avg

    def countReview(self):
        reviews = ReviewRating.objects.filter(product=self, status=True).aggregate(count=Count('id'))
        count = 0
        if reviews['count'] is not None:
            count = int(reviews['count'])
        return count


class VariationManager(models.Manager):
    def sizes(self):
        return super(VariationManager, self).filter(variation_category='size', is_active=True)


class Variation(models.Model):
    MAX_LEN_VARIATION_CATEGORY = 100
    MAX_LEN_VARIATION_VALUE = 100

    variation_category_choice = (
        ('size', 'size'),
    )

    objects = VariationManager()

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    variation_category = models.CharField(
        max_length=MAX_LEN_VARIATION_CATEGORY,
        choices=variation_category_choice,
    )

    variation_value = models.CharField(
        max_length=MAX_LEN_VARIATION_VALUE,
    )

    is_active = models.BooleanField(
        default=True,
    )

    created_date = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.variation_value


class ReviewRating(models.Model):
    MAX_LEN_SUBJECT = 100
    MAX_LEN_REVIEW = 500
    MAX_LEN_IP = 20

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )

    user = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
    )

    subject = models.CharField(
        max_length=MAX_LEN_SUBJECT,
        blank=True,
    )

    review = models.TextField(
        max_length=MAX_LEN_REVIEW,
        blank=True,
    )

    rating = models.FloatField(
        null=False,
        blank=False,
    )

    ip = models.CharField(
        max_length=MAX_LEN_IP,
        blank=True,
    )

    status = models.BooleanField(
        default=True,
        null=False,
        blank=False,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        null=False,
        blank=False,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.subject


class ProductGallery(models.Model):
    MAX_LEN_IMAGE = 255

    product = models.ForeignKey(
        Product,
        default=None,
        on_delete=models.CASCADE,
    )

    image = models.ImageField(
        upload_to='store/products',
        max_length=MAX_LEN_IMAGE,
    )

    def __str__(self):
        return self.product.product_name

    class Meta:
        verbose_name = 'productgallery'
        verbose_name_plural = 'product gallery'







