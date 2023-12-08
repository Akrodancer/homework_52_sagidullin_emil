from django.shortcuts import render, redirect, get_object_or_404
from to_do_list_app.models import ToDoList
from to_do_list_app.forms import ToDoListForm
from django.http import HttpResponseRedirect, Http404

# Create your views here.


def render_index (request):
    tasks = ToDoList.objects.all()
    return render(request, 'index.html', {'tasks': tasks})

def create(request, *args, **kwargs):
    if request.method == 'GET':
        form = ToDoListForm()
        return render(request, 'create.html', {'form': form})
    elif request.method == 'POST':
        form = ToDoListForm(data=request.POST)
        if form.is_valid():
            if form.cleaned_data['date'] == '':
                task = ToDoList.objects.create(
                    description=form.cleaned_data['description'],
                    status=form.cleaned_data['status'],
                    detailed_desc=form.cleaned_data['detailed_desc'],
                    date=None
                )
            else:
                task = ToDoList.objects.create(
                    description=form.cleaned_data['description'],
                    status=form.cleaned_data['status'],
                    detailed_desc=form.cleaned_data['detailed_desc'],
                    date=form.cleaned_data['date']
                )

            return redirect('detailed', pk=task.pk)
        else:
            return render(request, 'create.html', {'form': form})


def render_detailed(request, pk):
    task = ToDoList.objects.get(pk=pk)
    return render(request, 'detailed.html', {'task': task})


def update(request, pk):
    task = get_object_or_404(ToDoList, pk=pk)
    if request.method == 'GET':
        form = ToDoListForm(initial={
            'description': task.description,
            'date': task.date,
            'status': task.status,
            'detailed_desc': task.detailed_desc
        })
        return render(request, 'update.html', context={'task': task, 'form': form})
    elif request.method == 'POST':
        form = ToDoListForm(data=request.POST)
        if form.is_valid():
            if form.cleaned_data['date'] == '':
                task.description = form.cleaned_data['description']
                task.status = form.cleaned_data['status']
                task.detailed_desc = form.cleaned_data['detailed_desc']
                task.date = None
            else:
                task.description = form.cleaned_data['description']
                task.status = form.cleaned_data['status']
                task.detailed_desc = form.cleaned_data['detailed_desc']
                task.date = form.cleaned_data['date']

            task.save()
            return redirect('detailed', pk=task.pk)
        else:
            return render(request, 'update.html', context={'form': form, 'task': task})


def delete_view(request, pk):

    task = get_object_or_404(ToDoList, pk=pk)

    if request.method == 'GET':
        return render(request, 'delete.html', context={'task': task})
    elif request.method == 'POST':
        task.delete()
        return redirect('index')
