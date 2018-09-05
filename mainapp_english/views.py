#coding=utf-8
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import EditorArticleEng, MainPageArticleEng  # , ArticleEng
from mainapp.models import Article, ArticleCategory, Country, PhotoAlbum, Video
from commentapp.forms import CommentForm
from commentapp.models import Comment
from django.db.models import Q
from django.views import View


def articles_eng(request, pk=None, id=None):

    article_item_all = Article.objects.all().order_by('-id')
    number_of_articles = len(article_item_all)
    article_item = article_item_all[:101]
    types = ArticleCategory.objects.all()
    countries = []
    show_all = ''
    show_competitions = ''
    show_sport_camps = ''
    show_sport_science = ''
    show_editor = ''
    article_type = {}

    if pk:

        if pk == '0':
            article_type = {'type_rus': 'все', 'pk':0}
            article_item = Article.objects.all().order_by('-id')[:101]
            show_all = 'Show the rest articles'

        elif pk == '1':
            article_item = Article.objects.filter(type__id=pk).order_by('-date_start')[:101]
            article_type = get_object_or_404(ArticleCategory, pk=pk)
            countries = Country.objects.all().order_by('name_eng')
            show_competitions = 'Show the rest competitions'
            if id:
                article_item = Article.objects.filter(country__id=id).order_by('-date_start')[:31]
                return render(request, 'mainapp_english/main_eng.html',
                              {'article_item': article_item, 'article_type': article_type, 'types': types,
                               'countries': countries})

        elif pk == '2':
            article_item = Article.objects.filter(type__id=pk).order_by('-date_start')[:51]
            article_type = get_object_or_404(ArticleCategory, pk=pk)
            show_sport_camps = 'Show the rest camps'

        elif pk == '3':
            article_item = Article.objects.filter(type__id=pk).order_by('-id')[:31]
            article_type = get_object_or_404(ArticleCategory, pk=pk)
            show_sport_science = 'Show the rest articles'

        elif pk == '4':
            #article_item = ArticleEng.objects.filter(type__id=pk).order_by('-id')[:31]
            article_item = EditorArticleEng.objects.all().order_by('-id')[:31]
            article_type = get_object_or_404(ArticleCategory, pk=pk)
            show_editor = 'Show the rest articles'

        return render(request, 'mainapp_english/main_eng.html', {'number_of_articles': number_of_articles,
                                                     'article_item': article_item, 'article_type': article_type,
                                                        'types': types, 'countries': countries, 'show_all': show_all,
                                                        'show_competitions': show_competitions,
                                                        'show_sport_camps': show_sport_camps,
                                                        'show_sport_science': show_sport_science,
                                                        'show_editor': show_editor})

    show_all = 'Show the rest articles'

    if len(MainPageArticleEng.objects.all()) > 0:
        main_page_article = MainPageArticleEng.objects.all().order_by('-id')[0]
    else:
        main_page_article = ''

    return render(request, 'mainapp_english/main_eng.html', {'number_of_articles': number_of_articles, 'article_item': article_item,
                                                 'types': types, 'show_all': show_all,
                                                             'main_page_article': main_page_article})


def show_all_view_eng(request):
    art = Article.objects.all().order_by('-id')[101:]
    return render(request, 'mainapp_english/show_all_eng.html', {'articles': art})


def show_competitions_view_eng(request):
    art = Article.objects.filter(type__id=1).order_by('-date_start')[101:]
    return render(request, 'mainapp_english/show_competitions_eng.html', {'articles': art})


def show_sport_camps_view_eng(request):
    art = Article.objects.filter(type__id=2).order_by('-date_start')[51:]
    return render(request, 'mainapp_english/show_sport_camps_eng.html', {'articles': art})


def show_sport_science_view_eng(request):
    art = Article.objects.filter(type__id=3).order_by('-id')[31:]
    return render(request, 'mainapp_english/show_sport_science_eng.html', {'articles': art})


def show_editor_view_eng(request):
    art = Article.objects.filter(type__id=4).order_by('-id')[31:]
    return render(request, 'mainapp_english/show_editor_eng.html', {'articles': art})


def show_photo_view_eng(request):
    photo = PhotoAlbum.objects.all().order_by('-id')[31:]
    return render(request, 'mainapp_english/show_photo_eng.html', {'photo': photo})


def show_video_view_eng(request):
    video = Video.objects.all().order_by('-id')[31:]
    return render(request, 'mainapp_english/show_video_eng.html', {'video': video})


# def show_editor_view_eng(request):
#     editors = EditorArticleEng.objects.all().order_by('-id')[31:]
#     return render(request, 'mainapp_english/show_editors_eng.html', {'editors': editors})


def shotokan_eng(request):
    return render(request, 'mainapp_english/styles/shotokan_eng.html')


def shito_eng(request):
    return render(request, 'mainapp_english/styles/shito_eng.html')


def goju_eng(request):
    return render(request, 'mainapp_english/styles/goju_eng.html')


