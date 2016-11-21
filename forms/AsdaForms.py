from django import forms
from .models import Signup, PreDentalWeekendSignup, ContactInformation


class signupForm(forms.ModelForm):
    class Meta:
        model = Signup
        fields = ('firstName', 'lastName', 'email')


class ContactInformationForm(forms.ModelForm):
    class Meta:
        model = ContactInformation
        fields = ('firstName', 'lastName', 'contactNumber', 'email')


class PreDentalWeekendSignupForm(forms.ModelForm):
    class Meta:
        model = PreDentalWeekendSignup
        fields = (
                'school',
                'needsHotelRoom')
