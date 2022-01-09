from django.db import models
from sinav.models import Quiz

class Question(models.Model):
    text = models.CharField(max_length=250)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    def get_answers(self):
        return self.answer_set.all()

    class Meta:
        verbose_name_plural = "Sorular"

class Answer(models.Model):
    text = models.CharField(max_length=250)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Soru: {self.question.text}, Cevap: {self.text}, Doğru: {self.correct}"
    
    class Meta:
        verbose_name_plural = "Cevaplar"