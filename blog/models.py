from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    title = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateTimeField()
    author = models.ForeignKey(User, null=True, blank=True)

    def __str__(self):
        return self.title
