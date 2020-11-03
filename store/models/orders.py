from django.db import models
from .product import Product
from .customer import Customer
import datetime

class Order(models.Model):
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=200, default='', blank=True)
    phone = models.CharField(max_length=50, default='')
    date = models.DateField(default=datetime.datetime.now())
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.product.name

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        # print(Order.objects.filter(customer=customer_id).order_by('price'))
        # print(Order.objects.filter(customer=customer_id))
        return Order.objects.filter(customer=customer_id).order_by('status')
