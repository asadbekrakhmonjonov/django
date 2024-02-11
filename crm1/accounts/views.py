from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import *
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

