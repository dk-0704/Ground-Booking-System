from django.db import models
from groundapp.models import Customer
from groundapp.models import Owner
from ownerapp.models import Add_Ground

# Create your models here.


class Book_slot(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    ground = models.ForeignKey(Add_Ground, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    address = models.TextField()
    description = models.TextField(default=0)
    cost = models.BigIntegerField()
    hours = models.BigIntegerField(default=1)
    final_cost = models.BigIntegerField()
    status = models.IntegerField(default=0)