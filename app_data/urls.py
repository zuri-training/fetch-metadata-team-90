from django.urls import path
from . import views

urlpatterns = [
   	path('', views.HomePageView.as_view(), name='index'),
    path('contact/', views.Contact, name='contact'),
    path('contact/success', views.ContactSuccess.as_view(), name='contactsuccess'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    # path('dashboard/', views.CreateFilePuloadView.as_view(template_name='dashboard.html'), name='file_upload'),
    path('share/<int:pk>/', views.ShareFileUploadDetailView.as_view(), name='share'),
    path('details/<int:pk>/', views.FileUploadDetailView.as_view(), name='details')

]