from django.shortcuts import render, redirect
from .models import Duyuru

def duyuru(request):
    if not request.user.is_authenticated:
        return redirect('base') 
    else:
        context = {
            'duyuru' :  Duyuru.objects.all(),
        }
        return render(request, 'duyuru/duyuru.html', context)
