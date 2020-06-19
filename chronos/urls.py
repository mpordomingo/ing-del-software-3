from django.urls import path

from . import views

urlpatterns = [
    path('chronos/', views.task_list),
    path('chronos/<int:pk>/', views.task_detail),
]