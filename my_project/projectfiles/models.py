from django.db import models
from django.contrib.auth import get_user_model



class Task(models.Model):
    STATUS = (
        ('Completed', 'Completed'),
        ('Incomplete', 'Incomplete'),
    )
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)
    task_name = models.CharField(max_length=200, null=True)
    task_status = models.CharField(max_length=200, choices=STATUS, null=True)
    due_date = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.task_name


