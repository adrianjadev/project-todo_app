from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from todo_api.models import Todo

# import the pre-built django generic view
from django.views.generic.list import ListView


def index(request):
    return HttpResponse('Hello World! this is the APP index view')


# class TodoItemsView(ListView):
#     """ This view is using the pre-built django generic Detail View. """

#     queryset = Todo.objects.all()
#     template_name = 'todos/index.html'
#     paginate_by = 5

def TodoItemsView(request):
    todo_list = Todo.objects.all().order_by('-id')
    context = {
        'todo_list': todo_list,
    }

    return render(request, 'todos/index.html', context)
