from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import registerForm
from .create import taskForm
from .filter import TaskFilter


# Create your views here.
def home(request):
    form = registerForm()
    if request.method == 'POST':
        form = registerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'projectfiles/main.html', context)

def userInfo(request):
    users = Data.objects.all()

    context = {'users': users}
    return render(request, 'projectfiles/user_info.html',context)
def taskInfo(request):
    form = taskForm()
    if request.method == 'POST':
        form = taskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'projectfiles/tasks.html', context)
def taskList(request):
    user_task = tasks.objects.all()
    myFilter = TaskFilter(request.GET, queryset=user_task)
    user_task = myFilter.qs
    context = {'user_task': user_task, 'myFilter': myFilter}

    return render(request, 'projectfiles/task_list.html',context)


