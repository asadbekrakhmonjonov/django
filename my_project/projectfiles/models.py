from django.db import models

class task(models.Model):
    STATUS = (
        ('Completed', 'Completed'),
        ('Incomplete', 'Incomplete')
    )
    task_name = models.CharField(max_length=200, null=True)
    task_status = models.CharField(max_length=200,choices=STATUS, null=True)
    due_date = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.task_name


