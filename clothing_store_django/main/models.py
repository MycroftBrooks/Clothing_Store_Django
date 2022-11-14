from django.conf import settings
from django.db import models
from django.urls import reverse

CATEGORY_CHOICES = (
    ("S", "Shirt"),
    ("P", "Pants"),
    ("J", "Sweater"),
)

SEX_CHOICES = (("M", "Для мужчин"), ("W", "Для женщин"))

SIZE_CHOICES = (
    ("XS", "XS"),
    ("S", "S"),
    ("M", "M"),
    ("L", "L"),
    ("XL", "XL"),
    ("XXL", "XXL"),
)


class catalog(models.Model):
    name = models.CharField("Название товара", max_length=100)
    category = models.CharField("Категория", choices=CATEGORY_CHOICES, max_length=1)
    sex = models.CharField("Пол", choices=SEX_CHOICES, max_length=1)
    size = models.CharField("Размер", choices=SIZE_CHOICES, max_length=3)
    price = models.FloatField()
    image = models.ImageField(blank=True, upload_to="static/main/images")
    """ slug = models.SlugField() """

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product", kwargs={"pk": self.pk})
        """ return reverse("main:product", kwargs={
            'slug': self.slug
            }) """


class OrderItem(models.Model):
    item = models.ForeignKey(catalog, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.name
