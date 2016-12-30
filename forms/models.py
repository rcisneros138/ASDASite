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


class Signup(models.Model):
    firstName = models.CharField(max_length=140, null=True, blank=True)
    lastName = models.CharField(max_length=120, null=True, blank=True)
    email = models.EmailField()
    timeStamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return smart_text(self.email)


class ContactInformation(models.Model):
    firstName = models.CharField("First Name", max_length=140, null=True, blank=True)
    lastName = models.CharField("Last Name", max_length=140, null=True, blank=True)
    contactNumber = models.CharField("Contact Number", max_length=140, null=True, blank=True)
    email = email = models.EmailField("Email")

    def __str__(self):
        return self.firstName


class UsLocation(models.Model):
    addressLine1 = models.CharField("Address line 1", max_length=45)
    addressLine2 = models.CharField("address line 2", max_length=45, blank=True)
    postalCode = models.CharField("Postal Code", max_length=10)
    city = models.CharField("City", max_length=50, blank=False)
    state = models.CharField("State", max_length=40, blank=True)
    country = models.CharField("Country", max_length=40, blank=False)

    def __str__(self):
        return self.city


class PreDentalWeekendSignup(models.Model):
    applicantContactInfo = models.ForeignKey(
                                            "ContactInformation",
                                            on_delete=models.CASCADE,
                                            related_name='applicantContactInfo'
                                            , null=True)
    ApplicantAddress = models.ForeignKey("UsLocation", on_delete=models.CASCADE,
                                         related_name='ApplicantAddress',
                                         null=True)
    emergencyContactInfo = models.ForeignKey(
                                            "ContactInformation",
                                            on_delete=models.CASCADE,
                                            related_name='emergencyContactName'
                                            , null=True)
    school = models.CharField("school", max_length=140, null=True, blank=True)
    needsHotelRoom = models.BooleanField("Needs Hotel", default=False)
    timeStamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return str(self.ApplicantAddress)
