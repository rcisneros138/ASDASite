from django.shortcuts import render
from blog.models import BlogPost
from django.http import HttpResponse
from django.views.generic import DetailView, ListView


class Index(ListView):
    model = BlogPost
    queryset = BlogPost.objects.filter(approved=True).order_by('-date')[:4]
    template_name = 'ASDAWebApp/Home/Index.html'


# def index(request):
#     blogPosts = BlogPost.objects.filter(approved=True).order_by('-date')[:4]
#     return render(request, 'ASDAWebApp/Home/Index.html', {'blogPosts': blogPosts})
