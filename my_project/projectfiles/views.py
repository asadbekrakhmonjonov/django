from django.shortcuts import render
from django.http import HttpResponse
from . models import *
# Create your views here.
def home(request):
    user1 = UserInfo.objects.all()
    context = {'users': user1}
    return render(request, 'projectfiles/main.html', context)
def goals(request):
    goals = DailyGoal.objects.all()
    context = {'goals': goals}

    return render(request, 'projectfiles/goals.html', context)


