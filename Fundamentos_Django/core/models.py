from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)#nome do clinete em charfild(para string com tamanho maximo de 100, nao pode ser nulo e não pode ser em branco)
    idade = models.IntegerField(null=False, blank=True)
    data_nascimento = models.DateField(null=False, blank=False)
    is_ativo = models.BooleanField(null=False, default=True)#default(todo usuario que cadastrar estará ativo)