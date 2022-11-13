# Generated by Django 4.1.3 on 2022-11-13 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0008_alter_catalog_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="catalog",
            name="category",
            field=models.CharField(
                choices=[("S", "Shirt"), ("P", "Pants"), ("J", "Sweater")],
                max_length=1,
                verbose_name="Категория",
            ),
        ),
    ]
