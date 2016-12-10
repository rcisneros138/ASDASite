from django.conf.urls import url
from django.conf.urls.static import static
from django.views.generic import ListView, DetailView
from blog.models import BlogPost
from ASDA import settings

urlpatterns = [url(r'^$', ListView.as_view(
                    queryset=BlogPost.objects.filter(approved=True).order_by("-date")[:10],
                    template_name="blog/blog.html")),
               url(r'^(?P<pk>\d+$)', DetailView.as_view(
                   model=BlogPost,
                   template_name='blog/post.html'))]
