#coding=utf-8
from django.db import models
from django.urls import reverse

from mainapp.models import Country, ArticleCategory, PhotoAlbum, Video

import random


class ArticleEng(models.Model):

    """Статья для главной на английском"""

    class Meta():
        verbose_name = 'Не использовать! Article'
        verbose_name_plural = 'Не использовать! Articles'

    title = models.CharField(max_length=100, verbose_name='Название статьи')  # название статьи

    date = models.DateField(auto_now_add=True, null=True)  # дата создания статьи

    type = models.ForeignKey(ArticleCategory, on_delete=models.DO_NOTHING, null=True, verbose_name='Тип статьи')
                                                                        # вид события: напр., соревнования или лагерь

    image = models.ImageField(upload_to='photo_eng', blank=True, null=True,
                              verbose_name='Изображение вместо флага (если не соревнования/лагерь), размер 250x150, желательно .png')

    country = models.ForeignKey(Country, blank=True, null=True, on_delete=models.DO_NOTHING,
                                verbose_name='Страна проведения')  # страна проведения

    date_start = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True,
                                  verbose_name='Дата начала турнира')  # дата начала соревнований/лагеря
    date_end = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True,
                                verbose_name='Дата окончания турнира')  # дата окончания соревнований/лагеря

    text = models.TextField(blank=True, verbose_name='Основной текст статьи')  # текст основной информации о событии (правила, участники и т.д.)

    image_poster_logo_upper = models.ImageField(upload_to='photo_eng', blank=True,
                                                verbose_name='Постер/логотип - расположен над текстом, для постеров шире 400px')  # изображение (постер или логотип организации);
                                                                                    #  расположен сверху

    image_poster_logo = models.ImageField(upload_to='photo_eng', blank=True,
                                          verbose_name='Постер турнира/логотип организации - расположен слева')  # изображение (постер или логотип организации);
                                                                                    # расположен слева
    file1 = models.FileField(upload_to='photo_eng', blank=True, verbose_name='Файл 1 (положение, заявка и т.д.)')  # файлы (положения, заявки, приложения и т.д.)
    file2 = models.FileField(upload_to='photo_eng', blank=True, verbose_name='Файл 2 (положение, заявка и т.д.)')
    file3 = models.FileField(upload_to='photo_eng', blank=True, verbose_name='Файл 3 (положение, заявка и т.д.)')
    file4 = models.FileField(upload_to='photo_eng', blank=True, verbose_name='Файл 4 (положение, заявка и т.д.)')
    file5 = models.FileField(upload_to='photo_eng', blank=True, verbose_name='Файл 5 (положение, заявка и т.д.)')

    file1_name = models.CharField(max_length=32, blank=True, verbose_name='Название файла 1')
    file2_name = models.CharField(max_length=32, blank=True, verbose_name='Название файла 2')
    file3_name = models.CharField(max_length=32, blank=True, verbose_name='Название файла 3')
    file4_name = models.CharField(max_length=32, blank=True, verbose_name='Название файла 4')
    file5_name = models.CharField(max_length=32, blank=True, verbose_name='Название файла 5')

    city_description = models.TextField(blank=True, verbose_name='Описание города/страны')

    image1 = models.ImageField(upload_to='photo_eng', blank=True,
                               verbose_name='Фото 1 для статьи, все доп. фото 680px по ширине и одинаковой высоты')  # фото, связанные с событием (не больше 6)
    image2 = models.ImageField(upload_to='photo_eng', blank=True, verbose_name='Фото 2 для статьи')
    image3 = models.ImageField(upload_to='photo_eng', blank=True, verbose_name='Фото 3 для статьи')
    image4 = models.ImageField(upload_to='photo_eng', blank=True, verbose_name='Фото 4 для статьи')
    image5 = models.ImageField(upload_to='photo_eng', blank=True, verbose_name='Фото 5 для статьи')
    image6 = models.ImageField(upload_to='photo_eng', blank=True, verbose_name='Фото 6 для статьи')

    image_city_1 = models.ImageField(upload_to='photo_eng', blank=True,
                                     verbose_name='Фото города 1, 680px по ширине и все одинаковой высоты')
    image_city_2 = models.ImageField(upload_to='photo_eng', blank=True,
                                     verbose_name='Фото города 2, 680px по ширине')

    additional_text = models.TextField(blank=True, null=True,
                                       verbose_name='Текст в конце статьи, напр., ссылка на другую статью')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('main:id', args=[str(self.id)])


class EditorArticleEng(models.Model):

    '''Статья главного редактора на английском'''

    class Meta():
        verbose_name = "Editor's article"
        verbose_name_plural = "Editor's articles"

    title = models.CharField(max_length=100, unique=True, verbose_name='Название статьи')  # название статьи

    date = models.DateField(auto_now_add=True, null=True)  # дата создания статьи

    text = models.TextField(blank=True, verbose_name='Основной текст статьи')  # текст основной информации о событии (правила, участники и т.д.)

    image_poster_logo = models.ImageField(upload_to='photo_eng', blank=True,
                                          verbose_name='Основное фото для статьи')  # изображение (постер или логотип организации);
                                                                        # расположен слева

    image1 = models.ImageField(upload_to='photo_eng', blank=True,
                               verbose_name='Другие фото: Фото 1 для статьи гл. редактора, все доп фото одинаковой высоты')  # другие фото, не более двух
    image2 = models.ImageField(upload_to='photo_eng', blank=True, verbose_name='Фото 2 для статьи гл. редактора')

    additional_text = models.TextField(blank=True, null=True,
                                       verbose_name='Текст в конце статьи, напр., ссылка на другую статью')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('main:editor_id', args=[str(self.id)])


class MainPageArticleEng(models.Model):

    class Meta():
        verbose_name = 'Main page first place article (may be absent)'
        verbose_name_plural = 'Main page first place article (may be absent)'

    editor = models.ForeignKey(EditorArticleEng, on_delete=models.DO_NOTHING, blank=True, null=True,
                                      verbose_name="Editor in chief's article")
    album = models.ForeignKey(PhotoAlbum, on_delete=models.DO_NOTHING, blank=True, null=True,
                                      verbose_name='Photo album')
    video = models.ForeignKey(Video, on_delete=models.DO_NOTHING, blank=True, null=True,
                              verbose_name='Video')

    def __str__(self):
        return 'Main page first place article'