
from django.shortcuts import render
import datetime 

# Create your views here.


def hora_sistema(request):
    hora_sistema = datetime.datetime.now()
    return render(request,'lista_horario.html', context={'hora_sistema':hora_sistema})