# Generated by Django 4.2.7 on 2024-04-17 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        (
            "products",
            "0002_rename_description_product_content_category_title_en_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="category",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="products",
                to="products.category",
            ),
            preserve_default=False,
        ),
    ]
