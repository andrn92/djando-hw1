from django.urls import path
from .views import *

urlpatterns = [
    path('v1/sensor_list/', SensorList.as_view()),
    path('v1/sensor_list/<int:pk>/', SensorUpdate.as_view()),
    path('v1/add_measurement/', AddMeasurement.as_view()),
    path('v1/sensor_brief_info/', SensorBriefInfo.as_view()),

]
