from django.contrib import admin
from sale.models import User, Product

# Register your models here.

RegisteredModels = [
    User,
    Product,
]

admin.site.register(RegisteredModels)