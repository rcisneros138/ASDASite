from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.core.validators import URLValidator
from taggit.managers import TaggableManager
from taggit.models import Tag


def tag_helptext():
    help_text = "Options: "
    for tag in Tag.objects.all():
        help_text += tag.name + " ||| "
    return help_text


class BlogPost(models.Model):
    title = models.CharField(max_length=140)
    body = RichTextField()
    date = models.DateTimeField()
    author = models.ForeignKey(User, null=True, blank=True)
    approved = models.BooleanField(default=False)
    tags = TaggableManager(blank=True, help_text=tag_helptext())
    headerImage = models.ImageField(null=True, blank=True)
    videoUrlLink = models.CharField(null=True, blank=True, max_length=2000,
                                    validators=[URLValidator()])

    def __str__(self):
        return self.title

    def approve(self):
        self.approved = True
        self.save()


class BlogImage(models.Model):
    blogPost = models.ForeignKey(BlogPost, related_name='blogImages')
    Image = models.ImageField()
