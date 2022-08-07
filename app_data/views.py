from django.shortcuts import render
from .forms import ContactForm
from django.views.generic import TemplateView, DetailView
from .models import FileUpload
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa

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
def Contact(request):
	
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			message = form.save(commit=False)
			message.message_date = timezone.now()
			form.save()
			return redirect('contactsuccess')
	else:
		form = ContactForm()

	context = {
		'form':form,
	}

	return render(request, 'contact.html', context)


#static website for the form contact


class ContactSuccess(TemplateView):
    template_name = "contactsuccess.html"



class DashboardView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        if self.request.user is None:
            return
        context['file_list'] = self.request.user.user_file.all()
        return context



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
