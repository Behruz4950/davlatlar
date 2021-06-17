from django.urls import path
from .views import *

urlpatterns = [
    path('',home, name='home'),
    path('create/',create, name='posts_create'),
    path('delete/<int:id>',delete, name='posts_delete'),
    path('update/<int:id>',update, name='posts_update'),
]
