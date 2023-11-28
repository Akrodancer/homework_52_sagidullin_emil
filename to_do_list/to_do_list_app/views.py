from django.shortcuts import render
from to_do_list_app.models import ToDoList
from django.http import HttpResponseRedirect

# Create your views here.


def render_main_menu(request):
    return render(request, 'main_menu.html')

def render_index (request):
    tasks = ToDoList.objects.all()
    return render(request, 'index.html', {'tasks': tasks})

def create(request):
    status_choices = [('new', 'Новая'), ('in_progress', 'В процессе'), ('done', 'Сделано')]
    if request.method == 'GET':
        return render(request, 'create.html', {'status_choice': status_choices})
    elif request.method == 'POST':
        ToDoList.objects.create(
            description=request.POST.get('description'),
            status=request.POST.get('status'),
            date=request.POST.get('date')
        )

        return HttpResponseRedirect('/')
