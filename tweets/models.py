from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL


class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # id = models.AutoField(primary_key=True)
    image = models.FileField(upload_to='images/', blank=True, null=True)
    text = models.CharField(max_length=280, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['-id']

    def serialize(self):
        return {
            "id": self.id,
            "content": self.text,
            "likes": 0
        }
