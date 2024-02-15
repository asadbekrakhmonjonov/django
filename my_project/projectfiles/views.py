from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import registerForm
from .create import taskForm


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

def userInfo(request,pk):
    users = Data.objects.all()
    user_id = users.get(id=pk)

    context = {'users': users, 'user_id': user_id}
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
    context = {'user_task': user_task}

    return render(request, 'projectfiles/task_list.html',context)


