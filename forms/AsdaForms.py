from django import forms
from django.forms import TextInput
from django.forms import inlineformset_factory
from .models import Signup, PreDentalWeekendSignup, ContactInformation


class signupForm(forms.ModelForm):
    class Meta:
        model = Signup
        fields = ('firstName', 'lastName', 'email')


class ContactInformationForm(forms.ModelForm):
    class Meta:
        model = ContactInformation
        fields = ('firstName', 'lastName', 'contactNumber', 'email')
        widgets = {
            'firstName': TextInput(attrs={'placeholder': 'First Name'}),
            'lastName': TextInput(attrs={'placeholder': 'Last Name'}),
            'contactNumber': TextInput(attrs={'placeholder': 'Phone'}),
            'email': TextInput(attrs={'placeholder': 'Email'}),
        }


class PreDentalWeekendSignupForm(forms.ModelForm):
    class Meta:
        model = PreDentalWeekendSignup
        fields = (
                'school',
                'needsHotelRoom')


signupInLineFormSet = inlineformset_factory(ContactInformation,
                                            PreDentalWeekendSignup,
                                            fk_name="applicantContactInfo",
                                            fields=('school',
                                                    'needsHotelRoom'),
                                            extra=1,
                                            can_delete=False)
