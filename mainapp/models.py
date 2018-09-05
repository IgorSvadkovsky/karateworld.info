#coding=utf-8
from django.db import models
from django.urls import reverse

import random


class Country(models.Model):

    '''Страны'''

    class Meta():
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'

    name_rus = models.CharField(max_length=50, unique=True, verbose_name='Название на русском')
    name_eng = models.CharField(max_length=50, null=True, verbose_name='Название на английском')

    flag = models.ImageField(upload_to='flags', null=True, verbose_name='Флаг, размер 250x150, желательно .png')

    def __str__(self):
        return self.name_rus


class ArticleCategory(models.Model):

    '''Тип статьи'''

    class Meta():
        verbose_name = 'Тип статьи'
        verbose_name_plural = 'Типы статей'

    type_rus = models.CharField(max_length=32, unique=True, verbose_name='Тип статьи на русском')
    type_eng = models.CharField(max_length=32, null=True, verbose_name='Тип статьи на английском')

    def __str__(self):
        return self.type_rus


class Article(models.Model):

    '''Статья на главной'''

    class Meta():
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    title = models.CharField(max_length=100, verbose_name='Название статьи на русском')  # название статьи
    title_eng = models.CharField(max_length=100, verbose_name='English title of the article', null=True)

    date = models.DateField(auto_now_add=True, null=True)  # дата создания статьи

    type = models.ForeignKey(ArticleCategory, on_delete=models.DO_NOTHING, null=True, verbose_name='Тип статьи')
                                                                        # вид события: напр., соревнования или лагерь

    image = models.ImageField(upload_to='photo', blank=True, null=True,
                              verbose_name='Изображение вместо флага (если не соревнования/лагерь), размер 250x150, желательно .png')

    country = models.ForeignKey(Country, blank=True, null=True, on_delete=models.DO_NOTHING,
                                verbose_name='Страна проведения')  # страна проведения

    date_start = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True,
                                  verbose_name='Дата начала турнира')  # дата начала соревнований/лагеря
    date_end = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True,
                                verbose_name='Дата окончания турнира')  # дата окончания соревнований/лагеря

    text = models.TextField(blank=True, verbose_name='Основной текст статьи на русском')  # текст основной информации о событии (правила, участники и т.д.)
    text_eng = models.TextField(blank=True, verbose_name='Main text of the article in English', null=True)

    image_poster_logo = models.ImageField(upload_to='photo', blank=True,
                                          verbose_name='Постер турнира/логотип организации - расположен слева')  # изображение (постер или логотип организации);
                                                                        # расположен слева

    image_poster_logo_upper = models.ImageField(upload_to='photo', blank=True,
                                          verbose_name='Постер/логотип - расположен над текстом, для постеров шире 400px')  # изображение (постер или логотип организации);
                                                                        #  расположен сверху

    file1 = models.FileField(upload_to='photo', blank=True, verbose_name='Файл 1 (положение, заявка и т.д.)')  # файлы (положения, заявки, приложения и т.д.)
    file2 = models.FileField(upload_to='photo', blank=True, verbose_name='Файл 2 (положение, заявка и т.д.)')
    file3 = models.FileField(upload_to='photo', blank=True, verbose_name='Файл 3 (положение, заявка и т.д.)')
    file4 = models.FileField(upload_to='photo', blank=True, verbose_name='Файл 4 (положение, заявка и т.д.)')
    file5 = models.FileField(upload_to='photo', blank=True, verbose_name='Файл 5 (положение, заявка и т.д.)')

    file1_name = models.CharField(max_length=32, blank=True, verbose_name='Название файла 1 на русском')
    file1_name_eng = models.CharField(max_length=32, blank=True, verbose_name='File 1 English name', null=True)
    file2_name = models.CharField(max_length=32, blank=True, verbose_name='Название файла 2 на русском')
    file2_name_eng = models.CharField(max_length=32, blank=True, verbose_name='File 2 English name', null=True)
    file3_name = models.CharField(max_length=32, blank=True, verbose_name='Название файла 3 на русском')
    file3_name_eng = models.CharField(max_length=32, blank=True, verbose_name='File 3 English name', null=True)
    file4_name = models.CharField(max_length=32, blank=True, verbose_name='Название файла 4 на русском')
    file4_name_eng = models.CharField(max_length=32, blank=True, verbose_name='File 4 English name', null=True)
    file5_name = models.CharField(max_length=32, blank=True, verbose_name='Название файла 5 на русском')
    file5_name_eng = models.CharField(max_length=32, blank=True, verbose_name='File 5 English name', null=True)

    image1 = models.ImageField(upload_to='photo', blank=True,
                               verbose_name='Фото 1 для статьи, все доп. фото 680px по ширине и все одинаковой высоты')  # фото, связанные с событием (не больше 6)
    image2 = models.ImageField(upload_to='photo', blank=True, verbose_name='Фото 2 для статьи')
    image3 = models.ImageField(upload_to='photo', blank=True, verbose_name='Фото 3 для статьи')
    image4 = models.ImageField(upload_to='photo', blank=True, verbose_name='Фото 4 для статьи')
    image5 = models.ImageField(upload_to='photo', blank=True, verbose_name='Фото 5 для статьи')
    image6 = models.ImageField(upload_to='photo', blank=True, verbose_name='Фото 6 для статьи')

    city_description = models.TextField(blank=True, verbose_name='Описание города/страны на русском')
    city_description_eng = models.TextField(blank=True, verbose_name='City/country description in English', null=True)

    image_city_1 = models.ImageField(upload_to='photo', blank=True,
                                     verbose_name='Фото города 1, 680px по ширине и все одинаковой высоты')
    image_city_2 = models.ImageField(upload_to='photo', blank=True,
                                     verbose_name='Фото города 2, 680px по ширине')

    additional_text = models.TextField(blank=True, null=True,
                                       verbose_name='Текст на русс. в конце статьи, напр., ссылка на другую статью')
    additional_text_eng = models.TextField(blank=True, null=True,
                                       verbose_name='Additional English text at the end of the article, e.g., link to the other article')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('articles:id', args=[str(self.id)])

    def get_absolute_url_eng(self):
        return reverse('main:id', args=[str(self.id)])


