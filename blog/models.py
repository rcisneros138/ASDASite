from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager


class BlogPost(models.Model):
    title = models.CharField(max_length=140)
    body = RichTextUploadingField()
    date = models.DateTimeField()
    author = models.ForeignKey(User, null=True, blank=True)
    approved = models.BooleanField(default=False)
    tags = TaggableManager()
    headerImage = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title

    def approve(self):
        self.approved = True
        self.save()


class BlogImage(models.Model):
    blogPost = models.ForeignKey(BlogPost, related_name='blogImages')
    Image = models.ImageField()


