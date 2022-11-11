from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import catalogForm
from .models import catalog


# Create your views here.
def index(request):
    catalog_list = catalog.objects.all()
    return render(request, 'main/index.html', {'title':'Главная страница', 'catalog_list': catalog_list})

def about(request):
    return render(request, 'main/about.html')

def create(request):
    submitted = False
    if request.method == 'POST':
        form = catalogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/create?submitted=True')
    else:
        form = catalogForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'main/create.html', {'form': form, 'submitted': submitted})

class RegisterFormView(CreateView):
    form_class = UserCreationForm
    template_name = "main/register.html"
    success_url = reverse_lazy('index')
    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)
    def form_invalid(self, form):
        return super(RegisterFormView, self).form_invalid(form)

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.success(request, 'Логин или пароль неверны')
            return render(request, 'main/login.html')
    else: 
        return render(request, 'main/login.html')

def logout_user(request):
    logout(request)
    messages.success(request, ('Вы вышли из аккаунта'))
    return redirect('index')