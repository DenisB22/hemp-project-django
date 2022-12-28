from django.db import models

from final_project.accounts.models import Account
from final_project.store.models import Product, Variation


# Create your models here.


class Payment(models.Model):
    MAX_LEN_PAYMENT_ID = 100
    MAX_LEN_PAYMENT_METHOD = 100
    MAX_LEN_AMOUNT_PAID = 100
    MAX_LEN_STATUS = 100

    user = models.ForeignKey(
        Account,
        on_delete=models.CASCADE
    )

    payment_id = models.CharField(
        max_length=MAX_LEN_PAYMENT_ID,
    )

    payment_method = models.CharField(
        max_length=MAX_LEN_PAYMENT_METHOD,
    )

    amount_paid = models.CharField(
        max_length=MAX_LEN_AMOUNT_PAID,
    )

    status = models.CharField(
        max_length=MAX_LEN_STATUS,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return self.payment_id


class Order(models.Model):
    MAX_LEN_ORDER_NUMBER = 20
    MAX_LEN_FIRST_NAME = 50
    MAX_LEN_LAST_NAME = 50
    MAX_LEN_PHONE = 15
    MAX_LEN_EMAIL = 50
    MAX_LEN_ADDRESS_LINE_1 = 50
    MAX_LEN_ADDRESS_LINE_2 = 50
    MAX_LEN_COUNTRY = 50
    MAX_LEN_STATE = 50
    MAX_LEN_CITY = 50
    MAX_LEN_ORDER_NOTE = 100
    MAX_LEN_STATUS = 10
    MAX_LEN_IP = 20

    STATUS = (
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    )

    user = models.ForeignKey(
        Account,
        on_delete=models.SET_NULL,
        null=True,
    )

    payment = models.ForeignKey(
        Payment,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    order_number = models.CharField(
        max_length=MAX_LEN_ORDER_NUMBER,
        null=False,
        blank=False,
    )

    first_name = models.CharField(
        max_length=MAX_LEN_FIRST_NAME,
        null=False,
        blank=False,
    )

    last_name = models.CharField(
        max_length=MAX_LEN_LAST_NAME,
        null=False,
        blank=False,
    )

    phone = models.CharField(
        max_length=MAX_LEN_PHONE,
        null=False,
        blank=False,
    )

    email = models.EmailField(
        max_length=MAX_LEN_EMAIL,
        null=False,
        blank=False,
    )

    address_line_1 = models.CharField(
        max_length=MAX_LEN_ADDRESS_LINE_1,
        null=False,
        blank=False,
    )

    address_line_2 = models.CharField(
        max_length=MAX_LEN_ADDRESS_LINE_2,
        blank=True,
        null=True,
    )

    country = models.CharField(
        max_length=MAX_LEN_COUNTRY,
        null=False,
        blank=False,
    )

    state = models.CharField(
        max_length=MAX_LEN_STATE,
        null=True,
        blank=True,
    )

    city = models.CharField(
        max_length=MAX_LEN_CITY,
        null=False,
        blank=False,
    )

    order_note = models.CharField(
        max_length=MAX_LEN_ORDER_NOTE,
        null=True,
        blank=True,
    )

    order_total = models.FloatField(
        null=False,
        blank=False,
    )

    tax = models.FloatField(
        null=False,
        blank=False,
    )

    status = models.CharField(
        max_length=MAX_LEN_STATUS,
        choices=STATUS,
        default='New',
        null=False,
        blank=False,
    )

    ip = models.CharField(
        max_length=MAX_LEN_IP,
        null=False,
        blank=False,
    )

    is_ordered = models.BooleanField(
        default=False,
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
        blank=False,
        null=False,
    )

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def full_address(self):
        return f'{self.address_line_1} {self.address_line_2}'

    def __str__(self):
        return self.first_name


class OrderProduct(models.Model):
    MAX_LEN_COLOR = 50
    MAX_LEN_SIZE = 50

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )

    payment = models.ForeignKey(
        Payment,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    user = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )

    variations = models.ManyToManyField(
        Variation,
        blank=True,
    )

    quantity = models.IntegerField(
        null=False,
        blank=False,
    )

    product_price = models.FloatField(
        null=False,
        blank=False,
    )

    ordered = models.BooleanField(
        default=False,
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
        return self.product.product_name



