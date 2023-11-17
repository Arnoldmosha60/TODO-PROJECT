from django.shortcuts import render
from .models import Todo
from .serializers import TodoSerializer
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.
# class TodoView(viewsets.ModelViewSet):
#     serializer_class = TodoSerializer
#     queryset = Todo.objects.filter("completed").all()

class TodoDeatail(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    # def highlight(self, request, *args, **kwargs):
    #     todo = self.get_object()
    #     return Response(todo.highlighted)

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)
