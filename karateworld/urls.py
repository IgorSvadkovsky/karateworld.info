"""karateworld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from mainapp.views import SearchView, shotokan, shito, goju, wado, \
    show_all_view, show_competitions_view, show_sport_camps_view, show_sport_science_view, show_editor_view, \
    show_nonfiction_view, show_photo_view, show_video_view

from mainapp_english.views import SearchViewEng, shotokan_eng, shito_eng, goju_eng, wado_eng, \
    show_all_view_eng, show_competitions_view_eng, show_sport_camps_view_eng, show_sport_science_view_eng, \
    show_editor_view_eng, show_photo_view_eng, show_video_view_eng

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('search/', SearchViewEng.as_view(), name = 'search_eng'),
    path('shotokan/', shotokan_eng, name='shotokan_eng'),
    path('shito-ryu/', shito_eng, name='shito_eng'),
    path('goju-ryu/', goju_eng, name='goju_eng'),
    path('wado-ryu/', wado_eng, name='wado_eng'),
    path('all_articles/', show_all_view_eng, name='show_all_eng'),
    path('competitions/', show_competitions_view_eng, name='show_competitions_eng'),
    path('sport_camps/', show_sport_camps_view_eng, name='show_sport_camps_eng'),
    path('sport_science/', show_sport_science_view_eng, name='show_sport_science_eng'),
    path('editor_in_chief/', show_editor_view_eng, name='show_editor_eng'),
    path('photo_albums/', show_photo_view_eng, name='show_photo_eng'),
    path('videos/', show_video_view_eng, name='show_video_eng'),
    #path('editor_articles/', show_editor_view_eng, name='show_editors_eng'),

    path('ru/search/', SearchView.as_view(), name = 'search'),
    path('ru/shotokan/', shotokan, name='shotokan'),
    path('ru/shito-ryu/', shito, name='shito'),
    path('ru/goju-ryu/', goju, name='goju'),
    path('ru/wado-ryu/', wado, name='wado'),
    path('ru/all_articles/', show_all_view, name='show_all'),
    path('ru/competitions/', show_competitions_view, name='show_competitions'),
    path('ru/sport_camps/', show_sport_camps_view, name='show_sport_camps'),
    path('ru/sport_science/', show_sport_science_view, name='show_sport_science'),
    path('ru/editor_in_chief/', show_editor_view, name='show_editor'),
    path('ru/nonfiction/other/', show_nonfiction_view, name='show_nonfiction'),
    path('ru/photo_albums/', show_photo_view, name='show_photo'),
    path('ru/videos/', show_video_view, name='show_video'),
    #path('ru/editor_articles/', show_editor_view, name='show_editors'),
    path('ru/', include('mainapp.urls', namespace = 'articles')),
    path('', include('mainapp_english.urls', namespace = 'main')),

    path('auth/', include('authapp.urls', namespace = 'auth')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
