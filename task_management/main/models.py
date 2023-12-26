from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100, default=None)
    description = models.TextField()
    date_time_of_creation = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    due_date = models.DateField()
    project = models.CharField(max_length=50, null=True, blank=True)  
    priority = models.CharField(max_length=20, null=True, blank=True)
    completion_time = models.IntegerField(null=True, blank=True) 

    def __str__(self):
        return self.title


class Project(models.Model):
    name = models.CharField(max_length=50)
