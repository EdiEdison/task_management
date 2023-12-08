from django.db import models

# Models


class Task(models.Model):
    title = models.CharField(max_length=100, default=None)
    description = models.TextField()
    date_time_of_creation = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField()

    def __str__(self):
        return self.title
