from django.urls import path

from products import views


app_name = "products"

urlpatterns = [
    path(
        "",
        views.ProductListAPIView.as_view(),
        name="product_list",
    ),
    path(
        "<int:pk>/",
        views.ProductRetrieveAPIView.as_view(),
        name="product_retrieve",
    ),
    path("category/", views.CategoryListAPIView.as_view(), name="category_list"),
    path(
        "category/<int:pk>/",
        views.CategoryRetrieveAPIView.as_view(),
        name="category_retrieve",
    ),
    path(
        "option/",
        views.OptionListAPIView.as_view(),
        name="option_list",
    ),
    path(
        "option/<int:pk>/",
        views.OptionRetrieveAPIView.as_view(),
        name="option_retrieve",
    ),
]
