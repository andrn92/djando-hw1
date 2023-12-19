from django.urls import path
from .views import *

urlpatterns = [
    path('v1/sensorlist/', SensorAPIList.as_view()),
    path('v1/sensorlist/<int:pk>/', SensorAPIUpdate.as_view()),
    path('v1/add_measurement/', AddMeasurement.as_view()),
]
