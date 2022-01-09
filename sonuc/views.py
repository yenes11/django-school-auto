from django.shortcuts import render, redirect
from .models import Result
from sinav.models import Quiz


def sonuc(request):
    if not request.user.is_authenticated:
        return redirect('base') 
    else:
        current_user = request.user
        context = {
            'sonuc' :  Result.objects.filter(user=current_user),
        }
        return render(request, 'sonuc/sonuc.html', context)