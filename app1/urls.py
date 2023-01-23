from django.urls import path
from . import views

app_name = 'app1'

urlpatterns = [
    path('cars/',views.viewCars,name='viewCars'),
    path('createcar',views.createCar,name='createcar'),
    path('showcar/<id>',views.showCar,name='showwithid'),
    path('deletecar/<id>',views.deleteCar,name='deletewithid'),
    path('updatecar/<id>',views.updateCar,name='updatewithid'),

]