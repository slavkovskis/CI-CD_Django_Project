from django.shortcuts import render, redirect

from .models import Car
from .forms import CarForm


def index(request):
    cars = Car.objects.all()

    return render(request, "index.html", {"cars": cars})


def carView(request, carId):
    car = Car.objects.get(id=carId)

    return render(request, "car_detail.html", {"car": car})


def addCar(request):
    if request.method == "POST":
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = CarForm()

    return render(request, "form_add.html", {"form": form})


def editCar(request, carId):
    car = Car.objects.get(id=carId)
    if request.method == "POST":
        form = CarForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = CarForm(instance=car)

    return render(request, "form_edit.html", {"form": form})


def deleteCar(request, carId):
    car = Car.objects.get(id=carId)
    car.delete()
    return redirect("index")
