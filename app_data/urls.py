from django.urls import path
from . import views

urlpatterns = [
   	path('', views.HomePageView.as_view(), name='index'),
    path('contact/', views.Contact, name='contact'),
    path('contact/success', views.ContactSuccess.as_view(), name='contactsuccess'),

]