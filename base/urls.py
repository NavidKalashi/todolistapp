from django.urls import path

from . import views

urlpatterns = [
    path('', views.TaskList.as_view(), name='taskList'),
    path('task/<int:pk>/', views.TaskDetail.as_view(), name='taskDetail'),
]
