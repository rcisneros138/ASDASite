from .views import contactUsView, PreDentalRegisterWizard
from .AsdaForms import PreDentalForm1, PreDentalForm2, PaymentForm
from django.conf.urls import url


urlpatterns = [
               url(r'^register/$', PreDentalRegisterWizard.as_view([PreDentalForm1, PreDentalForm2, PaymentForm])),

             ]
