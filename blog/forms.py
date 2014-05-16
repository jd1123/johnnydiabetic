from django import forms
from blog.models import BlogPost

class BlogPostForm(forms.ModelForm):
    title = forms.CharField(max_length=120)
    body = forms.Textarea()
    
    class Meta:
        model = BlogPost
        fields = ('title', 'body')