from crm1.accounts.models import Customer, Order, Product

customer = Customer.objects.all()
firstCustomer = Customer.objects.first()
lastCustomer = Customer.objects.last()
customerByName = Customer.objects.get(name='Stephan')
customerById = Customer.objects.get(id=4)
firstCustomer.order_set.all()
order = Order.objects.first()
parentName = order.customer.name
product = Product.objects.filter(category='Outdoor')
leastToGreatest = Product.objects.all().order_by('id')
greatestToLeast = Product.objects.all().order_by('-id')
productFiltered = Product.objects.filter(tags_name='Sports')
ballOrders = firstCustomer.order_set.filter(product_name='ball').count()
allOrders = {}
for order in firstCustomer.order_set.all():
    if order.product.name in allOrders:
        allOrders[order.product.name] += 1
    else:
        allOrders[order.product.name] = 1
class ParentModel(models.Model):
    name = models.CharField(max_length=200, null=True)
class ChildModel(models.Model):
    parent = models.ForeignKey(ParentModel)
    name = models.CharField(max_length=200, null=True)
parent = ParentModel.objects.first()
parent.childmodel_set.all()