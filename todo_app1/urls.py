from django.urls import path
from .views import index, TodoItemsView, TodoAdd, TodoDelete

app_name = 'todo_app'

urlpatterns = [
    path('', TodoItemsView, name='todo-app-index'),
    path('add/', TodoAdd, name='todo-add'),
    path('delete/<int:todo_id>/', TodoDelete, name='todo-delete'),

]
