from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class BlogPost(models.Model):
    title = models.CharField(max_length=140)
    body = RichTextUploadingField()
    date = models.DateTimeField()
    author = models.ForeignKey(User, null=True, blank=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def approve(self):
        self.approved = True
        self.save()
