from django.views import View
from django.shortcuts import render, HttpResponse
from ..models.orders import Order
from store.middlewares.auth import auth_middleware
from django.utils.decorators import method_decorator

class OrderView(View):
    def get(self, request):
        customer = request.session.get('customer_id')
        orders = Order.get_orders_by_customer(customer)
        return render(request, 'orders.html', {'orders': orders})
