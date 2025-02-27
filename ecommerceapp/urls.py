from django.urls import path
from ecommerceapp import views

urlpatterns = [
    path('', views.index, name="index"),
    path('contact', views.contact, name="contact"),
    path('myprofile', views.myprofile, name="myprofile"),
    path('checkout/', views.checkout, name="checkout"),
    path('payment/', views.payment, name="payment"),
    path('myprofile/', views.myprofile, name='myprofile'),

]