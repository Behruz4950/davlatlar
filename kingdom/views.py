# from django.shortcuts import render
from kingdom import models
from django.views.generic import TemplateView, ListView
from kingdom.models import davlatlar


class IndexView(ListView):
    model = davlatlar
    template_name = 'index.html'
    context_object_name = 'davlatlar'