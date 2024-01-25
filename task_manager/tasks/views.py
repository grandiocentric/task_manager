from urllib.parse import parse_qs

from django.http import HttpResponse
from django.shortcuts import render

from .models import Task


def get_tasks(request):
    tasks = Task.objects.all()
    is_partial = request.headers.get("HX-Request")
    template = "list_partial" if is_partial else "list"
    return render(request, f"tasks/{template}.html", {"tasks": tasks})


def create_task(request):
    if request.method == "GET":
        template = "create_partial"
        context = {}
    elif request.method == "POST":
        name = request.POST["name"]
        new_task = Task(name=name)
        new_task.save()

        template = "list_partial"
        tasks = Task.objects.all()
        context = {"tasks": tasks}

    return render(request, f"tasks/{template}.html", context)


def update_task(request, task_id):
    if request.method == "PUT":
        values = parse_qs(request.body.decode("utf-8"))
        new_name = values["name"][0]

        task = Task.objects.get(pk=task_id)
        task.name = new_name
        task.save()

        template = "task_partial"

    elif request.method == "GET":
        task = Task.objects.get(pk=task_id)

        template = "update_partial"

    return render(request, f"tasks/{template}.html", {"task": task})


def delete_task(request, task_id):
    Task.objects.get(pk=task_id).delete()
    return HttpResponse()
