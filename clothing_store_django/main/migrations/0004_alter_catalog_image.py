# Generated by Django 4.1.3 on 2022-11-13 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0003_alter_catalog_image_alter_catalog_size"),
    ]

    operations = [
        migrations.AlterField(
            model_name="catalog",
            name="image",
            field=models.ImageField(blank=True, upload_to="static/main/images"),
        ),
    ]
