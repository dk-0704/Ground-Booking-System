from django.db import models
from groundapp.models import Owner

# Create your models here.


class Add_Ground(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    ground_type = models.CharField(max_length=200)
    ground_images = models.ImageField()
    address = models.TextField()
    cost = models.BigIntegerField()
    timings = models.CharField(max_length=100)

    class Meta:
        db_table = "add_ground"
