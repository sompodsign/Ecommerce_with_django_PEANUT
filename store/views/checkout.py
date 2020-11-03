from django.views import View
from django.shortcuts import redirect
from ..models.product import Product
from ..models.orders import Order
from ..models.customer import Customer

class Checkout(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer_id')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        print(address, phone, customer, products, cart)

        for product in products:
            order = Order(customer= Customer(id=customer),
                          product = product,
                          price = product.price,
                          address = address,
                          phone = phone,
                          quantity = cart.get(str(product.id)))
            order.placeOrder()
            request.session['cart'] = {}
        return redirect('cart')