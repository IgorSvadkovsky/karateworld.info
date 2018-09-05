from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):

    class Meta():

        model = Comment
        fields = ('comment',)

        widgets = {
            'comment': forms.Textarea(attrs={'placeholder': 'Type your comment here'})
        }

    #def __init__(self, *args, **kwargs):

        #super(CommentForm, self).__init__(*args, **kwargs)
        #for field_name, field in self.fields.items():
            #pass
            ##field.widjet.attrs['class'] = 'form_control'