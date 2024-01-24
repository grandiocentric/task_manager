from datetime import datetime, timedelta

from django.shortcuts import render

tasks = [
    dict(
        date=datetime.now(),
        name="Task One",
    ),
    dict(
        date=datetime.now() - timedelta(days=1),
        name="Task Two",
    ),
    dict(
        date=datetime.now() - timedelta(days=3),
        name="Task Three",
    ),
]


def get_tasks(request):
    return render(request, "tasks/list.html", {"tasks": tasks})


def create_task(request):
    if request.method == "GET":
        return render(request, "tasks/create_partial.html")
    elif request.method == "POST":
        return render(request, "tasks/list_partial.html", {"tasks": tasks})
