from django.contrib import admin
from .models import *
# Register your models here.

class ArtikelAdmin(admin.ModelAdmin):
    list_display = ('nama_tempat', 'body', 'lokasi', 'kategory', 'img', 'published')

admin.site.register(Kategori)
admin.site.register(Artikel, ArtikelAdmin)
