from django.db import models

# class Priority(models.TextChoices):
#     HIGH = "high", "HIGH"
#     MEDIUM = "medium","MEDIUM"
#     LOW = "low", "LOW"
class Task(models.Model):
    title = models.CharField(max_length=100, default=None)
    description = models.TextField()
    date_time_of_creation = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    due_date = models.DateField()
    completion_time = models.DateTimeField(default=None, null=True, blank=True) 

    def __str__(self):
        return self.title
