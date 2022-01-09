from django.shortcuts import render, redirect
from programs.models import Program
from users.models import dersler, siniflar



posts = {
    'saatler': ['09:00', '10:00', '11:00', '12:00', '13:00'],
}


def program(request):
    if not request.user.is_authenticated:
        return redirect('base') 
    else:
        current_user = request.user.ogrenciler.sinifi
        context = {
        'dersprg' :  Program.objects.filter(sinif=current_user),
        'saatler' : posts
        }
        return render(request, 'dash/program.html', context)

def dersler1(request):
    if not request.user.is_authenticated:
        return redirect('base') 
    else:
        cu = request.user.ogrenciler.sinifi
        context = {
            'dersler' :  dersler.objects.all(),
        }
        return render(request, 'dash/dersler.html', context)

def odevler(request):
    return render(request, 'dash/odevler.html')

def sinavlar(request):
    return render(request, 'dash/sinavlar.html')