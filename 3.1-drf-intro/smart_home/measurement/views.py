from rest_framework import generics, views, response
from django.forms import model_to_dict
from .models import Measurement, Sensor
from .serializers import SensorSerializer, MeasurementSerializer


class SensorAPIList(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class AddMeasurement(views.APIView):
    def get(self, request):
        measurements = Measurement.objects.all().values()
        return response.Response({'measurements': list(measurements)})
    
    def post(self, request):
        measurements = Measurement.objects.create(temperature = request.data['temperature'], sensor_id = request.data['sensor'])
        return response.Response({'measurements': model_to_dict(measurements)})


