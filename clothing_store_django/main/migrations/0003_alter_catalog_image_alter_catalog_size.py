# Generated by Django 4.1.3 on 2022-11-11 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0002_alter_catalog_image_alter_catalog_size"),
    ]

    operations = [
        migrations.AlterField(
            model_name="catalog",
            name="image",
            field=models.ImageField(blank=True, upload_to="images"),
        ),
        migrations.AlterField(
            model_name="catalog",
            name="size",
            field=models.CharField(max_length=6, verbose_name="Размер"),
        ),
    ]
