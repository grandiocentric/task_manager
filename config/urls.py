from django.urls import include, path

urlpatterns = [
    path("tasks/", include("task_manager.tasks.urls")),
]
