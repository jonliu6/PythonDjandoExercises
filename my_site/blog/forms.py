from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['user_name', 'user_email', 'text']
        labels = {
            'user_name': 'Your Name',
            'user_email': 'Your Email',
            'text': 'Your Comment',
        }
        # exclude = ['post']  # Exclude the 'post' field since it will be set in the view