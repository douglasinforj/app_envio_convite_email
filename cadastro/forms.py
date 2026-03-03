from django import forms
from .models import Pessoa

class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ['nome', 'email', 'telefone']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome completo'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email@exemplo.com'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(00) 00000-0000'}),
        }

        def clean_email(self):
            email = self.cleaned_data.get('email')
            if Pessoa.objects.filter(email=email).exists():                        #verifica no banco se email existe
                raise forms.ValidationError('Este email já existe cadastrado!')
            return email
        

class ConviteForm(forms.Form):
    assunto = forms.CharField(
        max_length=200,
        initial='Convite para paraticipar do nosso evento',
        widget=forms.TextInput(attrs={'class':'form-control'})
    )
    mensagem = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        initial='Olá {nome},\n\nGostaríamos de convidá-lo para participar do nosso sistema...\n\nAtenciosamente,\nEquipe'
    )