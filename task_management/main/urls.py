from django.urls import path
from .views import *

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("task/<int:pk>/", TaskDetail.as_view(), name="task-detail"),
    path("analytics/<str:period>/", Analytics.as_view(), name="analytics"),
    path("filters/<str:filter>/", Filters.as_view(), name="filters"),
    path("trends/", Trends.as_view(), name="trends")
]
