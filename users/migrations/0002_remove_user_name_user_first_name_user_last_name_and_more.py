# Generated by Django 4.2.7 on 2024-04-17 17:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="name",
        ),
        migrations.AddField(
            model_name="user",
            name="first_name",
            field=models.CharField(
                blank=True, max_length=150, verbose_name="first name"
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="last_name",
            field=models.CharField(
                blank=True, max_length=150, verbose_name="last name"
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="phone_number",
            field=models.CharField(
                default=1,
                max_length=16,
                validators=[
                    django.core.validators.RegexValidator(
                        message="Phone number must be entered in the format: '+999999999'. Up to 13 digits allowed.",
                        regex="^\\+?1?\\d{9,15}$",
                    )
                ],
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(
                blank=True, max_length=254, unique=True, verbose_name="email address"
            ),
        ),
    ]
