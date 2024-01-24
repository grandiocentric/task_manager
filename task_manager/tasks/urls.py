from django.urls import path

from .views import create_task, delete_task, get_tasks, update_task

urlpatterns = [
    path("", get_tasks, name="tasks"),
    path("create/", create_task, name="create_task"),
    path("<int:task_id>/delete/", delete_task, name="delete_task"),
    path("<int:task_id>/update/", update_task, name="update_task"),
]
