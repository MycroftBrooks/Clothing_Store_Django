from .models import catalog
from django.forms import ModelForm, TextInput


class catalogForm(ModelForm):
    class Meta:
        model = catalog
        fields = ["name", "description", "sex", "size", "price", "image"]
        """ widgets = {"name": TextInput(attrs={"class": "form-control", "placeholder": "Введдите название товара"}),
                   "description": TextInput(attrs={"class": "form-control", "placeholder": "Введите описание товара"}), 
                   "sex": TextInput(attrs={"class": "form-control", "placeholder": "Введите пол"}),
                   "size": TextInput(attrs={"class": "form-control", "placeholder": "Введите размер товара"}),
                   "price": TextInput(attrs={"class": "form-control", "placeholder": "Введите цену товара"})
        } """