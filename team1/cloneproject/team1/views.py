from django.shortcuts import redirect, render, get_object_or_404
from .models import *

# Create your views here.
def home(request):
    return render(request, 'home.html')

def detail(request, id):
    team1 = get_object_or_404(Team1, pk = id)
    return render(request, 'detail.html', {'team1':team1})

def new(request):
    return render(request, 'new.html')

def create(request):
    new = Team1
    new.name = request.POST['name']
    new.price = request.POST['price']
    new.sale_price = request.POST['sale_price']
    new.sale_period = request.POST['sale_period']
    new.color = request.POST['color']
    new.img = request.POST['img']
    new.save()
    return redirect('home')

def edit(request, id):
    team1 = Team1.objects.get(id = id)
    return render(request, 'edit.html', {'team1':team1})

def update(request, id):
    update = Team1.objects.get(id = id)
    update.name = request.POST['name']
    update.price = request.POST['price']
    update.sale_price = request.POST['sale_price']
    update.sale_period = request.POST['sale_period']
    update.color = request.POST['color']
    update.save()
    return redirect('detail', update.id)

def delete(request, id):
    delete = Team1.objects.get(id = id)
    delete.delete()
    return redirect('home')
