from django.db import models
from django_mysql.models import ListCharField
from users.models import siniflar

class Program(models.Model):
    name = models.CharField(max_length=20, default='program_1')
    sinif = models.ForeignKey(siniflar, on_delete=models.CASCADE, default=1)
    pazartesi = ListCharField(
        verbose_name = 'Pazartesi',
        base_field=models.CharField(max_length=15),
        size=10,
        max_length=(10 * 16) 
    )
    sali = ListCharField(
        verbose_name = 'Salı',
        base_field=models.CharField(max_length=15),
        size=10,
        max_length=(10 * 16) 
    )
    carsamba = ListCharField(
        verbose_name = 'Çarşamba',
        base_field=models.CharField(max_length=15),
        size=10,
        max_length=(10 * 16) 
    )
    persembe = ListCharField(
        verbose_name = 'Perşembe',
        base_field=models.CharField(max_length=15),
        size=10,
        max_length=(10 * 16) 
    )
    cuma = ListCharField(
        verbose_name = 'Cuma',
        base_field=models.CharField(max_length=15),
        size=10,
        max_length=(10 * 16) 
    )
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Ders Programları"