from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ImageField, ModelForm, TextInput

from .models import catalog


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
        widgets = {
            "name": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Введдите название товара",
                }
            ),
            "description": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Введите описание товара",
                }
            ),
            "sex": TextInput(
                attrs={"class": "form-control", "placeholder": "Введите пол"}
            ),
            "size": TextInput(
                attrs={"class": "form-control", "placeholder": "Введите размер товара"}
            ),
            "price": TextInput(
                attrs={"class": "form-control", "placeholder": "Введите цену товара"}
            ),
        }


class RegisterUserFrom(UserCreationForm):
    email = forms.EmailField(
        label="Email",
        required=True,
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Введите email"}
        ),
    )
    first_name = forms.CharField(
        label="Имя",
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Введите имя"}
        ),
    )
    last_name = forms.CharField(
        label="Фамилия",
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Введите фамилию"}
        ),
    )

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
            "first_name",
            "last_name",
        ]
        labels = {
            "username": "Имя пользователя",
            "email": "Email",
            "password1": "Пароль",
            "password2": "Подтверждение пароля",
        }

    def __init__(self, *args, **kwargs):
        super(RegisterUserFrom, self).__init__(*args, **kwargs)

        self.fields["username"].widget.attrs["class"] = "form-control"
        self.fields["password1"].widget.attrs["class"] = "form-control"
        self.fields["password2"].widget.attrs["class"] = "form-control"
