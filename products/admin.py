from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from products.models import (
    Category,
    Option,
    OptionValue,
    Product,
    ProductImage,
    ProductOptionValue,
)


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ("id", "title")
    list_display_links = ("id", "title")


@admin.register(Option)
class OptionAdmin(TranslationAdmin):
    list_display = ("id", "title")


@admin.register(OptionValue)
class OptionValueAdmin(TranslationAdmin):
    list_display = ("id", "title", "option")
    list_display_links = ("id", "title")


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "image", "is_main")
    list_display_links = ("id", "product")


class ImageInline(admin.StackedInline):
    model = ProductImage


@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    list_display = ("id", "title")
    list_display_links = ("id", "title")

    inlines = (ImageInline,)


@admin.register(ProductOptionValue)
class ProductOptionValueAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "option")
    list_display_links = ("id", "product")
