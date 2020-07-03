from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tasks', views.task_list),
    path('tasks/<int:code>', views.task_detail),
    path('tasks/<int:code>/start', views.start_task),
    path('tasks/<int:code>/pause', views.start_task),
    path('tasks/<int:code>/stop', views.start_task)
]