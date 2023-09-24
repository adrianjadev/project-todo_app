from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from todo_api.models import Todo

# import the pre-built django generic view
from django.views.generic.list import ListView


def index(request):
    return HttpResponse('Hello World! this is the APP index view')

# This will display all the task created with DRF


def TodoItemsView(request):
    todo_list = Todo.objects.all().order_by('-id')
    context = {
        'todo_list': todo_list,
    }
    return render(request, 'todos/index.html', context)


def TodoAdd(request):
    title = request.POST['title']
    description = request.POST['description']

    todo = Todo.objects.create(
        title=title,
        description=description
    )

    todo.save()

    return redirect('todo_app:todo-app-index')


def TodoDelete(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    todo.delete()

    return redirect('todo_app:todo-app-index')
