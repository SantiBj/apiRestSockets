from django.db import models

# Create your models here.
class Customer(models.Model):

    name = models.CharField(max_length=100)
    numberPhone = models.IntegerField()

    class Meta:
        db_table = "customer"
        verbose_name = "customer"
        verbose_name_plural = "customers"
