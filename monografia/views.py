import re
from django.shortcuts import render, redirect
from django.http import HttpResponse
from monografia.forms import AutoresForm,CoAutoresForm, DiscentesForm, MonografiasForm
from monografia.models import Autores, CoAutores,Discentes,Monografias


### -----------------Listagens das views ----------------
def home(request):
    return render("index.html")

def home(request):
    data = {}
    data['autores'] = Autores.objects.all()
    data['coautores'] = CoAutores.objects.all()
    data['discentes'] = Discentes.objects.all()
    data['monografias'] = Monografias.objects.all()
    return render(request,"index.html", data)


def buscarMonografias(request):
    data = {}
    orientador = request.GET.get('orientador')
    if orientador:
        data['monografias'] = Monografias.objects.filter(orientador__icontains=orientador)
        data['titulo'] = orientador
        return render(request,"buscarMonografia.html", data)
    else:
     data['monografias'] = Monografias.objects.all()
     return render(request,"buscarMonografia.html", data)




    
def formAutores(request):
    data = {}
    data['form'] = AutoresForm()
    return render(request,"formAutores.html", data)

def formCoAutores(request):
    data = {}
    data['form'] = CoAutoresForm()
    return render(request,"formCoAutores.html", data)

def formDiscentes(request):
    data = {}
    data['form'] = DiscentesForm()
    return render(request,"formDiscentes.html", data)

def formMonografias(request):
    data = {}
    data['form'] = MonografiasForm()
    return render(request,"formMonografias.html", data)



### -----------------Criação no banco ----------------
def createautores(request):
    form = AutoresForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def createcoautores(request):
    form = CoAutoresForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def creatediscentes(request):
    form = DiscentesForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def createmonografia(request):
    form = MonografiasForm(request.POST or None)
    form.save()
    return redirect('home')
    