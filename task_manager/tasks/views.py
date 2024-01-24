from datetime import datetime, timedelta

from django.shortcuts import render


def get_tasks(request):
    tasks = [
        dict(
            date=datetime.now(),
            name="Task One",
            priority=1,
        ),
        dict(
            date=datetime.now() - timedelta(days=1),
            name="Task Two",
            priority=3,
        ),
        dict(
            date=datetime.now() - timedelta(days=3),
            name="Task Three",
            priority=2,
        ),
    ]
    return render(request, "tasks/list.html", {"tasks": tasks})
