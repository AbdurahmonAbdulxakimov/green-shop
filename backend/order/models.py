from django.db import models
from django.contrib.auth import get_user_model

from utils.models import BaseModel
from products.models import Product


User = get_user_model()


class Basket(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="baskets")
    subtotal = models.DecimalField(decimal_places=2, max_digits=15, default=0)
    shiping = models.DecimalField(decimal_places=2, max_digits=15, default=30_000.00)
    total = models.DecimalField(decimal_places=2, max_digits=15, default=0)


class Cart(BaseModel):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE, related_name="carts")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="carts")

    amount = models.PositiveIntegerField(default=1)
    price = models.DecimalField(decimal_places=2, max_digits=15, default=0)

    def __str__(self) -> str:
        return f"{self.product_id} - {self.amount}"

    def save(self, *args, **kwargs):
        self.price = self.product.price * self.amount
        super(Cart, self).save(*args, **kwargs)


class Order(BaseModel):
    pass
