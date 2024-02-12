from django.db import models

# Create your models here.
class userRegistration(models.Model):
    email = models.CharField(max_length=200,null=True)
    password = models.CharField(max_length=200,null=True)
    address = models.CharField(max_length=200,null=True)
    city = models.CharField(max_length=200,null=True)
    state = models.CharField(max_length=200,null=True)
    zip = models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.email
