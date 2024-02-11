from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'projectfiles/main.html')
def goals(request):
    return render(request, 'projectfiles/goals.html')
def accomplishments(request):
    return render(request, 'projectfiles/accomplishments.html')

