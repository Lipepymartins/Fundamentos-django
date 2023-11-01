from django.contrib import admin
from django.urls import path, include
from .views import hora_sistema

urlpatterns = [
    path('hora_sistema', hora_sistema)
]