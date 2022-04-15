from unicodedata import name
from django.urls import path
from . import views
urlpatterns = [

    path('login/', views.loginpage, name="loginpage"),
    path('accounts/login/', views.loginpage, name="loginpage"),
    path('logout/', views.logoutuser,name="logoutuser"),
    path('register/', views.registerpage, name="registerpage"),

    path('', views.home, name="home"),
    path('user/', views.userPage, name="userpage"),
    path('products/', views.products, name='products'),
    path('customer/<int:num>', views.customer, name='customer'),

    path('create_order/<str:pk>', views.createOrder, name='create_order'),
    path('update_order/<str:pk>', views.updateOrder, name='update_order'),
    path('delete_order/<int:pk>', views.deleteOrder, name='delete_order'),
    
]