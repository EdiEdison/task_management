from django.urls import path
from .views import TaskListView, TaskDetail

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("task/<int:pk>/", TaskDetail.as_view()),
]
