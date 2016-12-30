from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView
from django.template.context import RequestContext
from blog.models import BlogPost
from forms.AsdaForms import ContactUsForm
from taggit.models import Tag


class blogPostList(ListView):
    model = BlogPost
    context_object_name = 'blogPost'
    queryset = BlogPost.objects.filter(approved=True).order_by("-date")[:10]
    template_name = "blog/blog.html"
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super(blogPostList, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context


class contactUsForm(FormView):
    form_class = ContactUsForm
    success_url = '/'

    def form_valid(self, form):
        form.save(commit=True)


class postDetail(DetailView):
    model = BlogPost
    template_name = 'blog/post.html'


class blogTagQueryList(ListView):
    template_name = "blog/blogQuery.html"
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super(blogTagQueryList, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context

    def get_queryset(self):
        return BlogPost.objects.filter(tags__name=self.kwargs['tag'],
                                       approved=True).order_by("-date")[:10]
