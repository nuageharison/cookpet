from django.shortcuts import render, redirect
from .forms import DocumentForm
from .models import Document


def index(request):
    if request.method == 'POST':
        form = DocumentForm( request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DocumentForm()
        obj = Document.objects.all()

    return render(request, 'okada/index.html', {
        'form': form,
        'obj': obj
    })
