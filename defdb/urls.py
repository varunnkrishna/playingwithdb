from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('customersearch/', views.customersearch, name='customersearch'),
    path('customerinput/', views.customerinput, name='customerinput'),
]
