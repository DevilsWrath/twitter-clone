from django.conf import settings
from rest_framework import serializers
from .models import Tweet


class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ['text']

    def validate_text(self, value):
        if len(value) > settings.MAX_TWEET_LENGTH:
            raise serializers.ValidationError("This tweet is too long")
        return value