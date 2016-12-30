from forms import views
from django.conf.urls import url


urlpatterns = [url(r'^$', views.signUp, name='signUp'),
               url(r'^PreDentalWeekendSignup/', views.AddPreDentalWeekendSignup,
                   name='PreDentalWeekendSignup')]
