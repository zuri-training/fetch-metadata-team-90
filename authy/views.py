from django.shortcuts import render, redirect, get_object_or_404
from authy.forms import ChangePasswordForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic.edit import UpdateView
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.views.generic import RedirectView
from authy.models import Profile
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib import messages

User = get_user_model()


class SignupRedirectView(RedirectView):
    pass
class PasswordChangeRedirectView(RedirectView):
    pass
class UserProfile(LoginRequiredMixin, View):
    form = ChangePasswordForm
    context = {"form":form}
    template_name = 'seetings.html'
    
    def get(self, request):
        user = get_object_or_404(User, email=request.user.email)
        self.context['profile'] = Profile.objects.get(user=user)
        return render(request, self.template_name, self.context)

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            new_password = form.cleaned_data.get('new_password')
            user.set_password(new_password)
            user.save()
            update_session_auth_hash(request, user)
            messages.success(request, "password change success")
            return redirect('change_password_done')
        else:
            user = get_object_or_404(User, email=request.user.email)
            form = self.form(instance=user)

            self.context = {
                'form':form,
            }

            return render(request, self.template_name, self.context)

def PasswordChangeDone(request):
    return render(request, 'change_password_done.html')



class UpdateProfileView(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = ['picture', 'first_name', 'last_name', 'location', 'url', 'profile_info']
    success_message = "Update done successfully"
    