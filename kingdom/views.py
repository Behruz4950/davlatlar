from typing import Text
from django.db import models
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Davlatlar
from django.shortcuts import redirect

def home(request):
    context = {
        'posts': Davlatlar.objects.all(),
    }
    return render(request,"home.html",context)


def create(request):
    if request.method == 'POST':
        p = Davlatlar(text=request.POST['title'])
        p.save()
        return redirect('home')
    
    return render(request,'create.html')


def update(request,id):
    try:
        p = Davlatlar.objects.get(id=id)
    except Davlatlar.DoesNotExist:
        return redirect('home')

    if request.method == 'POST':
        p.text = request.POST['title']
        p.save()

        return redirect('home')

    return render(request,'create.html',{
        'p':p
    })


def delete(request,id):
    Davlatlar.objects.filter(id=id).delete()
    return redirect('home')