from .AsdaForms import ContactUsForm
from django.utils import timezone
from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.views.generic import FormView, CreateView


class contactUsView(CreateView):
    form_class = ContactUsForm
    success_url = '/'
    template_name = "ASDAWebApp/Generic/smallFooter.html"

    def form_valid(self, form):

        return super(ContactUsForm, self).form_valid(form)
