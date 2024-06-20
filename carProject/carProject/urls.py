"""
URL configuration for carProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from carApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('product/<int:carId>/', views.carView, name='carView'),
    path('newProduct/create/', views.addCar, name='addCar'),
    path('product/edit/<int:carId>/', views.editCar, name='editCar'),
    path('product/delete/<int:carId>/', views.deleteCar, name='deleteCar'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
