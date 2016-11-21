from .AsdaForms import signupForm, PreDentalWeekendSignupForm, ContactInformationForm
from django.utils import timezone
from .models import ContactInformation, PreDentalWeekendSignup
from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect


def signUp(request):
    if request.method == "POST":
        form = signupForm(request.POST)
        if form.is_valid():
            Signup = form.save(commit=False)
            Signup.timeStamp = timezone.localtime(timezone.now())
            Signup.save()
            return redirect('ASDAWebApp.views.index')

    else:
        form = signupForm()
        return render(request, 'forms/signUp.html', {'form': form})


def AddPreDentalWeekendSignup(request):
    contactInfo = ContactInformation()
    emergencyContactInfo = ContactInformation()
    contactForm = ContactInformationForm(instance=contactInfo)
    emergencyContactForm = ContactInformationForm(instance=emergencyContactInfo)
    signupInLineFormSet = inlineformset_factory(ContactInformation,
                                                PreDentalWeekendSignup,
                                                fk_name="applicantContactInfo",
                                                fields=('school',
                                                        'needsHotelRoom'),
                                                extra=1,
                                                can_delete=False)
    if request.method == "POST":
        contactForm = ContactInformationForm(request.POST)
        emergencyContactForm = ContactInformationForm(request.POST)
        formset = signupInLineFormSet(request.POST, request.FILES)
        if contactForm.is_valid() and emergencyContactForm.is_valid:
            createdContact = contactForm.save(commit=False)
            createdEmergencyContact = contactForm.save(commit=False)
            formset = signupInLineFormSet(request.POST, request.FILES,
                                          instance=createdContact)
            emergencyFormSet = signupInLineFormSet(request.POST, request.FILES,
                                                   instance=
                                                   createdEmergencyContact)
            if formset.is_valid() and emergencyFormSet.is_valid():
                createdContact.save()
                formset.save()
                emergencyFormSet.save()
                # PreDentalWeekendSignup.timeStamp = timezone.localtime(
                #                                                     timezone.now())
                # PreDentalWeekendSignup.save()
            return HttpResponseRedirect(createdContact.get_absolute_url())
    else:
        contactForm = ContactInformationForm(instance=contactInfo)
        emergencyContactForm = ContactInformationForm(instance=
                                                      emergencyContactInfo)
        formset = signupInLineFormSet()

    return render(request, 'forms/PreDentalWeekendSignup.html', {
                            'contactForm': contactForm,
                            'emergencyContactForm': contactForm,
                            'formset': formset})
