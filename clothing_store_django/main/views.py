from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import RegisterUserFrom, catalogForm
from .models import Order, OrderItem, catalog


# Create your views here.
def index(request):
    context = {"catalog_list": catalog.objects.all()}
    return render(
        request,
        "main/index.html",
        context,
    )


def about(request):
    return render(request, "main/about.html")


def create(request):
    submitted = False
    if request.method == "POST":
        form = catalogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/create?submitted=True")
    else:
        form = catalogForm
        if "submitted" in request.GET:
            submitted = True
    return render(request, "main/create.html", {"form": form, "submitted": submitted})


def register_user(request):
    if request.method == "POST":
        form = RegisterUserFrom(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Вы зарегистрировались как " + username))
            return redirect("index")
    else:
        form = RegisterUserFrom()
    return render(request, "main/register.html", {"form": form})


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            messages.success(request, "Логин или пароль неверны")
            return render(request, "main/login.html")
    else:
        return render(request, "main/login.html")


def logout_user(request):
    logout(request)
    messages.success(request, ("Вы вышли из аккаунта"))
    return redirect("index")
