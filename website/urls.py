from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('addition.html',views.addition, name="addition"),
    path('subtraction.html',views.subtraction, name="subtraction"),
    path('multiplication.html',views.multiplication, name="multiplication"),
    path('division.html',views.division, name="division"),
]