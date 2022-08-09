from re import template
from tokenize import Name
from unicodedata import name
from django.urls import path, include
from authy.views import UpdateProfileView, UserProfile
from django_registration.backends.activation.views import RegistrationView
from .forms import AuthyRegistrationForm
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('profile/edit/<str:pk>/', UpdateProfileView.as_view(template_name = 'edit_profile.html', success_url = '/accounts/profile/'), name='edit-profile'),
	path('accounts/profile/', UserProfile.as_view(template_name='profile.html'), name='profile'),
	path("accounts/register/", RegistrationView.as_view(form_class=AuthyRegistrationForm), name="django_registration_register"),
	path("accounts/", include("django_registration.backends.activation.urls")),
	path('accounts/', include('django.contrib.auth.urls')),
	path("accounts/", include("allauth.urls")),

]