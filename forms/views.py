from .AsdaForms import ContactUsForm, PreDentalForm1, PreDentalForm2
from django.views.generic import FormView, CreateView, ListView
from blog.models import BlogPost, BlogImage
from formtools.wizard.views import SessionWizardView
from paypal.standard.forms import PayPalPaymentsForm
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
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


def payment_page(request, userInfo=None):
    print(request)
    if str(request.session.get('needsHotel')) == "True":
        amount = "425.00"
    else:
        amount = "325.00"
    print(amount)
    paypal_dict = {
        "business": "marquetteasda@gmail.com",
        "amount": str(amount),
        "item_name": "2018 ASDA Pre-Dental Weekend",
        "notify_url": "http://a7014cf5.ngrok.io" + reverse('paypal-ipn'),
        "return_url": "http://a7014cf5.ngrok.io",
        "cancel_return": "https://3562ed89.ngrok.io/forms/signup",
        }
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {"form": form}

    return render(request, "forms/payment.html", context)


class PreDentalRegisterWizard(SessionWizardView):
    template_name = "forms/Register.html"

    def done(self, form_list, **kwargs):
        self.request.session['signUpForm'] = self.request.POST
        print(self.request.POST)
        print(self.get_all_cleaned_data())
        print("worked~~!!!!!")
        print(form.cleaned_data for form in form_list)
        return HttpResponseRedirect('payment')


class signUp(ListView):
    model = BlogPost
    success_url = '/'
    template_name = "forms/signuppage.html"


class signUpSuccess(ListView):
    model = BlogPost
    success_url = '/'
    template_name = "forms/signupsuccess.html"


def submitPredentalForm(request):
    form = PreDentalSignUp(
        name=str(request.POST.get('Name')),
        Phone=str(request.POST.get('Phone')),
        Address1=str(request.POST.get('Address1')),
        Address2=str(request.POST.get('Address2')),
        Email=str(request.POST.get('Email')),
        Gender=str(request.POST.get('Gender')),
        BirthDate=str(request.POST.get('BirthDate')),

        School=str(request.POST.get('School')),
        Year=str(request.POST.get('Year')),

        EmergName=str(request.POST.get('EmergName')),
        EmergPhone=str(request.POST.get('EmergPhone')),
        EmergEmail=str(request.POST.get('EmergEmail')),

        SocialEvent=str(request.POST.get('SocialEvent')),
        DietaryNeeds=str(request.POST.get('DietaryNeeds')),
        NeedHotel=str(request.POST.get('NeedHotel'))
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
            request.session['needsHotel'] = request.POST['NeedHotel']

            return HttpResponseRedirect('/forms/register/payment')
    except Exception as e:
        response["exceptions"] = e

    return JsonResponse(response)

    # return HttpResponseRedirect('/forms/register/payment')

# This was the beginning of csv files.
# for large files, it said it was good to stream the file, that way if the page refreshed or cancelled, the connection would not be lost I think.

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
