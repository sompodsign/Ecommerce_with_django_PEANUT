from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=500)

    def __str__(self):
        name = f"{self.first_name} {self.last_name}"
        return name

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            False

    def ifExists(self):
        if Customer.objects.filter(email = self.email):
            return True

        return False
