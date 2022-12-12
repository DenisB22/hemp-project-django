from django.db import models
from django.db.models import ManyToManyField

from final_project.accounts.models import Account
from final_project.store.models import Product, Variation


# Create your models here.


class Cart(models.Model):
    MAX_LEN_CART_ID = 50

    cart_id = models.CharField(
        max_length=MAX_LEN_CART_ID,
        null=False,
        blank=False,
    )

    date_added = models.DateField(
        auto_now_add=True,
        blank=False,
        null=False,
    )

    def __str__(self):
        return self.cart_id


class CartItem(models.Model):
    user = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        null=True,
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

    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        null=True,
    )

    quantity = models.IntegerField(
        null=False,
        blank=False,
    )

    is_active = models.BooleanField(
        default=True,
        null=False,
        blank=False,
    )

    def sub_total(self):
        return self.product.price * self.quantity

    def __unicode__(self):
        return self.product




