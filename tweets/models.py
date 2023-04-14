from django.db import models
from django.contrib.auth.models import User


class Tweet(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.FileField(upload_to='images/', blank=True, null=True)
    text = models.CharField(max_length=280, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']

    def serialize(self):
        return {
            "id": self.id,
            "content": self.text,
            "likes": 0
        }