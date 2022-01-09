from django.db import models
from users.models import dersler
import random
from users.models import siniflar


Sinav_Secimi = [
        ('1.Sınav', '1.Sınav'),
        ('2.Sınav', '2.Sınav'),
        ('3.Sınav', '3.Sınav'),
    ]

class Quiz(models.Model):
    name = models.ForeignKey(dersler, on_delete=models.CASCADE)
    topic = models.CharField(max_length=7, choices=Sinav_Secimi)
    soru_sayisi = models.IntegerField()
    time = models.IntegerField()
    sinif = models.ForeignKey(siniflar, on_delete=models.CASCADE, default=2)

    def __str__(self):
        return str(self.name) + " " + self.topic + "ı"

    def get_question(self):
        questions = list(self.question_set.all())
        random.shuffle(questions)
        return questions[:self.soru_sayisi]

    class Meta:
        verbose_name_plural = "Sınavlar"