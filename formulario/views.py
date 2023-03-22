from django.shortcuts import render
from django.http import HttpResponse
from formulario.forms import ClienteForm
from formulario.models import Cliente
from formulario.forms import MeuFormulario

def index(request):
    return HttpResponse("chuchubl")

def form_formulario(request):
    if request.method == "GET":
        form = ClienteForm()
        context = {
            'form':form
        }
        return render(request, "formulario/formulario2.html", context=context)
    else:
        form = ClienteForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form = ClienteForm()
            return HttpResponse("Obrigado! Seu formulário foi enviado com sucesso.")
        context = {
            'form':form
        }
        return render(request, "formulario/formulario2.html", context=context)


