from django import forms
from .models import TODO

class Todoform(forms.ModelForm):
    class Meta:
        model=TODO
        fields=['title',]
        widgets={
            'title': forms.TextInput(attrs={'placeholder': '내용을 입력하세요'})
        }