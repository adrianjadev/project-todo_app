from django.urls import path
from .views import index, TodoItemsView

app_name = 'todo_app'

urlpatterns = [
    path('todo', TodoItemsView, name='todo-app-index'),
]
