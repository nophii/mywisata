from django.urls import path, include
from .views import *

# untuk media
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import handler404, handler500


urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('artikel/', artikel, name='tabel_artikel'),
    path('artikel/tambah', tambah_artikel, name='tambah_artikel'),
    path('artikel/lihat/<str:id>', lihat_artikel, name='lihat_artikel'),
    path('artikel/edit/<str:id>', edit_artikel, name='edit_artikel'),
    path('artikel/delete/<str:id>', delete_artikel, name='delete_artikel'),


    path('users/',users, name='tabel_users'),
    
]

urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)