from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from .forms import PessoaForm, ConviteForm
from django.contrib import messages
from .models import Pessoa
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.conf import settings



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



def detalhes_pessoa(request, pk):
    pessoa = get_list_or_404(Pessoa, pk=pk)
    return render(request, 'cadastro/detalhes.html', {'pessoa':pessoa})


def enviar_convite(request, pk):
    pessoa = get_object_or_404(Pessoa, pk=pk)
    
    if request.method == 'POST':
        form = ConviteForm(request.POST)
        if form.is_valid():
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']
            
            try:
                # Renderizar template HTML
                html_content = render_to_string('emails/convite.html', {
                    'pessoa': pessoa,
                    'mensagem': mensagem
                })
                
                # Criar e-mail
                email = EmailMultiAlternatives(
                    subject=assunto,
                    body=mensagem,  # Versão texto
                    from_email=settings.EMAIL_HOST_USER,
                    to=[pessoa.email]
                )
                
                # Anexar versão HTML
                email.attach_alternative(html_content, "text/html")
                
                # Enviar e-mail
                email.send()
                
                # Marcar convite como enviado
                pessoa.enviar_convite()
                
                messages.success(request, f'Convite enviado para {pessoa.nome}!')
                return redirect('detalhes_pessoa', pk=pessoa.pk)
                
            except Exception as e:
                messages.error(request, f'Erro ao enviar e-mail: {str(e)}')
    else:
        form = ConviteForm()
    
    return render(request, 'cadastro/enviar_convite.html', {
        'form': form,
        'pessoa': pessoa
    })






