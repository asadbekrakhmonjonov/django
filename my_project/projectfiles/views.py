from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm, TaskForm
from django.shortcuts import render, redirect
from .filter import TaskFilter
from django.contrib import messages
from .models import Task
from .decorators import unauthenticated_user, allowed_users
from django.contrib.auth.decorators import login_required

@unauthenticated_user
def signPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account is created for ' + user)
            # Use a named URL if available, replace 'home' with your actual home page name
            return redirect('login')

    context = {'regForm': form}
    return render(request, 'projectfiles/register.html', context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Correct the authenticate function call
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Wrong username or password')

    context = {}
    return render(request, 'projectfiles/login.html', context)
def logoutPage(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def taskPage(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            # Use a named URL if available, replace 'home' with your actual home page name
            return redirect('home')
    context = {'TaskForm': form}
    return render(request, 'projectfiles/taskPage.html', context)

@login_required(login_url='login')
@login_required(login_url='login')
def homePage(request):
    tasks = Task.objects.all()
    user_tasks = tasks.filter(user=request.user)
    myFilter = TaskFilter(request.GET, queryset=tasks)
    tasks = myFilter.qs
    context = {'tasks': tasks, 'myFilter': myFilter, 'user_tasks': user_tasks}
    return render(request, 'projectfiles/homePage.html', context)



@login_required(login_url='login')
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

@login_required(login_url='login')
def deleteTask(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('home')
    context = {'task': task}
    return render(request, 'projectfiles/deleteTask.html', context)
