from django.db import models

# Create your models here.
class catalog(models.Model):
    name = models.CharField('Название товара', max_length=100)
    description = models.CharField(max_length=254)
    sex = models.CharField('Пол', max_length=100)
    size = models.CharField('Размер', max_length=6)
    price = models.FloatField()
    image = models.ImageField(upload_to='images')
    def __str__(self):
        return self.name
    