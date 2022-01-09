from django import forms
from .models import ogrenciler, ogretmenler, User, dersler
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.contrib.auth.models import Group

class ogretmenKayit(UserCreationForm):
    email = forms.EmailField(required=True)
    brans = forms.ModelChoiceField(queryset=dersler.objects.all())
    
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'brans', 'email',)
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('email')
        user.is_teacher = True
        user.save()
        user.is_staff = True
        group = Group.objects.get(name='Ogretmen')
        user.groups.add(group)
        user.save()
        teacher = ogretmenler.objects.create(user=user)
        teacher.brans = self.cleaned_data.get('brans')
        teacher.save()
        return teacher

class ogrenciKayit(UserCreationForm):
    email = forms.EmailField(required=True)
    numara = forms.CharField(max_length=5, required=True)
    
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'numara', 'email',)
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('email')
        user.is_student = True
        user.save()
        #group = Group.objects.get(name='student')
        #user.groups.add(group)
        #user.save()
        student = ogrenciler.objects.create(user=user)
        student.numara = self.cleaned_data.get('numara')
        student.save()
        return student

class mylogin(forms.Form):
    username = forms.CharField(max_length=25)
    password = forms.CharField()


