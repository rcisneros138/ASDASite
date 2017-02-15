from forms import views
from django.conf.urls import url


urlpatterns = [url(r'^$', views.contactUsView.as_view(), name='contactUs')]
