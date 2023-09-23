from django.urls import path, include
from .views import home, TodoView, TodoDetailView

app_name = 'todo_api'

urlpatterns = [
    path('home', home, name='name'),
    path('todo', TodoView.as_view(), name='todo-index'),
    path('todo/<int:pk>', TodoDetailView.as_view(), name='todo-detail'),
]
