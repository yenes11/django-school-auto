from django.db import models
from sorular.models import Quiz
from users.models import User

class Result(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()

    def __str__(self):
        return str(self.pk)
    
    class Meta:
        verbose_name_plural = "Sonuçlar"