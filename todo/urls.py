from django.urls import path, include
from . import views
# from .api import TodoList, TodoDetail

app_name = 'todo'

urlpatterns = [
    path('', views.index, name='index'),
    path('todo_list_partial', views.todo_list_partial, name='todo_list_partial'),
    path('todo_details_partial/<int:pk>',
         views.todo_details_partial, name='todo_details_partial'),
    path('create', views.create, name='create'),
    # path('api/v1', TodoList.as_view()),
    # path('api/v1/<int:pk>', TodoDetail.as_view()),
    # path('api/v1/rest-auth', include('rest_framework.urls')),
]
