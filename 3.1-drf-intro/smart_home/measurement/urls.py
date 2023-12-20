from django.urls import path
from .views import *

urlpatterns = [
    path('v1/sensor-list/', SensorList.as_view()),
    path('v1/sensor-list/<int:pk>/', SensorUpdate.as_view()),
    path('v1/add-measurement/', AddMeasurement.as_view()),
    path('v1/sensor-brief-info/', SensorBriefInfo.as_view()),

]
