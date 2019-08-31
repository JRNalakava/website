from django import forms

from rush.models import RushComment
from . import models


class RusheeForm(forms.ModelForm):
    class Meta:
        model = models.Rushee
        labels = {'first_name': 'First Name',
                  'last_name': 'Last Name',
                  'email': 'E-mail',
                  'phone_num': 'Phone Number',
                  'image': 'Profile Picture'}
        fields = ['first_name', 'last_name', 'email', 'phone_num', 'college_year_selection', 'image']


class LoginForm(forms.Form):
    username = forms.CharField(help_text='Username received after starting the rush application', max_length=15,
                               required=True)

    class Meta:
        labels = {'username': 'Username'}


class CommentForm(forms.ModelForm):
    class Meta:
        model = RushComment
        exclude = ['author', 'rushee']
        labels = {'comment_text': 'Comment'}
