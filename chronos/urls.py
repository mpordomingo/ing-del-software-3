from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('chronos/', views.task_list),
    path('chronos/<int:pk>/', views.task_detail),
]