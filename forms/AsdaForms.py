from django import forms
from .models import contactUs


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = contactUs
        widgets = {
          'message': forms.Textarea(attrs={'rows':4, 'cols':15}),
        }
        fields = ('name', 'email', 'subject', 'message')


# class PreDentalForm1(forms.Form):
#     FirstName = forms.CharField(max_length=50)
#     LastName = forms.CharField(max_length=100)
#     PhoneNumber = forms.CharField(max_length=50)
#     BirthDate = forms.DateField(widget=forms.extras.SelectDateWidget)
#     DietaryRestrictions = forms.CharField(max_length=100)
#     Address1 = forms.CharField(label='Street Address', max_length=100)
#     Address2 = forms.CharField(label='apartment/suite', max_length=100)
#     City = forms.CharField(label='City', max_length=100)
#     ZipCode = forms.CharField(label='Zip', max_length=100)
