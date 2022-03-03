from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from sale.serializer import UserSerializer, ProductSerializer
from sale.models import User, Product

# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Main': 'Name',
        }
    ]
    return Response(routes)

@api_view(['GET'])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getProducts(request, pk):
    user = User.objects.get(id=pk)
    products = Product.objects.filter(user=user)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)
