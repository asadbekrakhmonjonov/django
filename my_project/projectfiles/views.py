from .forms import CreateUserForm, TaskForm
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import task
def signPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'you signed up')
            return redirect('/')
    context = {'regForm': form}
    return render(request, 'projectfiles/register.html', context)
def taskPage(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'taskForm': form}
    return render(request, 'projectfiles/taskPage.html', context)
def homePage(request):
    tasks = task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'projectfiles/homePage.html', context)
def updateTask(request, pk):
    chore = task.objects.get(id=pk)
    form = TaskForm(instance=chore)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=chore)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'projectfiles/taskPage.html', context)
