from django import forms
from .models import Todo
from django.utils.translation import ugettext_lazy as _


class TodoPost(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['content', ]
        widgets = {
            'content': forms.TextInput(attrs={'placeholder': 'what to do'}),
        }
        labels = {
            'content': _('할 일 '),
        }
