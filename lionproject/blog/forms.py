from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta: 
        # blog 모델에 fields를 연결시켜주겠다. = 이 정보를 가지고 blog form을 만들어주겠다.
        model = Blog
        fields = ['title', 'writer', 'body', 'image']
