#coding=utf-8
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import ArticleCategory, Country, Article, PhotoAlbum, Video, EditorArticle, Nonfiction, MainPageArticle
from commentapp.forms import CommentForm
from commentapp.models import Comment
from django.db.models import Q
from django.views import View


def articles(request, pk=None, id=None):

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
    show_nonfiction = ''
    article_type = {}

    if pk:

        if pk == '0':
            article_type = {'type_rus': 'все', 'pk':0}
            article_item = Article.objects.all().order_by('-id')[:101]
            show_all = 'Показать остальные статьи'

        elif pk == '1':
            article_item = Article.objects.filter(type__id=pk).order_by('-date_start')[:101]
            article_type = get_object_or_404(ArticleCategory, pk=pk)
            countries = Country.objects.all().order_by('name_rus')
            show_competitions = 'Показать остальные соревнования'
            if id:
                article_item = Article.objects.filter(country__id=id).order_by('-date_start')[:31]
                return render(request, 'mainapp/main.html',
                              {'article_item': article_item, 'article_type': article_type, 'types': types,
                               'countries': countries})

        elif pk == '2':
            article_item = Article.objects.filter(type__id=pk).order_by('-date_start')[:51]
            article_type = get_object_or_404(ArticleCategory, pk=pk)
            show_sport_camps = 'Показать остальные лагеря'

        elif pk == '3':
            article_item = Article.objects.filter(type__id=pk).order_by('-id')[:31]
            article_type = get_object_or_404(ArticleCategory, pk=pk)
            show_sport_science = 'Показать остальные статьи'

        elif pk == '4':
            #article_item = Article.objects.filter(type__id=pk).order_by('-id')[:31]
            article_item = EditorArticle.objects.all().order_by('-id')[:31]
            article_type = get_object_or_404(ArticleCategory, pk=pk)
            show_editor = 'Показать остальные статьи'

        elif pk == 'nonfiction':
            article_item = Nonfiction.objects.all().order_by('-id')[:31]
            #article_type = get_object_or_404(ArticleCategory, pk=pk)
            show_nonfiction = 'Показать остальные статьи'

        return render(request, 'mainapp/main.html', {'number_of_articles': number_of_articles,
                                                     'article_item': article_item, 'article_type': article_type,
                                                        'types': types, 'countries': countries, 'show_all': show_all,
                                                        'show_competitions': show_competitions,
                                                        'show_sport_camps': show_sport_camps,
                                                        'show_sport_science': show_sport_science,
                                                        'show_editor': show_editor, 'show_nonfiction': show_nonfiction})

    show_all = 'Показать остальные статьи'

    if len(MainPageArticle.objects.all()) > 0:
        main_page_article = MainPageArticle.objects.all().order_by('-id')[0]
    else:
        main_page_article = ''

    return render(request, 'mainapp/main.html', {'number_of_articles': number_of_articles, 'article_item': article_item,
                                                 'types': types, 'show_all': show_all,
                                                 'main_page_article': main_page_article})


def show_all_view(request):
    art = Article.objects.all().order_by('-id')[101:]
    return render(request, 'mainapp/show_all.html', {'articles': art})


def show_competitions_view(request):
    art = Article.objects.filter(type__id=1).order_by('-date_start')[101:]
    return render(request, 'mainapp/show_competitions.html', {'articles': art})


def show_sport_camps_view(request):
    art = Article.objects.filter(type__id=2).order_by('-date_start')[51:]
    return render(request, 'mainapp/show_sport_camps.html', {'articles': art})


def show_sport_science_view(request):
    art = Article.objects.filter(type__id=3).order_by('-id')[31:]
    return render(request, 'mainapp/show_sport_science.html', {'articles': art})


def show_editor_view(request):
    art = Article.objects.filter(type__id=4).order_by('-id')[31:]
    return render(request, 'mainapp/show_editor.html', {'articles': art})


def show_nonfiction_view(request):
    art = Nonfiction.objects.all().order_by('-id')[31:]
    return render(request, 'mainapp/show_nonfiction.html', {'articles': art})


def show_photo_view(request):
    photo = PhotoAlbum.objects.all().order_by('-id')[31:]
    return render(request, 'mainapp/show_photo.html', {'photo': photo})


def show_video_view(request):
    video = Video.objects.all().order_by('-id')[31:]
    return render(request, 'mainapp/show_video.html', {'video': video})


# def show_editor_view(request):
#     editors = EditorArticle.objects.all().order_by('-id')[31:]
#     return render(request, 'mainapp/show_editors.html', {'editors': editors})


def shotokan(request):
    return render(request, 'mainapp/styles/shotokan.html')


def shito(request):
    return render(request, 'mainapp/styles/shito.html')


def goju(request):
    return render(request, 'mainapp/styles/goju.html')


