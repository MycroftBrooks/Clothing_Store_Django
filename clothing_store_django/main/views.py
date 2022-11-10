from django.shortcuts import redirect, render
from .models import catalog
from .forms import catalogForm


# Create your views here.
def index(request):
    catalog_list = catalog.objects.all()
    return render(request, 'main/index.html', {'title':'Главная страница', 'catalog_list': catalog_list})

def about(request):
    return render(request, 'main/about.html')

def create(request):
    error = ''
    if request.method == 'POST':
        form = catalogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = 'Форма неверна'
    form = catalogForm()
    context = {
        'form': form,
    }
    return render(request, 'main/create.html')