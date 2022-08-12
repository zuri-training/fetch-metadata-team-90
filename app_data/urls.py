from django.urls import path
from . import views
import django

def pageNotFound(request, *args, **kwargs):
    return django.views.defaults.page_not_found(request, None)

urlpatterns = [
    path('404', pageNotFound, name= '404'),
   	path('', views.HomePageView.as_view(), name='index'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    # path('contact/success', views.ContactSuccess.as_view(), name='contactsuccess'),
    path('privacy-policies/', views.PrivacyView.as_view(), name='privacy-policies'),
    path('terms-conditions/', views.TermsConditionView.as_view(), name='terms-conditions'),
    path('documentations/', views.DocumentationView.as_view(), name='documentations'),
    path('archives/', views.ArchiveView.as_view(), name='archives'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('save-page/', views.SavePageView.as_view(), name='save-page'),
    # path('dashboard/', views.CreateFilePuloadView.as_view(template_name='dashboard.html'), name='file_upload'),
    path('share/<int:pk>/', views.ShareFileUploadDetailView.as_view(), name='share'),
    path('details/<int:pk>/', views.FileUploadDetailView.as_view(), name='details'),
    path('search/', views.search, name='search')

]