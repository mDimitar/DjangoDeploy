"""
URL configuration for PrototipShop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import path
from PrototipShopApp import views
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.redirect_to_home, name='root'),
    path('admin/', admin.site.urls,name='login'),
    path('home/', views.home, name='home'),
    path('add_to_cart/<int:product_id>/', login_required(views.add_to_cart), name='add_to_cart'),
    path('remove_from_cart/<int:product_id>/', login_required(views.remove_from_cart), name='remove_from_cart'),
    path('cart/', login_required(views.view_cart), name='view_cart'),
    #path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('products/', views.view_all_products, name='view_all_products'),
    path('paymentdetails/', login_required(views.make_payment), name='make_payment'),
    path('paymentsuccess/', login_required(views.simulate_payment), name='simulate_payment'),
    path('logout/', views.logout_view, name='logout'),
]
