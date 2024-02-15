from django.db import models

# Create your models here.
class Data(models.Model):
    name = models.CharField(max_length=200,null=True)
    username = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)


    def __str__(self):
        return self.username
class Tag(models.Model):
    name=models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.name
class userInfo(models.Model):
    goals = models.CharField(max_length=200,null=True)
    attended_time = models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.goals
class tasks(models.Model):
    STATUS = (
        ('Completed', 'Completed'),
        ('Incomplete', 'Incomplete'),
    )
    DAY =(
        ('Monday', 'Monday'),
        ('Tuesday','Tuesday'),
        ('Wednesday','Wednesday'),
        ('Thursday','Thursday'),
        ('Friday','Friday'),
        ('Saturday','Saturday'),
        ('Sunday','Sunday'),
    )
    task_name = models.CharField(max_length=200, null=True)
    status = models.CharField(max_length=200,null=True,choices=STATUS)
    doer = models.ForeignKey(Data, null=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField(Tag)



    def __str__(self):
        return self.task_name