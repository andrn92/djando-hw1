from django.urls import path
from .views import index, show_catalog, show_product


urlpatterns = [
    path('', index),
    path('catalog/', show_catalog, name='catalog'),
    path('catalog/<int:phone_id>/', show_product, name='phone'),
]