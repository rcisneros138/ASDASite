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


class PreDentalSignUp(models.Model):
    name = models.CharField(max_length=140)
    Phone = models.CharField(max_length=30)
    Address1 = models.CharField(max_length=140)
    Address2 = models.CharField(max_length=140)
    Email = models.CharField(max_length=70)
    Gender = models.CharField(max_length=20)
    BirthDate = models.CharField(max_length=20)

    School = models.CharField(max_length=140)
    Year = models.CharField(max_length=140)

    EmergName = models.CharField(max_length=140)
    EmergPhone = models.CharField(max_length=30)
    EmergEmail = models.CharField(max_length=70)

    SocialEvent = models.CharField(max_length=10)
    DietaryNeeds = models.CharField(max_length=200)
    NeedHotel = models.BooleanField(default=False)

    Verified = models.BooleanField(default=False)

    def __str__(self):
        return self.name
