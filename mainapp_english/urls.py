import mainapp_english.views as mainapp_english
from django.urls import path

app_name = 'mainapp_english'

urlpatterns = [
    path('', mainapp_english.articles_eng, name='main'),
    path('photo/', mainapp_english.gallery_photo_eng, name='photo'),
    path('video/', mainapp_english.gallery_video_eng, name='video'),
    #path('editor_in_chief/', mainapp_english.editor_in_chief_eng, name='editor_in_chief'),
    path('photo/<pk>/', mainapp_english.photo_album, name='photo_id'),
    path('video/<pk>/', mainapp_english.video_album, name='video_id'),
    path('editor_in_chief/<pk>/', mainapp_english.editor_article_eng, name='editor_id'),
    path('<pk>/', mainapp_english.articles_eng, name='type'),
    path('<pk>/country/<id>/', mainapp_english.articles_eng, name='country'),
    path('article/<pk>/', mainapp_english.article_eng, name='id'),
]