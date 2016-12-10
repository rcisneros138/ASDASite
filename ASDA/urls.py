from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from ASDA import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('ASDAWebApp.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^forms/', include('forms.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    # url(r'^forms/', include('forms.urls'))
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
