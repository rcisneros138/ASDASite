from django.shortcuts import render
from blog.models import BlogPost
from forms.models import contactUs
from django.http import HttpResponse
from django.views.generic import ListView, CreateView
from forms.AsdaForms import ContactUsForm


class Index(CreateView):
    form_class = ContactUsForm
    model = contactUs
    success_url = '/'
    template_name = "ASDAWebApp/Home/Index.html"

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['recentPosts'] = BlogPost.objects.filter(approved=True).order_by('-date')[:4]
        return context

    def form_valid(self, form):
        form.save()
        return super(Index, self).form_valid(form)




# def index(request):
#     blogPosts = BlogPost.objects.filter(approved=True).order_by('-date')[:4]
#     return render(request, 'ASDAWebApp/Home/Index.html', {'blogPosts': blogPosts})
