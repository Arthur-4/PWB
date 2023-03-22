from django.urls import path
from formulario import views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('formulario/', views.form_formulario, name = 'formulario'), 
]