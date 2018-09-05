from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from .models import KarateworldUser


class KarateworldLoginForm(AuthenticationForm):

    class Meta:

        model = KarateworldUser
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):

        super(KarateworldLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            pass
            #field.widjet.attrs['class'] = 'form_control'


class KarateworldRegisterForm(UserCreationForm):

    class Meta:

        model = KarateworldUser
        fields = ('username', 'password1', 'password2', 'email', 'avatar')

    def __init__(self, *args, **kwargs):

        super(KarateworldRegisterForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            pass
            #field.widget.attrs['class'] = 'form_control'
            #field.help_text = ''


class KarateworldEditForm(UserChangeForm):

    class Meta:

        model = KarateworldUser
        fields = ('username', 'password', 'email', 'avatar')

    def __init__(self, *args, **kwargs):

        super(KarateworldEditForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            pass
            #field.widget.attrs['class'] = 'form_control'
            #field.help_text = ''
            if field_name == 'password':
                field.widget = forms.HiddenInput()
                #pass