from django.urls import path
from . import views

urlpatterns = [
   	path('', views.HomePageView.as_view(), name='index'),
    path('contact/', views.Contact, name='contact'),
    path('contact/success', views.ContactSuccess.as_view(), name='contactsuccess'),
    path('dashboard/', views.DashboardView.as_view(template_name='dashboard.html'), name='dashboard'),
    path('details/<int:pk>/', views.FileUploadDetailView.as_view(), name='details')

]