class PhotoAlbum(models.Model):

    '''Фотоальбом'''

    class Meta():
        verbose_name = 'Фотоальбом'
        verbose_name_plural = 'Фотоальбомы'

    title_rus = models.CharField(max_length=100, unique=True, blank=False,
                                 verbose_name='Название фотоальбома на русском')
    title_eng = models.CharField(max_length=100, blank=False, null=True,
                                 verbose_name='Название фотоальбома на английском')

    date = models.DateField(auto_now_add=True)

    image1 = models.ImageField(upload_to='albums', blank=True,
                               verbose_name='image1 (все фото должны быть одинаковой высоты и по ширине 1200px)')
    image2 = models.ImageField(upload_to='albums', blank=True)
    image3 = models.ImageField(upload_to='albums', blank=True,)
    image4 = models.ImageField(upload_to='albums', blank=True,)
    image5 = models.ImageField(upload_to='albums', blank=True,)
    image6 = models.ImageField(upload_to='albums', blank=True,)
    image7 = models.ImageField(upload_to='albums', blank=True,)
    image8 = models.ImageField(upload_to='albums', blank=True,)
    image9 = models.ImageField(upload_to='albums', blank=True,)
    image10 = models.ImageField(upload_to='albums', blank=True,)
    image11 = models.ImageField(upload_to='albums', blank=True,)
    image12 = models.ImageField(upload_to='albums', blank=True,)
    image13 = models.ImageField(upload_to='albums', blank=True,)
    image14 = models.ImageField(upload_to='albums', blank=True,)
    image15 = models.ImageField(upload_to='albums', blank=True,)
    image16 = models.ImageField(upload_to='albums', blank=True,)
    image17 = models.ImageField(upload_to='albums', blank=True,)
    image18 = models.ImageField(upload_to='albums', blank=True,)
    image19 = models.ImageField(upload_to='albums', blank=True,)
    image20 = models.ImageField(upload_to='albums', blank=True,)
    image21 = models.ImageField(upload_to='albums', blank=True,)
    image22 = models.ImageField(upload_to='albums', blank=True,)
    image23 = models.ImageField(upload_to='albums', blank=True,)
    image24 = models.ImageField(upload_to='albums', blank=True,)
    image25 = models.ImageField(upload_to='albums', blank=True,)
    image26 = models.ImageField(upload_to='albums', blank=True,)
    image27 = models.ImageField(upload_to='albums', blank=True,)
    image28 = models.ImageField(upload_to='albums', blank=True,)
    image29 = models.ImageField(upload_to='albums', blank=True,)
    image30 = models.ImageField(upload_to='albums', blank=True,)

    #image = random.choice([image1, image2, image3, image4, image5])

    additional_text_rus = models.TextField(blank=True,
                                           verbose_name='Текст на рус. под всеми фото, напр., ссылка на другой альбом')

    additional_text_eng = models.TextField(blank=True, null=True,
                                           verbose_name='Текст на англ. под всеми фото, напр., ссылка на другой альбом')

    def __str__(self):
        return self.title_rus

    def get_absolute_url(self):
        return reverse('articles:photo_id', args=[str(self.id)])

    def get_absolute_url_eng(self):
        return reverse('main:photo_id', args=[str(self.id)])


