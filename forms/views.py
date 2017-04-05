from .AsdaForms import ContactUsForm, PreDentalForm1, PreDentalForm2
from django.views.generic import FormView, CreateView, ListView
from blog.models import BlogPost, BlogImage
from formtools.wizard.views import SessionWizardView
from paypal.standard.forms import PayPalPaymentsForm
from django.http import HttpResponse, JsonResponse, StreamingHttpResponse

import json
from datetime import datetime
from forms.models import contactUs, PreDentalSignUp
import csv


class contactUsView(CreateView):
    form_class = ContactUsForm
    success_url = '/'
    template_name = "ASDAWebApp/Generic/smallFooter.html"

    def form_valid(self, form):
        return super(ContactUsForm, self).form_valid(form)


class PreDentalRegisterWizard(SessionWizardView):
    template_name = "forms/Register.html"
    form_list = PreDentalForm1, PreDentalForm2

    def done(self, form_list, **kwargs):
        print("worked")


class signUp(ListView):
    model = BlogPost
    template_name = "ASDAWebApp/Generic/signuppage.html"


def submitPredentalForm(request):
    form = PreDentalSignUp(
        name = str(request.POST.get('Name')),
        Phone = str(request.POST.get('Phone')),
        Address1 = str(request.POST.get('Address1')),
        Address2 = str(request.POST.get('Address2')),
        Email = str(request.POST.get('Email')),
        Gender = str(request.POST.get('Gender')),
        BirthDate = str(request.POST.get('BirthDate')),

        School = str(request.POST.get('School')),
        Year = str(request.POST.get('Year')),

        EmergName = str(request.POST.get('EmergName')),
        EmergPhone = str(request.POST.get('EmergPhone')),
        EmergEmail = str(request.POST.get('EmergEmail')),

        SocialEvent = str(request.POST.get('SocialEvent')),
        DietaryNeeds = str(request.POST.get('DietaryNeeds')),
        NeedHotel = str(request.POST.get('NeedHotel'))
    )

    # paypal = paypalform(
    #     cardHolderName = str(request.POST.get('cardHolderName')),
    #     cardNumber = str(request.POST.get('cardNumber')),
    #     expiryMonth = str(request.POST.get('expiryMonth')),
    #     expiryMonth = str(request.POST.get('expiryMonth')),
    #     cvv = str(request.POST.get('cvv'))
    # )

    # Handle the user save to the database first.
    response = {}
    try:
        if str(request.POST.get('Name')) == "":
            response["response"] = "Incomplete Parameters"
        else:
            form.save()
            response["response"] = "Successful"
    except Exception as e:
        response["exceptions"] = e

    # Handle the paypal stuff second, that way if paypal fails, their info is saved..?

    return JsonResponse(response)



# class Echo(object):
#     """An object that implements just the write method of the file-like
#     interface.
#     """
#     def write(self, value):
#         """Write the value by returning it, instead of storing in a buffer."""
#         return value
#
# def some_streaming_csv_view(request):
#     """A view that streams a large CSV file."""
#     # Generate a sequence of rows. The range is based on the maximum number of
#     # rows that can be handled by a single sheet in most spreadsheet
#     # applications.
#     rows = (["Row {}".format(idx), str(idx)] for idx in range(65536))
#     pseudo_buffer = Echo()
#     writer = csv.writer(pseudo_buffer)
#     response = StreamingHttpResponse((writer.writerow(row) for row in rows),
#                                      content_type="text/csv")
#     response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
#     return response
