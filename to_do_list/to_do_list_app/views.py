from django.shortcuts import render, redirect
from to_do_list_app.models import ToDoList
from django.http import HttpResponseRedirect

# Create your views here.


def render_index (request):
    tasks = ToDoList.objects.all()
    return render(request, 'index.html', {'tasks': tasks})

def create(request, *args, **kwargs):
    status_choices = [('new', 'Новая'), ('in_progress', 'В процессе'), ('done', 'Сделано')]
    if request.method == 'GET':
        return render(request, 'create.html', {'status_choice': status_choices})
    elif request.method == 'POST':
        if request.POST.get('date') == '':
            task = ToDoList.objects.create(
                description=request.POST.get('description'),
                status=request.POST.get('status'),
                date=None
            )
        else:
            task = ToDoList.objects.create(
                description=request.POST.get('description'),
                status=request.POST.get('status'),
                date=request.POST.get('date')
            )

        return redirect('detailed', pk=task.pk)


def render_detailed(request, pk):
    task = ToDoList.objects.get(pk=pk)
    return render(request, 'detailed.html', {'task': task})