from django.db import models

# Create your models here.


class Contact(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    class Meta:
        db_table = "contact"


class Customer(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.BigIntegerField()
    password = models.CharField(max_length=100)

    class Meta:
        db_table = "Customer"


class Owner(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.BigIntegerField()
    password = models.CharField(max_length=100)
    ground_type = models.CharField(max_length=200)
    ground_image = models.ImageField()
    timings = models.CharField(max_length=200)

    class Meta:
        db_table = "owner"
