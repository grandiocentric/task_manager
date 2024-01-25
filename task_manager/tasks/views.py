from urllib.parse import parse_qs

from django.http import HttpResponse
from django.shortcuts import render

tasks = [
    dict(
        name="Task One",
        id=0,
    ),
    dict(
        name="Task Two",
        id=1,
    ),
    dict(
        name="Task Three",
        id=2,
    ),
]


def get_tasks(request):
    if request.headers.get("HX-Request"):
        name = request.POST["name"]
        new_task = {"name": name, "id": len(tasks) + 1}
        return render(
            request,
            "tasks/list_partial.html",
            {"tasks": tasks + [new_task]},
        )
    else:
        return render(request, "tasks/list.html", {"tasks": tasks})


def create_task(request):
    if request.method == "GET":
        return render(request, "tasks/create_partial.html")
    elif request.method == "POST":
        return get_tasks(request)


def update_task(request, task_id):
    if request.method == "PUT":
        values = parse_qs(request.body.decode("utf-8"))
        name = values["name"][0]
        return render(
            request,
            "tasks/task_partial.html",
            {"task": tasks[task_id] | {"name": name}},
        )
    elif request.method == "GET":
        return render(
            request,
            "tasks/update_partial.html",
            {"task": tasks[task_id]},
        )


def delete_task(request, task_id):
    return HttpResponse()
