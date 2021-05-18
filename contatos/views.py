from django.shortcuts import render
from .models import Contato

# Create your views here.
def contatos_list_view(request):
    contatos = Contato.objects.all()
    return render(request, 'contatos/contatos_list.html', {'contatos':contatos})
