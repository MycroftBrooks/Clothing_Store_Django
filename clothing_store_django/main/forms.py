from .models import catalog
from django.forms import ImageField, ModelForm, TextInput


class catalogForm(ModelForm):
    class Meta:
        model = catalog
        fields = ["name", "description", "sex", "size", "price", "image"]
        labels = {
            "name": "Название товара",
            "description": "Описание",
            "sex": "Пол",
            "size": "Размер",
            "price": "Цена",
            "image": "Изображение",
        }
        widgets = {"name": TextInput(attrs={"class": "form-control", "placeholder": "Введдите название товара"}),
                   "description": TextInput(attrs={"class": "form-control", "placeholder": "Введите описание товара"}), 
                   "sex": TextInput(attrs={"class": "form-control", "placeholder": "Введите пол"}),
                   "size": TextInput(attrs={"class": "form-control", "placeholder": "Введите размер товара"}),
                   "price": TextInput(attrs={"class": "form-control", "placeholder": "Введите цену товара"})
        } 