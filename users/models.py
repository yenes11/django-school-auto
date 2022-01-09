from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Kullanıcılar"

class dersler(models.Model):
    ders_adi = models.CharField(max_length=30)
    ders_link = models.URLField()
    def __str__(self):
        return str(self.ders_adi)
    
    class Meta:
        verbose_name_plural = "Dersler"


class ogretmenler(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ogrt_adi = models.CharField(max_length=30)
    ogrt_soyadi = models.CharField(max_length=30)
    brans = models.ForeignKey(dersler, null=True, on_delete=models.CASCADE)
    foto = models.ImageField(default='default.jpg', upload_to='profile_pics')
    #mail

    def __str__(self):
        return self.ogrt_adi + " Öğretmen" + self.ogrt_soyadi

    class Meta:
        verbose_name_plural = "Öğretmenler"

class odevler(models.Model):
    ders = models.ForeignKey(dersler, null=True, on_delete=models.CASCADE)
    odev = models.TextField()
    teslim = models.DateTimeField()

    def __str__(self):
        return str(self.ders) + ' Ödevi'

    class Meta:
        verbose_name_plural = "Ödevler"


class siniflar(models.Model):
    sinif = models.CharField(max_length=10)
    alinan_dersler = models.ManyToManyField(dersler)

    def __str__(self):
        return self.sinif

    class Meta:
        verbose_name_plural = "Sınıflar"


class ogrenciler(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ogr_adi = models.CharField(max_length=30)
    ogr_soyadi = models.CharField(max_length=30)
    sinifi = models.ForeignKey(siniflar, null=True, on_delete=models.CASCADE)
    numara = models.CharField(max_length=5)
    foto = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return self.numara + " numaralı öğrenci"

    class Meta:
        verbose_name_plural = "Öğrenciler"