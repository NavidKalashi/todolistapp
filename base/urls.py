from django.urls import path

from . import views

urlpatterns = [
    path('', views.TaskList.as_view(), name='taskList'),
    path('task/<int:pk>/', views.TaskDetail.as_view(), name='taskDetail'),
    path('task-create/', views.TaskCreate.as_view(), name='taskCreate'),
    path('task-update/<int:pk>/', views.TaskUpdate.as_view(), name='taskUpdate'),
    path('task-delete/<int:pk>/', views.TaskDelete.as_view(), name='taskDelete'),
]
