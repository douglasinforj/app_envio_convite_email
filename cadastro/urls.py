from django.urls import path 
from . import views

app_name = 'cadastro'

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastrar/', views.cadastrar_pessoa, name='cadastrar'),
    path('listar/', views.listar_pessoas, name='listar_pessoas'),
    path('pessoa/<int:pk>/', views.detalhes_pessoa, name='detalhes_pessoa'),
    path('pessoa/<int:pk>/convite', views.enviar_convite, name='enviar_convite'),

]
