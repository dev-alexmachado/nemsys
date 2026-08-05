from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastrarEvento/', views.cadastrar_evento, name='cadastrar_evento')
]