from django.views import View
from django.shortcuts import render
from ..models.product import Product



class Cart(View):
    def get(self, request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)

        return render(request, 'cart.html', {'products': products})
    def post(self, request):
        pass