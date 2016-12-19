from django.conf.urls import url
from django.conf.urls.static import static
from ASDA import settings
from . import views

urlpatterns = [
    url(r'^$', views.index, name='Index'),
    url(r'^contact/', views.contact, name='contact'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
