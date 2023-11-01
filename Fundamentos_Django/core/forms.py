from django import forms

class ClienteForm(forms.Form):
    nome = forms.CharField(label="Nome do cliente", max_length=100) # para strings
    idade = forms.IntegerField(label="Idade do cliente") # para numeros inteiros
    data_nascimento = forms.DateField(label="Data de nascimento do cliente") # para datas
    is_ativo = forms.BooleanField(label="Se o cliente está ativo") # para resultados booleanos (sim/não)