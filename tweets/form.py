from django import forms
from django.conf import settings
from .models import Tweet


class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text']

    def clean_content(self):
        content = self.cleaned_data.get("text")
        if len(content) > settings.MAX_TWEET_LENGTH:
            raise forms.ValidationError("This tweet is too long")
        return content
