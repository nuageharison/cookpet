from django.shortcuts import render
from datetime import datetime
def index(request):
    return render(request, 'okada/index.html')

def index2(request):
    return render(request, 'okada/index2.html')

def index3(request):
    return render(request, 'okada/index3.html')

# Create your views here.
