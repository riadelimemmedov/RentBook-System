from celery import shared_task


@shared_task(queue="tasks")
def task_one():
    return "Task One"


@shared_task(queue="tasks")
def hello_one():
    return "Hello"
