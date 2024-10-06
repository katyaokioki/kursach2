"""
URL configuration for project_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tasks.views import project_list, add_project, edit_project, delete_project, project_detail, task_comments
# from .views import project_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', project_list, name='project_list'),
    path('add/', add_project, name='add_project'),
    path('edit/<int:pk>/', edit_project, name='edit_project'),
    path('delete/<int:pk>/', delete_project, name='delete_project'),
    path('project/<int:pk>/', project_detail, name='project_detail'),
    path('task/<int:task_id>/comments/', task_comments, name='task_comments'),
]