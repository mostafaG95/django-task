from django.shortcuts import render, redirect
from .models import Car
from .forms import CarForm
def viewCars(request) :
    car_dict={'cars': Car.objects.all()}
    print(Car.objects.all().order_by('model'))
    return render(request,'app1/index.html',car_dict)

def createCar(request) :
    car = CarForm(request.POST,request.FILES)
    if car.is_valid():
        car.save()
    return render(request,'app1/createcar.html',{"form":CarForm})

   
def showCar(request,id) :
    car=Car.objects.get(pk=id)
    return render(request,'app1/showcar.html',{'car':car})

def deleteCar(request,id) :
    car=Car.objects.get(pk=id)
    car.delete()

    car_dict={'cars': Car.objects.all()}
    print(Car.objects.all().order_by('model'))
    return render(request,'app1/index.html',car_dict)

# def updateCar(request,id) :
#     car = CarForm(request.POST,request.FILES)
#     car_data=Car.objects.get(pk=id)
#     if car.is_valid():
#         car.save()
#     return render(request,'app1/updatecar.html',{"data":[CarForm,car_data]})

def updateCar(request, id):
    car = Car.objects.get(pk=id)
    if request.method == 'POST':
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            car_dict={'cars': Car.objects.all()}
            return render(request,'app1/index.html',car_dict)
    else:
        form = CarForm(instance=car)
    return render(request, 'app1/updatecar.html', {'form': form})
