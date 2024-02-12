from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .models import *
from .forms import OrderForm
def main(request):
    order = Order.objects.all()
    customer1 = Customer.objects.all()
    total_customers = customer1.count()
    total_orders = order.count()
    delivered = order.filter(status='Delivered').count()
    pending = order.filter(status='Pending').count()
    context = {'order': order, 'customers': customer1, 'total_orders': total_orders, 'delivered': delivered, 'pending': pending}
    return render(request, 'accounts/main.html', context)
def product(request):
    product = Product.objects.all()
    return render(request, 'accounts/product.html', {'product': product})
def customer(request, pk_test):
    customer = Customer.objects.get(id=pk_test)
    orders = customer.order_set.all()
    order_count = orders.count()
    context = {'customer': customer, 'orders': orders, 'order_count': order_count}

    return render(request, 'accounts/customer.html', context)
def createOrder(request):
    form = OrderForm()
    if request.method == 'POST':
        #print("Printing POST",request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}

    return render(request, 'accounts/order_form.html', context)
def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        #print("Printing POST",request.POST)
        form = OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)
def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    context = {'item': order}

    return render(request,'accounts/delete.html', context)
