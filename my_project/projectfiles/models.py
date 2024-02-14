from django.db import models

# Create your models here.
class Data(models.Model):
    name = models.CharField(max_length=200,null=True)
    username = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.username
class userInfo(models.Model):
    goals = models.CharField(max_length=200,null=True)
    attended_time = models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.goals