from datetime import datetime, timedelta

from django.http import HttpResponse
from django.shortcuts import render

tasks = [
    dict(
        date=datetime.now(),
        name="Task One",
        id=1,
    ),
    dict(
        date=datetime.now() - timedelta(days=1),
        name="Task Two",
        id=2,
    ),
    dict(
        date=datetime.now() - timedelta(days=3),
        name="Task Three",
        id=3,
    ),
]


def get_tasks(request):
    return render(request, "tasks/list.html", {"tasks": tasks})


def create_task(request):
    if request.method == "GET":
        return render(request, "tasks/create_partial.html")
    elif request.method == "POST":
        return render(request, "tasks/list_partial.html", {"tasks": tasks})


def delete_task(request, task_id):
    return HttpResponse()
