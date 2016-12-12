from django.conf.urls import url
from django.views.generic import ListView, DetailView
from blog.models import BlogPost
from blog.views import blogPostList, blogTagQueryList


urlpatterns = [url(r'^$', blogPostList.as_view(), name="blogPostList"),
               url(r'^(?P<pk>\d+$)', DetailView.as_view(model=BlogPost,
                   template_name='blog/post.html')),
               url(r'^(?P<tag>\w+)/$', blogTagQueryList.as_view(),
                   name="blogTagQueryList")]


#    ListView.as_view(
#                        queryset=BlogPost.objects.filter(approved=True).order_by("-date")[:10],
#                        template_name="blog/blog.html"))
