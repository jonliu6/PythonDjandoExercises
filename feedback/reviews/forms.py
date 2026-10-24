from django import forms
from .models import Review
# class ReviewForm(forms.Form):
#     user_name = forms.CharField(label="Your Name", max_length=100, required=True, error_messages={
#         'required': 'Please enter your name.',
#         'max_length': 'Your name is too long.'
#         })
#     review_text = forms.CharField(label="Your Review", widget=forms.Textarea, required=True, error_messages={
#         'required': 'Please enter your review.',
#         'max_length': 'Your review is too long.'
#         })
#     rating = forms.IntegerField(label="Rating (1-5)", min_value=1, max_value=5)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['user_name', 'review_text', 'rating']
        # fields = '__all__'
        # exclude = ['owner_comments']
        labels = {
            'user_name': 'Your Name',
            'review_text': 'Your Review',
            'rating': 'Rating (1-5)',
        }
        error_messages = {
            'user_name': {
                'required': 'Please enter your name.',
                'max_length': 'Your name is too long.'
            },
            'review_text': {
                'required': 'Please enter your review.',
                'max_length': 'Your review is too long.'
            },
            'rating': {
                'min_value': 'Rating must be at least 1.',
                'max_value': 'Rating cannot be more than 5.'
            }
        }