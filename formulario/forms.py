from django import forms
from formulario.models import Cliente

SERIES_CHOICES = [
    ["F", "Ensino Fundamental"],
    ["M", "Ensino Médio"]
]

ddd_valido = ("11", "12", "13", "14", "15", "16", "17", "18", "19", "21"
"22", "24", "27", "28", "31", "32", "33", "34", "35", "37", "38", "41",
"42", "43", "44", "45", "46", "47", "48", "49", "51", "53", "54", "55",
"61", "62", "63", "64", "65", "66", "67", "68", "69", "71", "73", "74",
"75", "77", "79", "81", "82", "83", "84", "85", "86", "87", "88", "89",
"91", "92", "93", "94", "95", "96", "97", "98", "99")

def validar_ddd(ddd):
  if ddd[0:2] not in ddd_valido:
    raise forms.ValidationError("O DDD enviado é inválido")

class ClienteForm(forms.Form):
    Nome = forms.CharField(max_length=35)
    Data_de_nascimento = forms.DateField(error_messages={'invalid': "Essa data não é válida!"})
    Nome_da_mae = forms.CharField(max_length=35)
    Nome_do_pai = forms.CharField(max_length=35)
    telefone = forms.CharField(label= "Telefone (DDD seguido de numero)", validators = [validar_ddd], max_length=11)
    Email = forms.EmailField(max_length=50,error_messages={'invalid': "O Email informado não é válido!"})
    Serie = forms.ChoiceField(choices = SERIES_CHOICES)

class MeuFormulario(forms.Form):
    Nome = forms.CharField(max_length=35)
    Data_de_nascimento = forms.DateField()
    Nome_da_mae = forms.CharField(max_length=35)
    Nome_do_pai = forms.CharField(max_length=35)
    telefone = forms.CharField(initial= "Telefone (DDD seguido de numero)", max_length=11)
    Email = forms.EmailField(max_length=50)
    Serie = forms.ChoiceField(choices = SERIES_CHOICES)