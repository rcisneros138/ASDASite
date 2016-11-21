from forms import views
from django.conf.urls import url
from django.views.generic import DetailView
from . import views

urlpatterns = [url(r'^$', views.signUp, name='signUp'),
               url(r'^PreDentalWeekendSignup/', views.AddPreDentalWeekendSignup,
                   name='PreDentalWeekendSignup')]
