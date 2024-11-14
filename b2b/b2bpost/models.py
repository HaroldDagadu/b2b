from django.db import models
from django.conf import settings

from accounts.models import Profile 
class B2BPost(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="b2b_posts")  # Link to the User who created the post
    content = models.TextField(max_length=200)
    facts = models.IntegerField(default=0)  # Represents "likes"
    nah_bro = models.IntegerField(default=0, blank=True)  # Represents "dislikes"
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:50]  # Display first 50 characters for readability