def wado_eng(request):
    return render(request, 'mainapp_english/styles/wado_eng.html')


def gallery_photo_eng(request):

    number_of_albums = len(PhotoAlbum.objects.all().order_by('-id'))
    gallery_item = PhotoAlbum.objects.all().order_by('-id')[:31]

    return render(request, 'mainapp_english/photo_eng.html', {'number_of_albums': number_of_albums, 'gallery_item': gallery_item})


def gallery_video_eng(request):

    number_of_videos = len(Video.objects.all().order_by('-id'))
    video_item = Video.objects.all().order_by('-id')[:31]

    return render(request, 'mainapp_english/video_eng.html', {'number_of_videos':number_of_videos, 'video_item': video_item})


# def editor_in_chief_eng(request):
#
#     number_of_editors = len(EditorArticleEng.objects.all().order_by('-id'))
#     editor_item = EditorArticleEng.objects.all().order_by('-id')[:31]
#
#     return render(request, 'mainapp_english/editor_in_chief_eng.html', {'number_of_editors': number_of_editors,
#                                                             'editor_item': editor_item})


class SearchViewEng(View):

    template_name = 'mainapp_english/search_eng.html'

    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('q')
        found_articles = Article.objects.filter(Q(title_eng__icontains=query)|Q(text_eng__icontains=query)|
                                                Q(title_eng__icontains=query.title())|
                                                Q(text_eng__icontains=query.title())|Q(city_description_eng__icontains=query)|
                                                 Q(city_description_eng__icontains=query.title())).order_by('-id')
        found_albums = PhotoAlbum.objects.filter(Q(title_eng__icontains=query)|
                                                 Q(title_eng__icontains=query.title())).order_by('-id')
        found_videos = Video.objects.filter(Q(title_eng__icontains=query) |
                                                 Q(title_eng__icontains=query.title())|Q(description_eng__icontains=query)|
                                                 Q(description_eng__icontains=query.title())).order_by('-id')
        found_editors = EditorArticleEng.objects.filter(Q(title__icontains=query) |
                                            Q(title__icontains=query.title())|Q(text__icontains=query) |
                                            Q(text__icontains=query.title())).order_by('-id')

        context = {'found_articles': found_articles, 'found_albums': found_albums,
                   'found_videos': found_videos, 'found_editors': found_editors}

        return render(self.request, self.template_name, context)

#-------------------------article_i_eng-----------------------------


def article_eng(request, pk=None):

    art = get_object_or_404(Article, pk=pk)
    comment = Comment.objects.filter(article_id=art).order_by('id')

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            comm = comment_form.save(commit=False)
            comm.author_id = request.user
            comm.article_id = art
            if request.user.avatar:
                comm.avatar = request.user.avatar.url
            comm.save()
            return HttpResponseRedirect('')

    else:
        comment_form = CommentForm()

    return render(request, 'mainapp_english/articles/article_{}_eng.html'.format(pk),
                  {'article': art, 'comment_form': comment_form, 'comment': comment})


#-------------------------photo_i-----------------------------


def photo_album(request, pk=None):

    photo = get_object_or_404(PhotoAlbum, pk=pk)
    comment = Comment.objects.filter(photo_album_id=photo).order_by('id')

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            comm = comment_form.save(commit=False)
            comm.author_id = request.user
            comm.photo_album_id = photo
            if request.user.avatar:
                comm.avatar = request.user.avatar.url
            comm.save()
            return HttpResponseRedirect('')

    else:
        comment_form = CommentForm()

    return render(request, 'mainapp_english/gallery_albums/photo_{}.html'.format(pk),
                  {'photo': photo, 'comment_form': comment_form, 'comment': comment})


#-------------------------video_i-----------------------------


def video_album(request, pk=None):

    video = get_object_or_404(Video, pk=pk)
    comment = Comment.objects.filter(video_id=video).order_by('id')

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            comm = comment_form.save(commit=False)
            comm.author_id = request.user
            comm.video_id = video
            if request.user.avatar:
                comm.avatar = request.user.avatar.url
            comm.save()
            return HttpResponseRedirect('')

    else:
        comment_form = CommentForm()

    return render(request, 'mainapp_english/gallery_videos/video_{}.html'.format(pk),
                  {'video': video, 'comment_form': comment_form, 'comment': comment})


#-------------------------editor_i_eng-----------------------------


def editor_article_eng(request, pk=None):

    editor = get_object_or_404(EditorArticleEng, pk=pk)
    comment = Comment.objects.filter(editor_eng_id=editor).order_by('id')

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            comm = comment_form.save(commit=False)
            comm.author_id = request.user
            comm.editor_eng_id = editor
            if request.user.avatar:
                comm.avatar = request.user.avatar.url
            comm.save()
            return HttpResponseRedirect('')

    else:
        comment_form = CommentForm()

    return render(request, 'mainapp_english/editor_articles/editor_{}_eng.html'.format(pk),
                  {'editor': editor, 'comment_form': comment_form, 'comment': comment})