from re import template
from tokenize import Name
from unicodedata import name
from django.urls import path, include
from authy.views import UserProfile, EditProfile
from django_registration.backends.activation.views import RegistrationView
from .forms import AuthyRegistrationForm
from django.contrib.auth import views as auth_views


urlpatterns = [
   	
    path('profile/edit', EditProfile, name='edit-profile'),
	path('accounts/profile/', UserProfile, name='profile'),
	path("accounts/signup/", RegistrationView.as_view(form_class=AuthyRegistrationForm), name="signup"),
	# path("accounts/password/reset/", auth_views.PasswordResetView.as_view(), name='password_reset'),
	path('accounts/', include('django.contrib.auth.urls')),
	path("accounts/", include("allauth.urls")),
	
	path("accounts/", include("django_registration.backends.activation.urls"))




]