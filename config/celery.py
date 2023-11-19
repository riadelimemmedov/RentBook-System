#!Celery modules and functions
from __future__ import absolute_import, unicode_literals
from celery import Celery


#!Python modules and functions
import os
from time import timezone
import time


#!RabbitMQ module
from kombu import Queue, Exchange


#!Register celery file to django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")


#!Create celery instance
app = Celery("config")
app.config_from_object("django.conf:settings", namespace="CELERY")


#!Python modules and functions
import logging


# ?Configuration rabbitmq
app.conf.task_queues = [
    Queue(
        "tasks",
        Exchange("tasks"),
        routing_key="tasks",
        queue_arguments={"x-max-priority": 10},
    ),
    Queue(
        "dead_letter", routing_key="dead_letter"
    ),  # This is common for all tasjs and other queues
]

app.conf.task_acks_late = True  # When you set task_acks_late to True, it means that tasks are acknowledged after they have been successfully executed by a worker. This behavior ensures that the task is not removed from the queue until the worker confirms that it has been processed correctly. If the task fails during execution, it remains in the queue for re-try.
app.conf.task_reject_on_worker_lost = True  # So here this configuration option salary determines the behavior of the worker when it is lost or disconnected from the message broker.So when task reject or worker lost is set to true, any unacknowledged tasks assigned to the lost worker,will be rejected and returned to the message broker for re queuing.And that way the task can then be reassigned to a different worker.
app.conf.task_default_priority = 5
app.conf.worker_prefetch_multiplier = 1  # Task count,# In Celery, tasks are processed by worker processes. The prefetch_multiplier setting determines how many tasks a worker should prefetch from the queue at once. This can help improve efficiency by reducing the overhead of constantly requesting new tasks,For example, let's say you have prefetch_multiplier set to 4 and worker_prefect_multiplier set to 2. This means that for every 4 tasks that a worker prefetches, two worker processes will be spawned to handle those tasks concurrently. The goal is to parallelize the processing of tasks and improve overall throughput.
app.conf.worker_concurrency = 1  # Worker count,#For instance, if you set worker_concurrency to 4, it means that Celery will create and manage 4 worker processes that work in parallel to process tasks. These processes will collectively process tasks from the queue, which can help improve the throughput of your application if your tasks are capable of running concurrently.


# ?Adjust task discovery
base_dir = os.getcwd()
task_folder = os.path.join(base_dir, "./", "tasks")

if os.path.exists(task_folder) and os.path.isdir(task_folder):
    task_modules = []
    for filename in os.listdir(task_folder):
        if filename.startswith("ex") and filename.endswith(".py"):
            module_name = f"tasks.{filename[:-3]}"
            module = __import__(module_name, fromlist=["*"])  # Dynamic import module
            for name in dir(module):
                obj = getattr(module, name)
                if callable(obj):
                    task_modules.append(f"{module_name}.{name}")

    #!Automatically discover and register tasks from  different app and modules in within you project
    app.autodiscover_tasks(task_modules)


#!Automatically discover and register tasks from  different app and modules in within you project
app.autodiscover_tasks()
