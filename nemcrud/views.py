from django.shortcuts import render, redirect
from .models import Evento

# Create your views here.
def index(request):
    return render(request, "index.html")

def cadastrar_evento(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        lotacao = request.POST.get('lotacao')
        dia = request.POST.get('dia')
        horario = request.POST.get('horario')
        ingresso = request.POST.get('ingresso')
        telefone = request.POST.get('telefone')
        endereco = request.POST.get('endereco')
        Evento.objects.create(
            nome=nome,lotacao=lotacao,dia=dia,horario=horario,ingresso=ingresso,telefone=telefone,endereco=endereco
        )
        return redirect('index')
    return render(request, 'cadastrar-evento.html')