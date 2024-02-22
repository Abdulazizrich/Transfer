from django.contrib import admin
from django.urls import path
from mainApp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('clubs/', clubs, name='clubs'),
    path('players/', players,name='players'),
    path('<str:count_name>/clubs/', davlat_club),
    path('players20/', u_20, name='u_20'),
    path('latest/', transfer_2023, name='latest'),
    path('stats/', stats, name='stats'),
    path('record1/', t_records, name='record1'),
    path('about/', about, name='about'),
    path('<str:nom>/players/', club_players),
    path('tryouts/', tryouts, name='tryouts'),
    path('record2/', records150, name='record2'),
    path('top50/', top50, name='top50'),
    path('top502/', top502, name='top502'),
    path('archive/', archive, name='archive'),
    path('<str:mavsum>/18season/', season, name='season'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)