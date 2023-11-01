
from django.http import HttpResponseRedirect
from django.shortcuts import render
import datetime 
from .forms import ClienteForm

# Create your views here.


def hora_sistema(request):
    hora_sistema = datetime.datetime.now()
    return render(request,'lista_horario.html', context={'hora_sistema':hora_sistema})

def exibir_template(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('hora_sistema')
    form = ClienteForm()
    return render(request, 'form_cliente.html', context={'form': form})