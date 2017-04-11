from .views import contactUsView, PreDentalRegisterWizard, payment_page
from .AsdaForms import PreDentalForm1, PreDentalForm2
from django.conf.urls import url, include

from forms.views import signUp, submitPredentalForm


urlpatterns = [
        url(r'^register/$', PreDentalRegisterWizard.as_view([PreDentalForm1, PreDentalForm2]),
            name='PreDentalRegisterWizard'),
        url(r'^(?i)register/payment/', payment_page, name='payment_page'),
        url(r'^(?i)signUp/$', signUp.as_view(),
            name='multiPageView'),
        url(r'^(?i)submitPredentalForm/$', submitPredentalForm),

             ]
