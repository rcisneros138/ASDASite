from .views import contactUsView, PreDentalRegisterWizard
from .AsdaForms import PreDentalForm1, PreDentalForm2
from django.conf.urls import url

from forms.views import signUp, submitPredentalForm


urlpatterns = [
        url(r'^register/$', PreDentalRegisterWizard,
            name='PreDentalRegisterWizard'),
        url(r'^(?i)signUp/$', signUp.as_view(),
            name='multiPageView'),
        url(r'^(?i)submitPredentalForm/$', submitPredentalForm),
             ]
