from django.shortcuts import render, redirect
from ..models.customer import Customer
from django.contrib.auth.hashers import make_password
from django.views import View


class Signup(View):
    def validateCustomer(self, customer):
        error_message = None
        if not customer.first_name:
            error_message = "First Name Required!!"
        elif not customer.last_name:
            error_message = "Last name required!!"
        elif not len(customer.phone) > 9:
            error_message = "Phone number must be 11 digits.!"
        elif not customer.email:
            error_message = "Email address required!"
        elif not customer.password:
            error_message = "Password Required!"
        elif customer.ifExists():
            error_message = "Email already registered."
        return error_message

    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        post_data = request.POST
        first_name = post_data.get('firstname')
        last_name = post_data.get('lastname')
        phone = post_data.get('phone')
        email = post_data.get('email')
        password = post_data.get('password')

        # validation
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }

        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password)

        error_message = self.validateCustomer(customer)

        # save customer
        if not error_message:
            customer.password = make_password(customer.password)
            customer.save()
            return redirect('index')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)
