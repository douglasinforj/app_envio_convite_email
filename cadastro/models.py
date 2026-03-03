from django.db import models


class Pessoa(models.Model):
    nome = models.CharField('Nome', max_length=100)
    email = models.EmailField('E-mail', unique=True)
    telefone = models.CharField('Telefone', max_length=20, blank=True)
    data_cadastro = models.DateTimeField('Data de Cadastro', auto_now_add=True)
    convite_enviado = models.BooleanField('Convite Enviado', default=False)
    data_convite = models.DateTimeField('Data do Convite', null=True, blank=True)
    ativo = models.BooleanField('Ativo', default=True)
    
    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'
        ordering = ['-data_cadastro']
    
    def __str__(self):
        return self.nome
    

