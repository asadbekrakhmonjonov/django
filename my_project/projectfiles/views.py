from .forms import CreateUserForm
from django.shortcuts import render, redirect
from django.contrib import messages
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
