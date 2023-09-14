from django.http import HttpResponse
from django.urls import path, include
from .views import books_view, moving_date_published


urlpatterns = [
    path('', books_view, name='books'),
    path('<str:date_published>/', moving_date_published, name='date_published'),
]

