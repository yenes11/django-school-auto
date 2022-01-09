from django.contrib import admin
from .models import Answer, Question

class AnwerInLine(admin.TabularInline):
    model = Answer

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnwerInLine]

admin.site.register(Answer)
admin.site.register(Question, QuestionAdmin)