import mainapp.views as mainapp
from django.urls import path

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.articles, name='main'),
    path('photo/', mainapp.gallery_photo, name='photo'),
    path('video/', mainapp.gallery_video, name='video'),
    #path('editor_in_chief/', mainapp.editor_in_chief, name='editor_in_chief'),
    path('photo/<pk>/', mainapp.photo_album, name='photo_id'),
    path('video/<pk>/', mainapp.video_album, name='video_id'),
    path('editor_in_chief/<pk>/', mainapp.editor_article, name='editor_id'),
    path('nonfiction/<pk>/', mainapp.nonfiction_article, name='nonfiction'),
    path('<pk>/', mainapp.articles, name='type'),
    path('<pk>/country/<id>/', mainapp.articles, name='country'),
    path('article/<pk>/', mainapp.article, name='id'),
]