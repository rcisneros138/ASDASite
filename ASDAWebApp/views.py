from django.shortcuts import render
from blog.models import BlogPost
from forms.models import contactUs
from django.http import HttpResponse
from django.views.generic import ListView, CreateView
from forms.AsdaForms import ContactUsForm


class Index(CreateView):
    form_class = ContactUsForm
    model = contactUs
    success_url = '/'
    template_name = "ASDAWebApp/Home/Index.html"

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['recentPosts'] = BlogPost.objects.filter(approved=True).order_by('-date')[:4]
        return context

    def form_valid(self, form):
        form.save()
        return super(Index, self).form_valid(form)


class BookClubView(ListView):
    model = BlogPost
    template_name = "ASDAWebApp/Committees/BookClub.html"
    queryset = BlogPost.objects.filter(tags__name='BookClub',
                                       approved=True).order_by("-date")[:4]


class CommunityServiceView(ListView):
    model = BlogPost
    template_name = "ASDAWebApp/Committees/CommunityService.html"
    queryset = BlogPost.objects.filter(tags__name='CommunityService',
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
