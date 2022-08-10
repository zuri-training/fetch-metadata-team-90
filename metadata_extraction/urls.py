from django.urls import path
from .views import home, test

urlpatterns = [
    path('', test),
    path('home', home)
]