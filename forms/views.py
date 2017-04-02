from .AsdaForms import ContactUsForm
from django.views.generic import FormView, CreateView
from formtools.wizard.views import SessionWizardView


class contactUsView(CreateView):
    form_class = ContactUsForm
    success_url = '/'
    template_name = "ASDAWebApp/Generic/smallFooter.html"

    def form_valid(self, form):
        return super(ContactUsForm, self).form_valid(form)


class PreDentalRegisterWizard(SessionWizardView):
    template_name = "forms/Register.html"

    def done(self, form_list, **kwargs):
        print("worked")
