from django.contrib import admin
from django.urls import path, include
from . import views
from users import views as usr_views
from django.contrib.auth import views as auth_views 
from sonuc.views import sonuc
from odev.views import upload, OdevYukle
from duyuru.views import duyuru
from users.views import base


urlpatterns = [
    
    path('',views.program, name='ders-programi'),
    path('sonuc/',sonuc, name='sonuc'),
    path('base/',base, name='base'),
    path('duyuru/',duyuru, name='duyuru'),
    path('odev/',upload, name='odev'),
    path('odev/yeni',OdevYukle.as_view(), name='odev-yukle'),
    path('dersler/', views.dersler1, name='dersler'),
    path('kaydol/', usr_views.register.as_view(), name='kaydol'),
    path('sinavlar/', views.sinavlar, name='sinavlar'),
    path('ogrencikayit/', usr_views.ogrenciregister.as_view(), name='ogrencikayit'),
    path('giris/', auth_views.LoginView.as_view(template_name='users/giris.html'), name='giris'),
    path('cikis/', auth_views.LogoutView.as_view(template_name='users/cikis.html'), name='cikis'),
    path('odevler/', views.odevler ,name='odevler'),
]