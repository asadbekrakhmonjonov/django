from django.contrib import admin
from . models import UserData
from . models import DailyGoals
from . models import DailyAccomplishments

# Register your models here.
admin.site.register(UserData)
admin.site.register(DailyGoals)
admin.site.register(DailyAccomplishments)