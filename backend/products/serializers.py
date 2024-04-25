from rest_framework import serializers

from products.models import (
    Category,
    Option,
    OptionValue,
    Product,
    ProductOptionValue,
    ProductImage,
)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "title")


class OptionValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = OptionValue
        fields = ("id", "title")


class OptionSerializer(serializers.ModelSerializer):
    values = OptionValueSerializer(many=True)

    class Meta:
        model = Option
        fields = ("id", "code", "title", "values")


class ProductOptionValueSerializer(serializers.ModelSerializer):
    option = OptionSerializer()
    values = OptionValueSerializer(many=True)

    class Meta:
        model = ProductOptionValue
        fields = ("id", "option", "values")


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ("id", "image", "is_main")


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True)
    category = CategorySerializer()
    options = ProductOptionValueSerializer(many=True)

    class Meta:
        model = Product
        fields = (
            "id",
            "images",
            "title",
            "content",
            "price",
            "category",
            "options",
        )
