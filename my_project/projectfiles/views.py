from django.contrib.auth import authenticate, login
from .forms import CreateUserForm, TaskForm
from django.shortcuts import render, redirect
from .filter import TaskFilter
from django.contrib import messages
from .models import Task

def signPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account is created for', user)
            # Use a named URL if available, replace 'home' with your actual home page name
            return redirect('login')
    context = {'regForm': form}
    return render(request, 'projectfiles/register.html', context)

def loginPage(request):

    if request.method == 'POST':

        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:

            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Email or Password is incorrect')
    context = {}
    return render(request, 'projectfiles/login.html', context)

def taskPage(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            # Use a named URL if available, replace 'home' with your actual home page name
            return redirect('/')
    context = {'TaskForm': form}
    return render(request, 'projectfiles/taskPage.html', context)

def homePage(request):
    task = Task.objects.all()
    myFilter = TaskFilter(request.GET, queryset=task)
    task = myFilter.qs
    context = {'task': task, 'myFilter': myFilter}
    return render(request, 'projectfiles/homePage.html', context)

def updateTask(request, pk_test):
    task = Task.objects.get(id=pk_test)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            # Use a named URL if available, replace 'home' with your actual home page name
            return redirect('home')

    context = {'TaskForm': form}
    return render(request, 'projectfiles/taskPage.html', context)

def deleteTask(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('home')
    context = {'task': task}
    return render(request, 'projectfiles/deleteTask.html', context)
