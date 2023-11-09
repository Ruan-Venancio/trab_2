from django.shortcuts import render
from models import Pessoa
# Create your views here.

tasks = [1,2,3,4]

def index(request):

    name = request.POST.get('name')

    pessoa = Pessoa(name=name)
    pessoa.save()

    pessoas = Pessoa.objects.all()

    return render(request, 'task/index.html', {
        "tasks":tasks,
        "name":name

    })
