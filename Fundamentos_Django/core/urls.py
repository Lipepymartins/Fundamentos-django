from django.contrib import admin
from django.urls import path, include
from .views import hora_sistema, exibir_template

urlpatterns = [
    path('hora_sistema', hora_sistema),
    path('exibir_template', exibir_template),
]