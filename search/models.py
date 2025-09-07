from django.db import models
from django.contrib.auth.models import User


class ParagraphSubmission(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="submissions"
    )
    paragraph = models.TextField()
    word_freq_index = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)
