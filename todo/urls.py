from django.urls import path, include
from . import views
# from .api import TodoList, TodoDetail

app_name = 'todo'

urlpatterns = [
    path('', views.index, name='index'),
    # path('api/v1', TodoList.as_view()),
    # path('api/v1/<int:pk>', TodoDetail.as_view()),
    # path('api/v1/rest-auth', include('rest_framework.urls')),
]
