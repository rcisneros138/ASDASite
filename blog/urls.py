from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from blog.models import BlogPost

urlpatterns = [url(r'^$', ListView.as_view(
                    queryset=BlogPost.objects.filter(approved=True).order_by("-date")[:10],
                    template_name="blog/blog.html")),
               url(r'^(?P<pk>\d+$)', DetailView.as_view(
                   model=BlogPost,
                   template_name='blog/post.html'))]
