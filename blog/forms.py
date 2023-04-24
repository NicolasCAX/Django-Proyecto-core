from django import forms
from .models import Post

class PostCretaForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=("title", "content")
