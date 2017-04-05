from django.shortcuts import render
from blog.models import BlogPost, BlogImage
from forms.models import contactUs, PreDentalSignUp
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView, CreateView
from forms.AsdaForms import ContactUsForm
import json
from datetime import datetime


class Index(CreateView):
    form_class = ContactUsForm
    model = contactUs
    success_url = '/'
    template_name = "ASDAWebApp/Home/Index.html"

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['recentPosts'] = BlogPost.objects.filter(
                                 approved=True).order_by('-date')[:4]
        return context

    def form_valid(self, form):
        form.save()
        return super(Index, self).form_valid(form)


class BookClubView(ListView):
    model = BlogPost
    template_name = "ASDAWebApp/Committees/BookClub.html"
    queryset = BlogPost.objects.filter(tags__name='BookClub',
                                       approved=True).order_by("-date")[:4]


class GalleryView(ListView):
    model = BlogImage
    template_name = "ASDAWebApp/Pictures.html"
    queryset = BlogImage.objects.filter(blogPost__approved=True)


class CommunityServiceView(ListView):
    model = BlogPost
    template_name = "ASDAWebApp/Committees/CommunityService.html"
    queryset = BlogPost.objects.filter(tags__name='CommunityService',
                                       approved=True).order_by("-date")[:4]


class VendorRelationsView(ListView):
    model = BlogPost
    template_name = "ASDAWebApp/Committees/VendorRelations.html"
    queryset = BlogPost.objects.filter(tags__name='VendorRelations',
                                       approved=True).order_by("-date")[:4]


class HealthView(ListView):
    model = BlogPost
    template_name = "ASDAWebApp/Committees/Health.html"
    queryset = BlogPost.objects.filter(tags__name='HealthAndWellness',
                                       approved=True).order_by("-date")[:4]


class FundraisingView(ListView):
    model = BlogPost
    template_name = "ASDAWebApp/Committees/FundraisingCommittee.html"
    queryset = BlogPost.objects.filter(tags__name='Fundraising',
                                       approved=True).order_by("-date")[:4]


class PrediatricView(ListView):
    model = BlogPost
    template_name = "ASDAWebApp/Committees/PediatricCommittee.html"
    queryset = BlogPost.objects.filter(tags__name='Pediatrics',
                                       approved=True).order_by("-date")[:4]


class SocialView(ListView):
    model = BlogPost
    template_name = "ASDAWebApp/Committees/SocialCommittee.html"
    queryset = BlogPost.objects.filter(tags__name='Social',
                                       approved=True).order_by("-date")[:4]


class LunchView(ListView):
    model = BlogPost
    template_name = "ASDAWebApp/Committees/LunchClub.html"
    queryset = BlogPost.objects.filter(tags__name='Lunch',
                                       approved=True).order_by("-date")[:4]


class SustainabilityView(ListView):
    model = BlogPost
    template_name = "ASDAWebApp/Committees/SustainabilityCommittee.html"
    queryset = BlogPost.objects.filter(tags__name='Sustainability',
                                       approved=True).order_by("-date")[:4]


class PreDentalView(ListView):
    model = BlogPost
    template_name = "ASDAWebApp/Committees/PreDental.html"
    queryset = BlogPost.objects.filter(tags__name='PreDental',
                                       approved=True).order_by("-date")[:4]


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
