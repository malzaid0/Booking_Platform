from django.db import models


# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    phone = models.CharField(max_length=15)
    available_times = models.TimeField(choices=[])
    photo = models.ImageField()


class Customer(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    photo = models.ImageField(null=True, blank=True)


class Appointment(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    time = models.DateTimeField()
