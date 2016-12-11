from django.shortcuts import render
from django.views.generic import ListView
from blog.models import BlogPost


class blogPostList(ListView):
    model = BlogPost
    context_object_name = 'blogPost'
    queryset = BlogPost.objects.filter(approved=True).order_by("-date")[:10]
    template_name = "blog/blog.html"
    paginate_by = 5
