from django.db import models

class Duyuru(models.Model):
    konu = models.CharField(max_length=40)
    icerik = models.TextField(max_length=500)

    def __str__(self):
        return str(self.konu)

    class Meta:
        verbose_name_plural = "Duyurular"