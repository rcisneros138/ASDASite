from django.shortcuts import render
from blog.models import BlogPost
from django.http import HttpResponse


def index(request):
    blogPosts = BlogPost.objects.all().order_by('-date')
    return render(request, 'ASDAWebApp/home.html', {'blogPosts': blogPosts})


def contact(request):
    return render(request, 'ASDAWebApp/basic.html', {'content': ['if you want to contact, email me at',
                                                                 'rcisneros138@gmail.com']})
