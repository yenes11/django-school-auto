from django.contrib import admin
from .models import Odev_Konu, Yuklenen_Odev

class AnwerInLine(admin.TabularInline):
    model = Yuklenen_Odev

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnwerInLine]

admin.site.register(Yuklenen_Odev)
admin.site.register(Odev_Konu, QuestionAdmin)