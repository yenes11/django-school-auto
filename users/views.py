from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import ogrenciKayit, ogretmenKayit
from django.views.generic import CreateView
from .models import User, ogrenciler, ogretmenler
from django.contrib.auth import login
from django.contrib.auth.models import Group
from django.contrib import messages

from django.urls import path, include
import os
import face_recognition
import cv2
from .forms import mylogin
from django.contrib.auth import authenticate, login


class register(CreateView):
    model = User
    form_class = ogretmenKayit
    template_name = 'kaydol.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        return redirect('giris')

class ogrenciregister(CreateView):
    model = User
    form_class = ogrenciKayit
    template_name = 'ogrencikayit.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        return redirect('giris')

import numpy as np


def facedect(loc):

    cap = cv2.VideoCapture(0) # video capture source camera (Here webcam of laptop) 
    ret,frame = cap.read() # return a single frame in variable `frame`
    if ret:   
            
            BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            #MEDIA_ROOT =os.path.join(BASE_DIR,'users')
            MEDIA_ROOT = os.path.join(BASE_DIR)
            print(MEDIA_ROOT)
            loc=(str(MEDIA_ROOT)+loc)
            face_1_image = face_recognition.load_image_file(loc)
 

            face_1_face_encoding = face_recognition.face_encodings(face_1_image)[0]



            #
            loc2 = MEDIA_ROOT + '/media/temp/c1.jpeg'
            cv2.imwrite(loc2, frame)
            cap.release()

            face_2_image = face_recognition.load_image_file(loc2)
            try:
                face_2_face_encoding = face_recognition.face_encodings(face_2_image)[0]
            except:
                return False

            #small_frame = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)

            #rgb_small_frame = small_frame[:, :, ::-1]

            #face_locations = face_recognition.face_locations(rgb_small_frame)
            #face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
    

            check=face_recognition.compare_faces([face_1_face_encoding], face_2_face_encoding)
            

            print(check)

            if check[0]:
                return True

            else :
                return False
                


def base(request):
    if request.method =="POST":
        form =mylogin(request.POST)
        if form.is_valid():
            username=request.POST['username']
            password=request.POST['password']
            user = authenticate(request,username=username,password=password)
            if user is not None:
                if facedect(user.ogrenciler.foto.url):
                    login(request,user)
                    return redirect('ders-programi')
                else:
                    messages.warning(request, "Yüz tanınamadı.")
                    return redirect('base')
            else:
                return redirect('base')
                            
    else:
        MyLoginForm = mylogin()
        return render(request,"facelogin.html",{"MyLoginForm": MyLoginForm})  