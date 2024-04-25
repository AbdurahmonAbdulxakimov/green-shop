from django.db.models.signals import pre_save
from django.dispatch import receiver

from order.models import Basket, Cart


@receiver(pre_save, sender=Cart)
def update_basket(sender, instance, **kwargs):
    instance.basket.subtotal += instance.price
    instance.basket.total += instance.basket.subtotal + instance.basket.shiping
    instance.basket.save()
