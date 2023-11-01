from django.http import HttpResponse
from django.shortcuts import render
import datetime 

# Create your views here.


def hora_sistema(request):
    hora_sistema = datetime.datetime.now()
    return HttpResponse(hora_sistema)