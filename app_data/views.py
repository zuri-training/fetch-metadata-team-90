from django.shortcuts import render
from django.views.generic.base import TemplateView
from .forms import ContactForm

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


