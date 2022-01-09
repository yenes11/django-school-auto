from django.contrib import admin
from .models import dersler, ogrenciler, ogretmenler, odevler, siniflar, User


class hor_sinif(admin.ModelAdmin):
    model = siniflar
    filter_horizontal = ('alinan_dersler',)

admin.site.register(dersler)
admin.site.register(ogretmenler)
admin.site.register(ogrenciler)
admin.site.register(odevler)
admin.site.register(User)
admin.site.register(siniflar, hor_sinif)
