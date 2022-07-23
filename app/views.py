from django.shortcuts import render
from .models import mails

# Create your views here.

def home(request):
    if request.method == 'POST':
        m = mails()
        m.text = request.POST.get('text')
        m.save()
        return render(request, 'index.html')
        
    return render(request, 'index.html')