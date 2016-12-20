from django.conf.urls import url
from django.conf.urls.static import static
from ASDA import settings
from ASDAWebApp.views import Index

urlpatterns = [
    url(r'^$', Index.as_view(), name='Index'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
