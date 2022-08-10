from django.shortcuts import render
from .forms import FileContentForm
from .models import FileContent
# Create your views here.
def test(request, *args, **kwargs):
    form = FileContentForm(request.POST or None, request.FILES or None)
    file = ''
    if request.method == 'POST' or request.method == 'FILES':
        if form.is_valid():
            form.save()
            form = FileContentForm()
            file = request.FILES['file'].name
    object = FileContent.objects.filter(file__iexact=file)
    context = {
        'form': form,
        'object': object,
    }
    return render(request, 'metadata.html', context)

def home(request, *args, **kwargs):

    return render(request, 'index.html', {})
