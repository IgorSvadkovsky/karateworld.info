from django.contrib import admin
from .models import Country, ArticleCategory, Article, PhotoAlbum, Video, EditorArticle, Nonfiction, MainPageArticle

# Register your models here.

admin.site.register(Country)
admin.site.register(ArticleCategory)
admin.site.register(Article)
admin.site.register(EditorArticle)
admin.site.register(Nonfiction)
admin.site.register(PhotoAlbum)
admin.site.register(Video)
admin.site.register(MainPageArticle)
