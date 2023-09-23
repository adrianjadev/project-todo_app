from django.shortcuts import render
from django.http import HttpResponse

# Django rest framework
from rest_framework import generics

from .models import Todo
from .serializers import TodoSerializer


def home(request):
    return HttpResponse('Hello, world!')


class TodoView(generics.ListCreateAPIView):
    """ This view have the functionality to list or create a Task in API. """

    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):
    """ This view will get the specific task record based on their PK that was set to pull. """

    queryset = Todo.objects.all().order_by('date_created')
    serializer_class = TodoSerializer
