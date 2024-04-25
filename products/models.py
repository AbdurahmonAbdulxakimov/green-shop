from django.db import models
from ckeditor.fields import RichTextField

from utils.models import BaseModel


class Category(BaseModel):
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title


class Option(BaseModel):
    code = models.CharField(max_length=255, unique=True)
    title = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.title


class OptionValue(BaseModel):
    option = models.ForeignKey(Option, on_delete=models.CASCADE, related_name="values")
    title = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.title


class Product(BaseModel):
    title = models.CharField(max_length=255)
    content = RichTextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=15)

    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="products") # noqa

    def __str__(self) -> str:
        return self.title


class ProductOptionValue(BaseModel):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="options"
    )
    option = models.ForeignKey(Option, on_delete=models.CASCADE)
    values = models.ManyToManyField(OptionValue)


class ProductImage(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images") # noqa
    image = models.ImageField(upload_to="products/", editable=True)

    is_main = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.image.name
