from django.contrib import admin
from django.urls import path, include
from . views import *

#untuk media
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import handler404, handler500


urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', include('mywisata.urls')),
    

    path('', index,name='index'),
    path('about/', about, name='about'),
    path('blog/', blog, name='blog'),
    path('gallery/', gallery, name='gallery'),
    path('deskripsi/', deskripsi, name='deskripsi'),

    path('login/', login, name='login'),
    path('logout/', logout_views, name='logout'),

    path('artikel_detail/<int:id>', artikel_detail, name='artikel_detail'),
]

urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)