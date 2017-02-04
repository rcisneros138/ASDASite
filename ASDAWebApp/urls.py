from django.conf.urls import url
from django.conf.urls.static import static
from django.views.generic import TemplateView
from ASDA import settings
from ASDAWebApp.views import Index, BookClubView, CommunityServiceView, HealthView, FundraisingView, PrediatricView, SocialView, LunchView, SustainabilityView, VendorRelationsView, GalleryView

urlpatterns = [
    url(r'^$', Index.as_view(), name='Index'),
    url(r'^committees/$', TemplateView.as_view(
        template_name='ASDAWebApp/Committees/Committees.html'),
        name='Committees'),
    url(r'^calendar/$', TemplateView.as_view(
        template_name='ASDAWebApp/Calendar/calendar.html'),
        name='Calendar'),
    url(r'^pictures/$', GalleryView.as_view(),
        name='Pictures'),
    url(r'^committees/bookclub/$', BookClubView.as_view(),
        name='BookClubView'),
    url(r'^committees/communityservice/$', CommunityServiceView.as_view(),
        name='CommunityServiceView'),
    url(r'^committees/health/$', HealthView.as_view(), name='HealthView'),
    url(r'^committees/fundraising/$', FundraisingView.as_view(),
        name='FundraisingView'),
    url(r'^committees/pediatric/$', PrediatricView.as_view(),
        name='PrediatricView'),
    url(r'^committees/social/$', SocialView.as_view(), name='SocialView'),
    url(r'^committees/lunch/$', LunchView.as_view(), name='LunchView'),
    url(r'^committees/sustainability/$', SustainabilityView.as_view(),
        name='SustainabilityView'),
    url(r'^committees/vendorrelations/$', VendorRelationsView.as_view(),
        name='VendorRelationsView')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
