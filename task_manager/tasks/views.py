from datetime import datetime, timedelta
from urllib.parse import parse_qs

from django.http import HttpResponse
from django.shortcuts import render

tasks = [
    dict(
        date=datetime.now(),
        name="Task One",
        id=0,
    ),
    dict(
        date=datetime.now() - timedelta(days=1),
        name="Task Two",
        id=1,
    ),
    dict(
        date=datetime.now() - timedelta(days=3),
        name="Task Three",
        id=2,
    ),
]


def get_tasks(request):
    return render(request, "tasks/list.html", {"tasks": tasks})


def create_task(request):
    if request.method == "GET":
        return render(request, "tasks/create_partial.html")
    elif request.method == "POST":
        return render(request, "tasks/list_partial.html", {"tasks": tasks})


def update_task(request, task_id):
    if request.method == "PUT":
        values = parse_qs(request.body.decode("utf-8"))
        return render(request, "tasks/task_partial.html", {"task": tasks[task_id]})
    elif request.method == "GET":
        return render(request, "tasks/update_partial.html", {"task": tasks[task_id]})


def delete_task(request, task_id):
    return HttpResponse()
