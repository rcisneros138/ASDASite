from django.conf.urls import url
from django.conf.urls.static import static
from django.views.generic import TemplateView
from ASDA import settings
from ASDAWebApp.views import Index, BookClubView, CommunityServiceView, HealthView, FundraisingView, PrediatricView, SocialView

urlpatterns = [
    url(r'^$', Index.as_view(), name='Index'),
    url(r'^committees/$', TemplateView.as_view(
        template_name='ASDAWebApp/Committees/Committees.html'),
        name='Committees'),
    url(r'^committees/bookclub/$', BookClubView.as_view(),
        name='BookClubView'),
    url(r'^committees/communityservice/$', CommunityServiceView.as_view(),
        name='CommunityServiceView'),
    url(r'^committees/health/$', HealthView.as_view(), name='HealthView'),
    url(r'^committees/fundraising/$', FundraisingView.as_view(),
        name='FundraisingView'),
    url(r'^committees/pediatric/$', PrediatricView.as_view(),
        name='PrediatricView'),
    url(r'^committees/social/$', SocialView.as_view(), name='SocialView')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
