from .forms import ContactForm
from django.views.generic import TemplateView, DetailView
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ContactForm, FileUploadForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, DetailView, CreateView
from django.views import View
from .models import FileUpload
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa
from django.utils import timezone
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator

from django.conf import settings
from django.core.mail import send_mail, send_mass_mail
from django.contrib import messages

# to be placed in a differn=ent file  
def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


class HomePageView(TemplateView):
    template_name = "index.html"



# //wil be change to class based view 
class ContactView(View):
    form = ContactForm
    template_name = 'contact.html'
    context  = {'form': form}
    def get(self, request):
        return render(request, self.template_name, self.context)
    
    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            name_email = request.POST['name']
            email = request.POST['sender_email']
            
            subject = request.POST['subject']
            message_email = request.POST['message']
            message_email2 = f'{message_email} from {email}'
            print(message_email2, settings.EMAIL_HOST_USER)
            try:
                send_mail(subject, message_email2, email, 
                [settings.EMAIL_HOST_USER], fail_silently=False,)
                messages.success(request, 'Thanks, A response has been sent to your mail')
                
                return render(request, self.template_name, self.context)
            except:
                messages.error(request, 'Email not sent, Something went wrong. Try again!')
                return render(request, self.template_name, self.context)
            
        else:
            self.context['form'] = form
            return render(request, self.template_name, self.context)


#static website for the form contact


class ContactSuccess(TemplateView):
    template_name = "contactsuccess.html"

class PrivacyView(TemplateView):
    template_name = 'privacy-policies.html'

class TermsConditionView(TemplateView):

    template_name = 'terms-conditions.html'

class DocumentationView(TemplateView):
    template_name = 'documentation.html'  

class ArchiveView(TemplateView):
    template_name = 'archive.html'

class DashboardView(LoginRequiredMixin, View):
    template_name = 'dashboard.html'
    form = FileUploadForm
    context = {'form': form} 
    @method_decorator(never_cache)
    def get(self, request):
        q = request.GET.get('q')
        if q:
            self.context['file_list'] = FileUpload.objects.search(q)
        self.context['file_list'] = self.request.user.user_file.all()
        return render(request, self.template_name, self.context)
    @method_decorator(never_cache)
    def post(self, request):
        form = self.form(request.POST, request.FILES)
        if form.is_valid():
            _form = form.save(commit=False)
            _form.user = request.user
            saved_data = form.save()
            print(saved_data.file_name)
            self.context['file_list'] = self.request.user.user_file.all()
            if saved_data:
                self.context['new_data'] = self.context['file_list'][0]
            else :
                self.context['new_data'] = None

            
            
            return render(request, self.template_name, self.context)
        else:
            self.context['form'] = form
            return render(request, self.template_name, self.context)

class SavePageView(LoginRequiredMixin, View):
    template_name = 'save_page.html'
    context = {}
    @method_decorator(never_cache)
    def get(self, request):
        q = request.GET.get('q')
        if q:
            self.context['file_list'] = FileUpload.objects.search(q)
        self.context['file_list'] = self.request.user.user_file.all()
        return render(request, self.template_name, self.context)


class FileUploadDetailView(DetailView):
    def get_object(self, queryset=None):
        obj = FileUpload.objects.filter(user__pk=self.request.user.pk).get(pk=self.kwargs.get('pk'))
        return obj

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        pdf = render_to_pdf('pdf_template.html', {'data': obj.exif})
        query = request.GET.get('q')
        if query:
            return HttpResponse(pdf, content_type='application/pdf')
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = f"metlap{kwargs['pk']}.pdf"
        content = "attachment; filename='%s'" %(filename)
        response['Content-Disposition'] = content
        return response

class ShareFileUploadDetailView(DetailView):
    model = FileUpload
    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        pdf = render_to_pdf('pdf_template.html', {'data': obj.exif})
        return HttpResponse(pdf, content_type='application/pdf')

# class CreateFilePuloadView(LoginRequiredMixin, CreateView):
#     model = FileUpload
#     fields = ['file']
#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)
def search(request, *args, **kwargs):
    query = request.POST.get('q')
    if request.user.is_authenticated:
        user = request.user
        user_files = user.user_file.all()
    else:
        user_files = None
    result = FileUpload.objects.filter(user=user).search(query)
    context = {
        'files': result,
        'user': user_files

    } 

    return render(request, 'search.html', context)