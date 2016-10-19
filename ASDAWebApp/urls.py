from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='Index'),
    url(r'^contact/', views.contact, name='contact')
]
