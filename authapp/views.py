from django.shortcuts import render, HttpResponseRedirect
from authapp.forms import KarateworldLoginForm, KarateworldRegisterForm, KarateworldEditForm
from django.contrib import auth
from django.urls import reverse


def login(request):

    login_form = KarateworldLoginForm(data=request.POST or None)

    if request.method == 'POST' and login_form.is_valid():

        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user and user.is_active:

            auth.login(request, user)
            return HttpResponseRedirect(reverse('articles:main'))
            #return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    content = {'login_form': login_form}
    return render(request, 'authapp/login.html', content)


def logout(request):

    auth.logout(request)

    #try:
        #return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    #except:
    return HttpResponseRedirect(reverse('articles:main'))


def register(request):

    if request.method == 'POST':

        register_form = KarateworldRegisterForm(request.POST, request.FILES)

        if register_form.is_valid():

            register_form.save()
            return HttpResponseRedirect(reverse('auth:login'))

    else:

        register_form = KarateworldRegisterForm()

    content = {'register_form': register_form}
    return render(request, 'authapp/register.html', content)


def edit(request):

    if request.method == 'POST':

        edit_form = KarateworldEditForm(request.POST, request.FILES, instance=request.user)

        if edit_form.is_valid():

            edit_form.save()
            return HttpResponseRedirect(reverse('auth:edit'))

    else:

        edit_form = KarateworldEditForm(instance=request.user)

    content = {'edit_form': edit_form}

    return render(request, 'authapp/edit.html', content)


def login_eng(request):

    login_form = KarateworldLoginForm(data=request.POST or None)

    if request.method == 'POST' and login_form.is_valid():

        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user and user.is_active:

            auth.login(request, user)
            return HttpResponseRedirect(reverse('main:main'))
            #return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    content = {'login_form': login_form}
    return render(request, 'authapp/login_eng.html', content)


def logout_eng(request):

    auth.logout(request)

    return HttpResponseRedirect(reverse('main:main'))


def register_eng(request):

    if request.method == 'POST':

        register_form = KarateworldRegisterForm(request.POST, request.FILES)

        if register_form.is_valid():

            register_form.save()
            return HttpResponseRedirect(reverse('auth:login_eng'))

    else:

        register_form = KarateworldRegisterForm()

    content = {'register_form': register_form}
    return render(request, 'authapp/register_eng.html', content)


def edit_eng(request):

    if request.method == 'POST':

        edit_form = KarateworldEditForm(request.POST, request.FILES, instance=request.user)

        if edit_form.is_valid():

            edit_form.save()
            return HttpResponseRedirect(reverse('auth:edit_eng'))

    else:

        edit_form = KarateworldEditForm(instance=request.user)

    content = {'edit_form': edit_form}

    return render(request, 'authapp/edit_eng.html', content)

