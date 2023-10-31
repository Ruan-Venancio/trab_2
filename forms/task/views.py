from django.shortcuts import render

# Create your views here.

tasks = [1,2,3,4]

def index(request):

    name = request.POST.get('name')

    return render(request, 'task/index.html', {
        "tasks":tasks,
        "name":name


    })
