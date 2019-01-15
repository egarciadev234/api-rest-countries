from django.contrib import admin
from django.urls import path, include
from .views import *
urlpatterns = [
    path('countries', ListCountries.as_view(), name='list-countries'),
    path('countries/<int:pk>', DetailCountry.as_view(), name='detail-country'),
]
