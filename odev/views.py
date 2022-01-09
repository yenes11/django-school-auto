from django.shortcuts import render, redirect
from .models import Odev_Konu, Yuklenen_Odev
from django.core.files.storage import FileSystemStorage
from django.views.generic.edit import CreateView


class OdevYukle(CreateView):
    model = Yuklenen_Odev
    fields = ['odev', 'dosya']

    def form_valid(self, form):
        form.instance.yukleyen = self.request.user.ogrenciler
        return super().form_valid(form)


def upload(request):
    if not request.user.is_authenticated:
        return redirect('base') 
    else:
        context = {
            'obj' :  Odev_Konu.objects.all(),
        }
        return render(request, 'odev/odev.html', context)