def wado(request):
    return render(request, 'mainapp/styles/wado.html')


def gallery_photo(request):

    number_of_albums = len(PhotoAlbum.objects.all().order_by('-id'))
    gallery_item = PhotoAlbum.objects.all().order_by('-id')[:31]

    return render(request, 'mainapp/photo.html', {'number_of_albums': number_of_albums, 'gallery_item': gallery_item})


def gallery_video(request):

    number_of_videos = len(Video.objects.all().order_by('-id'))
    video_item = Video.objects.all().order_by('-id')[:31]

    return render(request, 'mainapp/video.html', {'number_of_videos':number_of_videos, 'video_item': video_item})


# def editor_in_chief(request):
#
#     number_of_editors = len(EditorArticle.objects.all().order_by('-id'))
#     editor_item = EditorArticle.objects.all().order_by('-id')[:31]
#
#     return render(request, 'mainapp/editor_in_chief.html', {'number_of_editors': number_of_editors,
#                                                             'editor_item': editor_item})


class SearchView(View):

    template_name = 'mainapp/search.html'

    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('q')
        found_articles = Article.objects.filter(Q(title__icontains=query)|Q(text__icontains=query)|
                                                Q(title__icontains=query.title())|
                                                Q(text__icontains=query.title())|Q(city_description__icontains=query)|
                                                 Q(city_description__icontains=query.title())).order_by('-id')
        found_albums = PhotoAlbum.objects.filter(Q(title_rus__icontains=query)|
                                                 Q(title_rus__icontains=query.title())).order_by('-id')
        found_videos = Video.objects.filter(Q(title_rus__icontains=query) |
                                                 Q(title_rus__icontains=query.title())|Q(description_rus__icontains=query)|
                                                 Q(description_rus__icontains=query.title())).order_by('-id')
        found_editors = EditorArticle.objects.filter(Q(title__icontains=query) |
                                            Q(title__icontains=query.title())|Q(text__icontains=query) |
                                            Q(text__icontains=query.title())).order_by('-id')
        found_nonfiction = Nonfiction.objects.filter(Q(title__icontains=query) |
                                                     Q(title__icontains=query.title()) | Q(text__icontains=query) |
                                                     Q(text__icontains=query.title())).order_by('-id')

        context = {'found_articles': found_articles, 'found_albums': found_albums,
                   'found_videos': found_videos, 'found_editors': found_editors, 'found_nonfiction': found_nonfiction}

        return render(self.request, self.template_name, context)

#def search(request):
#
#    query = request.GET.get('q')
#    found_articles = Article.objects.filter(Q(title__icontains=query)|Q(text__icontains=query))
#
#    context = {'found_articles': found_articles}
#
#    return render(request, 'mainapp/search.html', context)

# -------------------------article_i-----------------------------


def article(request, pk=None):

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

    return render(request, 'mainapp/articles/article_{}.html'.format(pk), {'article': art, 'comment_form': comment_form,
                                                                  'comment': comment})


# -------------------------photo_i-----------------------------


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

    return render(request, 'mainapp/gallery_albums/photo_{}.html'.format(pk),
                  {'photo': photo, 'comment_form': comment_form, 'comment': comment})


# -------------------------video_i-----------------------------


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

    return render(request, 'mainapp/gallery_videos/video_{}.html'.format(pk),
                  {'video': video, 'comment_form': comment_form, 'comment': comment})


# -------------------------editor_i-----------------------------


def editor_article(request, pk=None):

    editor = get_object_or_404(EditorArticle, pk=pk)
    comment = Comment.objects.filter(editor_id=editor).order_by('id')

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            comm = comment_form.save(commit=False)
            comm.author_id = request.user
            comm.editor_id = editor
            if request.user.avatar:
                comm.avatar = request.user.avatar.url
            comm.save()
            return HttpResponseRedirect('')

    else:
        comment_form = CommentForm()

    return render(request, 'mainapp/editor_articles/editor_{}.html'.format(pk),
                  {'editor': editor, 'comment_form': comment_form, 'comment': comment})


# -------------------------nonfiction_i-----------------------------


def nonfiction_article(request, pk=None):  # Использует шаблон editor_i.html, поэтому название "editor" сохранено

    editor = get_object_or_404(Nonfiction, pk=pk)
    comment = Comment.objects.filter(nonfiction_id=editor)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            comm = comment_form.save(commit=False)
            comm.author_id = request.user
            comm.nonfiction_id = editor
            if request.user.avatar:
                comm.avatar = request.user.avatar.url
            comm.save()
            return HttpResponseRedirect('')

    else:
        comment_form = CommentForm()

    return render(request, 'mainapp/nonfiction/editor_{}.html'.format(pk),
                  {'editor': editor, 'comment_form': comment_form, 'comment': comment})