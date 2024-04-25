from modeltranslation.translator import register, TranslationOptions
from products.models import (
    Category,
    Option,
    OptionValue,
    Product,
)


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ("title",)


@register(Option)
class OptionTranslationOptions(TranslationOptions):
    fields = ("title",)


@register(OptionValue)
class OptionValueTranslationOptions(TranslationOptions):
    fields = ("title",)


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ("title", "content")
