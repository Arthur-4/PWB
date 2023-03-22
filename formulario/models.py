from django.db import models
from django import forms 
from django.core import validators

series_choices = [
    ["F", "Ensino Fundamental"],
    ["M", "Ensino Médio"]
]


class Cliente(models.Model):
    def validate_email_address(email_address):
        return re.search(r"^[A-Za-z0-9_!#$%&'*+\/=?`{|}~^.-]+@[A-Za-z0-9.-]+$", email_address)
    Nome = models.CharField(max_length=35)
    Data_de_nascimento = models.DateField(blank=True, null=True)
    Nome_da_mae = models.CharField(max_length=35)
    Nome_do_pai = models.CharField(max_length=35)
    telefone = models.CharField(verbose_name = "Telefone (DDD seguido de numero)", max_length=11)
    Email = models.EmailField(max_length=50)
    Serie = models.CharField(max_length=1, choices = series_choices)


    def __str__(self):
        return self.nome

