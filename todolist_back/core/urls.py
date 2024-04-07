from django.contrib import admin
from django.urls import path
from .views import get,save

urlpatterns = [
    path('',get),
    path('salvar/',save)

]
    