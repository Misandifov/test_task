from django.urls import path

from test_task.views import webhook, run_process

urlpatterns = [
    path("webhook/", webhook, name="webhook"),
    path("run/", run_process, name="run_process"),
]
