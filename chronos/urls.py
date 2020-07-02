from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tasks', views.task_list),
    path('tasks/title/<str:title>', views.task_list),
    path('tasks/state/<str:state>', views.task_list),
    path('tasks/<int:code>', views.task_detail),
]