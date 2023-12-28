from django.shortcuts import render
from .models import Task
from .serializers import TaskSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .multi import Multi  
from django.utils import timezone
from django.conf import settings
import os
import pandas as pd

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
            if serializer.validated_data.get('completed'):
                # If the task is marked as completed, calculate task_time and set completion_time
                completion_time = timezone.now()
                task.completion_time = completion_time

                # Calculate the number of hours spent on the task
                time_spent_seconds = (completion_time - task.date_time_of_creation).total_seconds()
                task.task_time = time_spent_seconds / 3600  # Convert seconds to hours

            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        task = self.get_object(pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class Data:
    def read():
        csv_file_path = os.path.join(settings.BASE_DIR, 'warehouse/tasks.csv')
        data = pd.read_csv(csv_file_path)
        return data
class Analytics(APIView):
    def get(self, request, **kwargs):
        period = request.query_params.get('period', 'monthly')
        if period == "monthly":
            data = Data.read()
            data["task_time"] = data["task_time" == 30]
        elif period == 'daily':
            data = Data.read()
            data["task_time"] = data["task_time" <= 24]
        elif period == 'yearly':
            data = Data.read()
            data["task_time"] = data["task_time" >= 870]
        else:
            return Response({"error": "Invalid period specified."}, status=400)

        multi_analytics = Multi()

        result = multi_analytics.drill_down(data["task_time"])

        return Response({"result": result.to_dict()})


class Filters(APIView):
    def get(self, request):
        data = Data.read()

        filter_condition = request.query_params.get('filter')

        if filter_condition is not None:
            analytics = Multi(data.dropna())
            
            try:
                result = analytics.slice_and_dice(conditions=filter_condition)
                return Response({"result": result.to_dict()})
            except Exception as e:
                return Response({"error": f"Error in filtering: {str(e)}"}, status=400)
        else:
            return Response({"error": "Missing 'filter' query parameter"}, status=400)
class Trends(APIView):
    def get(self, request, **kwargs):
        data = Data.read()
        analytics = Multi(data[['date_time_of_creation', 'task_time']].dropna())
        result = analytics.trend_analysis(time_column='date_time_of_creation', measure_column='task_time')

        return Response({"result": result.to_dict()})
