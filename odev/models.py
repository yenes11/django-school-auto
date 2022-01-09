from django.db import models
from django.db.models.base import Model
from users.models import dersler, ogrenciler
from django.urls import reverse


class Odev_Konu(models.Model):
    ders = models.ForeignKey(dersler, on_delete=models.CASCADE)
    konu = models.CharField(max_length=500)

    def get_answers(self):
        return self.yuklenen_odev_set.all()

    def __str__(self):
        return f"{self.ders} Ödevi #{self.pk}"
    
    class Meta:
        verbose_name_plural = "Ödevler"


class Yuklenen_Odev(models.Model):
    yukleyen = models.ForeignKey(ogrenciler, on_delete=models.CASCADE)
    odev = models.ForeignKey(Odev_Konu, on_delete=models.CASCADE)
    dosya = models.FileField(upload_to='odevler')
    created = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('odev')

    class Meta:
        verbose_name_plural = "Yüklenen Ödevler"