from django import template

register = template.Library()


@register.filter(name='is_in_cart')
def is_in_cart(product, cart):
    for id in cart.keys():
        if int(id) == product.id:
            return True
    return False

@register.filter(name='cart_quantity')
def cart_quantity(product, cart):
    for key in cart.keys():
        if product.id == int(key):
            return cart.get(key)
    return 0

@register.filter(name='price_total')
def price_total(product, cart):
    # print(cart_quantity(product, cart)
    return product.price * cart_quantity(product, cart)

@register.filter(name='total_cart_price')
def total_cart_price(products, cart):
    sum = 0
    for p in products:
        sum += price_total(p, cart)
    return sum

@register.filter(name='multiply')
def multiply(number, number1):
    return number * number1


