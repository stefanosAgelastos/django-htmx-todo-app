from rest_framework import generics, permissions
from rest_framework.response import Response

from .models import Todo
from .serializers import TodoSerializer
from .permissions import IsOwnerOrNoAccess


class TodoList(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
