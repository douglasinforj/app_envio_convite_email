from django.urls import path 
from . import views

app_name = 'cadastro'

urlpatterns = [
    path('', views.index, name='index'),
]
