from django.db import models

# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length=200,null=True)
    age = models.CharField(max_length=10,null=True)
    phone = models.CharField(max_length=40,null=True)
    email = models.EmailField(max_length=200,null=True)
    def __str__(self):
        return self.name
class DailyGoal(models.Model):
    goal = models.CharField(max_length=200,null=True)
    attended_time = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.goal
