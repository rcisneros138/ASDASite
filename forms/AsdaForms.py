from django import forms
from .models import contactUs
from paypal.standard.forms import PayPalPaymentsForm



class ContactUsForm(forms.ModelForm):
    class Meta:
        model = contactUs
        widgets = {
          'message': forms.Textarea(attrs={'rows':4, 'cols':15}),
        }
        fields = ('name', 'email', 'subject', 'message')

Gender_Choices = (
    ('male', 'Male'),
    ('female', 'Female')
)
paypal_dict = {
    "business": "rcisneros138@gmail.com",
    "amount": "10.00",
    "item_name": "Pre-Dental Weekend",
    "invoice": "unique-invoice-id",
    "notify_url": "https://www.example.com" + ('paypal-ipn'),
    "return_url": "https://www.example.com/your-return-location/",
    "cancel_return": "https://www.example.com/your-cancel-location/",
    "custom": "preDentalWeekendgit "
}

class PaymentForm(PayPalPaymentsForm):
    initial_dict = paypal_dict

class PreDentalForm1(forms.Form):
    FirstName = forms.CharField(max_length=50)
    LastName = forms.CharField(max_length=100)
    PhoneNumber = forms.CharField(max_length=50)
    Gender = forms.MultipleChoiceField(
        required=True,
        widget=forms.CheckboxSelectMultiple,
        choices=Gender_Choices,
    )
    BirthDate = forms.DateField()
    Address1 = forms.CharField(label='Street Address', max_length=100)
    Address2 = forms.CharField(label='apartment/suite', max_length=100)
    City = forms.CharField(label='City', max_length=100)
    ZipCode = forms.CharField(label='Zip', max_length=100)


class PreDentalForm2(forms.Form):
    DietaryRestrictions = forms.CharField(max_length=100)
    AffiliateSchool = forms.CharField(max_length=100)
    NeedsHotel = forms.BooleanField()
    AdditionalInfo = forms.CharField(widget=forms.Textarea)
