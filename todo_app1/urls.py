from django.urls import path
from .views import index, TodoItemsView

app_name = 'todo_app'

urlpatterns = [
    path('', TodoItemsView, name='todo-app-index'),
]
