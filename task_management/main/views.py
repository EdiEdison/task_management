from django.shortcuts import render
from .models import Task
from .serializers import TaskSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .multi import Multi  

from django.http import Http404


class TaskListView(APIView):
    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetail(APIView):
    def get_object(self, pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        task = self.get_object(pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def put(self, request, pk):
        task = self.get_object(pk)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        task = self.get_object(pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Analytics(APIView):
    def get(self, request, **kwargs):
        analytics = Multi(Task.objects.values('task', 'completion_time'))
        period = request.data.get("period")
        result = analytics.drill_down(dimension='task')

        return Response({"result": result.to_dict()})


class Filters(APIView):
    def get(self, request, condition):
        analytics = Multi(Task.objects.values('task', 'completion_time'))
        result = analytics.slice_and_dice(conditions= self.condition)

        return Response({"result": result.to_dict()})


class Trends(APIView):
    def get(self, request, **kwargs):
        analytics = Multi(Task.objects.values('date_time_of_creation', 'completion_time'))
        result = analytics.trend_analysis(time_column='date_time_of_creation', measure_column='completion_time')

        return Response({"result": result.to_dict()})
