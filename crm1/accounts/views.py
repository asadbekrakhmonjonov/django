from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def main(request):
    return render(request, 'accounts/main.html')
def product(request):
    return render(request, 'accounts/product.html')
def customer(request):
    return render(request, 'accounts/customer.html')

