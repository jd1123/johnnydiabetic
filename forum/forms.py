from django import forms
from forum.models import Forum, Thread, Post
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    subject = forms.CharField(max_length=120, help_text='Subject')
    body = forms.CharField(widget=forms.Textarea)
    
    class Meta:
        model = Post
        fields = ('subject', 'body')