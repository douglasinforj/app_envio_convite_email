from django.shortcuts import render, redirect
from .forms import PessoaForm
from django.contrib import messages
from .models import Pessoa



def index(request):
    return render(request, 'cadastro/index.html')


def cadastrar_pessoa(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            pessoa = form.save()
            messages.success(request, f'{pessoa.nome} cadastrado com sucesso!')
            return redirect('listar_pessoas')
    else:
        form = PessoaForm()
    
    return render(request, 'cadastro/cadastrar.html', {'form': form})

def listar_pessoas(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'cadastro/listar.html', {'pessoas': pessoas})

