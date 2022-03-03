from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    bill = models.IntegerField(null=True, blank=True)
    joining = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name


class Product(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='products')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField(null=True, blank=True)
    def __int__(self):
        return self.id