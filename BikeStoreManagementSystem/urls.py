"""BikeStoreManagementSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from bikeshop import views

urlpatterns = [
    path('', views.dashboard, name = 'dashboard'),
    path('customers/', views.customers, name='customers'),
    path('staff/', views.staff, name='staff'),
    path('stores/', views.stores, name='stores'),
    path('products/', views.products, name='products'),
    path('stocks/', views.stocks, name='stocks'),
    path('orders/', views.orders, name='orders'),
    path('login_view/', views.login_view, name='login_view'),
    path('logout_view/',views.logout_view,name='logout_view'),
    path('registration/', views.registration, name='registration'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('contact/', views.contact, name='contact'),
    path('add_product/', views.add_product, name='add_product'),
    path('edit_product/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('add_customer/', views.add_customer, name='add_customer'),
    path('edit_customer/<int:customer_id>/', views.edit_customer, name='edit_customer'),
    path('delete_customer/<str:customer_ids>/', views.delete_customer, name='delete_customer'),
    path('edit_staff/<int:staff_id>/', views.edit_staff, name='edit_staff'),
    path('delete_staff/<int:staff_id>/', views.delete_staff, name='delete_staff'),
    path('add_store/', views.add_store, name='add_store'),
    path('edit_store/<int:store_id>/', views.edit_store, name='edit_store'),
    path('delete_store/<int:store_id>/', views.delete_store, name='delete_store'),
    path('add_stock/', views.add_stock, name='add_stock'),
    path('edit_stock/<int:stock_id>', views.edit_stock, name='edit_stock'),
    path('add_order/', views.add_order, name='add_order'),
    path('edit_order/<int:order_id>/', views.edit_order, name='edit_order'),
    path('delete_order/<str:order_ids>/', views.delete_order, name='delete_order'),
]
