from rest_framework.generics import ListAPIView, RetrieveAPIView

from products import serializers, models


class CategoryListAPIView(ListAPIView):
    serializer_class = serializers.CategorySerializer
    queryset = models.Category.objects.all()


class CategoryRetrieveAPIView(RetrieveAPIView):
    serializer_class = serializers.CategorySerializer
    queryset = models.Category.objects.all()


class OptionListAPIView(ListAPIView):
    serializer_class = serializers.OptionSerializer
    queryset = models.Option.objects.all().prefetch_related("values")


class OptionRetrieveAPIView(RetrieveAPIView):
    serializer_class = serializers.OptionSerializer
    queryset = models.Option.objects.all().prefetch_related("values")


class ProductListAPIView(ListAPIView):
    serializer_class = serializers.ProductSerializer
    queryset = (
        models.Product.objects.all()
        .prefetch_related("options", "images", "options__option__values")
        .select_related("category")
    )


class ProductRetrieveAPIView(RetrieveAPIView):
    serializer_class = serializers.ProductSerializer
    queryset = (
        models.Product.objects.all()
        .prefetch_related("options", "images", "options__option__values")
        .select_related("category")
    )
