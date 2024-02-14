from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import registerForm


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



