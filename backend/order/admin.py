from django.contrib import admin

from order.models import Cart, Basket, Order


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("id", "basket", "product", "amount", "price")
    list_display_links = ("id", "amount", "price")


class CartInline(admin.StackedInline):
    model = Cart
    extra = 1


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "total")
    list_display_links = ("id", "total")

    inlines = (CartInline,)


# @admin.register(Order)
# class OrderAdmin(admin.ModelAdmin):
#     list_display = ("id", "user", "total")
#     list_display_links = ("id", "total")
