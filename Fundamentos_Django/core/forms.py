from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
   class Meta:
      model = Cliente
      fields = ('nome', 'idade', 'data_nascimento', 'is_ativo') # em caso de todos os campos usa "__all__"