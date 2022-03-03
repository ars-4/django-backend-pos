from django.urls import path
from sale import views

urlpatterns = [
    path("", views.getRoutes, name="Routes"),
    path("users/", views.getUsers, name="Users"),
    path("user/<str:pk>/products/", views.getProducts, name="Products"),
]