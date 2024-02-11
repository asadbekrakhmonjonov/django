from django.db import models

# Create your models here.
class UserData(models.Model):
    name = models.CharField(max_length=200,null=True)
    age = models.IntegerField(max_length=10,null=True)
    phone = models.CharField(max_length=40,null=True)
    email = models.EmailField(max_length=200,null=True)
    def __str__(self):
        return self.name
class DailyGoals(models.Model):
    goal = models.CharField(max_length=200,null=True)
    date = models.DateField(auto_now=True)
    def __str__(self):
        return self.goal
class DailyAccomplishments(models.Model):
    accomplishment = models.CharField(max_length=200,null=True)
    date = models.DateField(auto_now=True)
    def __str__(self):
        return self.accomplishment
