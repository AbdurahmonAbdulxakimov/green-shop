# Generated by Django 4.2.7 on 2024-04-18 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("order", "0002_alter_basket_subtotal_alter_basket_total_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="basket",
            name="carts",
        ),
        migrations.RemoveField(
            model_name="order",
            name="carts",
        ),
        migrations.RemoveField(
            model_name="order",
            name="shiping",
        ),
        migrations.RemoveField(
            model_name="order",
            name="subtotal",
        ),
        migrations.RemoveField(
            model_name="order",
            name="total",
        ),
        migrations.RemoveField(
            model_name="order",
            name="user",
        ),
        migrations.AddField(
            model_name="cart",
            name="basket",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="carts",
                to="order.basket",
            ),
            preserve_default=False,
        ),
    ]
