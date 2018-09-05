from django.db import models
from mainapp.models import Article, PhotoAlbum, Video, EditorArticle, Nonfiction
from mainapp_english.models import EditorArticleEng  # , ArticleEng
from authapp.models import KarateworldUser
from django.utils import timezone


class Comment(models.Model):

    class Meta():
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    article_id = models.ForeignKey(Article, blank=True, null=True, on_delete=models.DO_NOTHING,
                                   verbose_name='Статья, к которой относится комментарий')
    editor_id = models.ForeignKey(EditorArticle, blank=True, null=True, on_delete=models.DO_NOTHING,
                                  verbose_name='Статья гл. редактора, к которой относится комментарий')
    # article_eng_id = models.ForeignKey(ArticleEng, blank=True, null=True, on_delete=models.DO_NOTHING,
    #                                    verbose_name='Англ. статья, к которой относится комментарий')
    editor_eng_id = models.ForeignKey(EditorArticleEng, blank=True, null=True, on_delete=models.DO_NOTHING,
                                      verbose_name='Англ. статья гл. редактора, к которой относится комментарий')
    nonfiction_id = models.ForeignKey(Nonfiction, blank=True, null=True, on_delete=models.DO_NOTHING,
                                      verbose_name='Статья из публицистики, к которой относится комментарий')
    photo_album_id = models.ForeignKey(PhotoAlbum, blank=True, null=True, on_delete=models.DO_NOTHING,
                                       verbose_name='Фотоальбом, к которому относится комментарий')
    video_id = models.ForeignKey(Video, blank=True, null=True, on_delete=models.DO_NOTHING,
                                 verbose_name='Видео-клип, к которому относится комментарий')
    author_id = models.ForeignKey(KarateworldUser, on_delete=models.DO_NOTHING, verbose_name='Автор комментария')
    avatar = models.CharField(max_length=300, null=True, blank=True)
    comment = models.TextField(max_length=3000, verbose_name='Текст комментария')
    #date = models.DateTimeField(verbose_name='дата комментария', auto_now_add=True)
    date = models.DateTimeField(verbose_name='дата комментария', default=timezone.now)

    def __str__(self):
        return str(self.id) + '---' + str(self.date) + '---' + str(self.author_id) + '---' + str(self.article_id) + \
               '-' + str(self.editor_id) + '-' + str(self.editor_eng_id) + '-' + str(self.nonfiction_id) + '-' + \
               str(self.photo_album_id) + '-' + str(self.video_id) + '---' + '<<'+self.comment[:21]+'>>'