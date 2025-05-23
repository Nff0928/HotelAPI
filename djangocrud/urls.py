"""djangocrud URL Configuration

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
from tasks import views

urlpatterns = [
    path('', views.hotel_view, name='hotel'),
     path('', views.home, name='home'),
    path('check_in', views.check_in, name='Check_in'),
    path('check_out', views.check_out, name='check_Out'),
    path('tarjetaRegistro', views.tarjetaRegistro, name='tarjetaRegistro'),    
    path('admin/', admin.site.urls),
    path('contacto', views.contacto, name='contacto'),
    path('reserva', views.reserva_form, name='reserva'),
    path('reservar/', views.hacer_reserva, name='reservar'),
    path('checkin/', views.validar_checkin, name='checkin'),
    path('estandar/', views.estandar, name='estandar'),
    path('deluxe/', views.deluxe, name='deluxe'),
    path('suite/', views.suite, name='suite'),
    path('tarjetaRegistro/<int:id>/', views.tarjeta_registro, name='tarjeta_registro'),
    path('mi_reserva/',views.mi_reserva, name='mi_reserva'),
    
    
     
    

    
]
