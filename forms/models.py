from django.db import models
from django.utils.encoding import smart_text


class contactUs(models.Model):
    name = models.CharField(max_length=140, null=True, blank=True)
    email = models.EmailField()
    subject = models.CharField(max_length=140, null=True, blank=True)
    message = models.TextField()

    class Meta:
        verbose_name = 'Contact Request'
        verbose_name_plural = 'Contact Requests'

    def __str__(self):
        return self.email
