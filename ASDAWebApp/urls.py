from django.conf.urls import url
from django.conf.urls.static import static
from django.views.generic import TemplateView
from ASDA import settings
from ASDAWebApp.views import Index, BookClubView

urlpatterns = [
    url(r'^$', Index.as_view(), name='Index'),
    url(r'^committees/$', TemplateView.as_view(
        template_name='ASDAWebApp/Committees/Committees.html'),
        name='Committees'),
    url(r'^committees/bookclub/$', BookClubView.as_view(), name='BookClubView'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
