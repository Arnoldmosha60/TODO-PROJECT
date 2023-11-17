from rest_framework.routers import DefaultRouter
from .views import TodoDeatail
from django.shortcuts import render
from django.urls import path, include

# todo_list = TodoDeatail.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# todo_detail = TodoDeatail.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
# todo_highlight = TodoDeatail.as_view({
#     'get': 'highlight'
# }, 
# renderer_classes=[renderers.StaticHTMLRenderer])



router = DefaultRouter()
router.register(r'todos', TodoDeatail, basename='todo')

urlpatterns = [
    path('api/', include(router.urls)),
]