class Video(models.Model):

    '''Видео-клип'''

    class Meta():

        verbose_name = 'Видео-клип'
        verbose_name_plural = 'Видео-клипы'

    title_rus = models.CharField(max_length=100, unique=True, blank=False,
                                 verbose_name='Название видео на русском')
    title_eng = models.CharField(max_length=100, blank=False, null=True, verbose_name='Название видео на английском')

    date = models.DateField(auto_now_add=True)

    description_rus = models.TextField(blank=True, null=True,
                                   verbose_name='Краткая информация на русском о видео, напр., об авторе')
    description_eng = models.TextField(blank=True, null=True,
                                       verbose_name='Краткая информация на английском о видео, напр., об авторе')
    video = models.FileField(upload_to='videos', blank=True, null=True, verbose_name='Файл видео-клипа')
    youtube_video = models.TextField(blank=True,
                                     verbose_name='Для вставки видео с YouTube - альтернатива загрузке файла видео')

    additional_text_rus = models.TextField(blank=True,
                                       verbose_name='Текст на русском под видео, напр., ссылка на другое видео')
    additional_text_eng = models.TextField(blank=True,
                                           verbose_name='Текст на англ. под видео, напр., ссылка на другое видео')

    def __str__(self):
        return self.title_rus

    def get_absolute_url(self):
        return reverse('articles:video_id', args=[str(self.id)])

    def get_absolute_url_eng(self):
        return reverse('main:video_id', args=[str(self.id)])


class EditorArticle(models.Model):

    '''Статья главного редактора'''

    class Meta():
        verbose_name = 'Статья главного редактора'
        verbose_name_plural = 'Статьи главного редактора'

    title = models.CharField(max_length=100, unique=True, verbose_name='Название статьи')  # название статьи

    date = models.DateField(auto_now_add=True, null=True)  # дата создания статьи

    text = models.TextField(blank=True, verbose_name='Основной текст статьи')  # текст основной информации о событии (правила, участники и т.д.)

    image_poster_logo = models.ImageField(upload_to='photo', blank=True,
                                          verbose_name='Основное фото для статьи')  # изображение (постер или логотип организации);
                                                                        # расположен слева

    image1 = models.ImageField(upload_to='photo', blank=True,
                               verbose_name='Другие фото: Фото 1 для статьи гл. редактора, все доп фото одинаковой высоты')  # другие фото, не более двух
    image2 = models.ImageField(upload_to='photo', blank=True, verbose_name='Фото 2 для статьи гл. редактора')

    additional_text = models.TextField(blank=True, null=True,
                                       verbose_name='Текст в конце статьи, напр., ссылка на другую статью')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('articles:editor_id', args=[str(self.id)])


class Nonfiction(models.Model):

    class Meta():
        verbose_name = 'Публицистика'
        verbose_name_plural = 'Публицистика'

    title = models.CharField(max_length=100, unique=True, verbose_name='Название статьи')  # название статьи

    date = models.DateField(auto_now_add=True, null=True)  # дата создания статьи

    text = models.TextField(blank=True,
                            verbose_name='Основной текст статьи')  # текст основной информации о событии (правила, участники и т.д.)

    image_poster_logo = models.ImageField(upload_to='photo', blank=True,
                                          verbose_name='Основное фото для статьи')  # изображение (постер или логотип организации);
                                                                                    # расположен слева

    image1 = models.ImageField(upload_to='photo', blank=True,
                               verbose_name='Другие фото: Фото 1 для публицистики')  # другие фото, не более двух
    image2 = models.ImageField(upload_to='photo', blank=True, verbose_name='Фото 2 для публицистики')

    additional_text = models.TextField(blank=True, null=True,
                                       verbose_name='Текст в конце статьи, напр., ссылка на другую статью')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('articles:nonfiction', args=[str(self.id)])


class MainPageArticle(models.Model):

    class Meta():
        verbose_name = 'Первое место на главной (может отсутствовать)'
        verbose_name_plural = 'Первое место на главной (может отсутствовать)'

    editor = models.ForeignKey(EditorArticle, on_delete=models.DO_NOTHING, blank=True, null=True,
                                      verbose_name='Статья главного редактора')
    nonfiction = models.ForeignKey(Nonfiction, on_delete=models.DO_NOTHING, blank=True, null=True,
                               verbose_name='Публицистика')
    album = models.ForeignKey(PhotoAlbum, on_delete=models.DO_NOTHING, blank=True, null=True,
                                      verbose_name='Фотоальбом')
    video = models.ForeignKey(Video, on_delete=models.DO_NOTHING, blank=True, null=True,
                              verbose_name='Видео')

    def __str__(self):
        return 'Первое место на главной'