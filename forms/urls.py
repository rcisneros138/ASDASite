from .views import contactUsView, PreDentalRegisterWizard
from .AsdaForms import PreDentalForm1, PreDentalForm2
from django.conf.urls import url


urlpatterns = [
               url(r'^register/$', PreDentalRegisterWizard,
                   name='PreDentalRegisterWizard')
             ]
