from django.urls import path

from .views import create_task, get_tasks

urlpatterns = [
    path("", get_tasks, name="tasks"),
    path("create/", create_task, name="create_task"),
]
