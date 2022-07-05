from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("collection/new/", views.add_collection, name="add-collection"),
    path("task/new/", views.add_task, name="add-task"),
    path("delete-task/<int:task_pk>", views.delete_task, name="delete-task"),
    path("delete-collection/<int:collection_pk>", views.delete_collection, name="delete-collection"),
    path("get-tasks/<int:collection_pk>/", views.get_tasks, name="get-tasks"),
]
