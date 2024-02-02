from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    path('', views.TaskList.as_view(), name='taskList'),
    path('task/<int:pk>/', views.TaskDetail.as_view(), name='taskDetail'),
    path('task-create/', views.TaskCreate.as_view(), name='taskCreate'),
    path('task-update/<int:pk>/', views.TaskUpdate.as_view(), name='taskUpdate'),
    path('task-delete/<int:pk>/', views.TaskDelete.as_view(), name='taskDelete'),
]
