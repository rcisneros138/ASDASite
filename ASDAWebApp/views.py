from django.shortcuts import render
from blog.models import BlogPost
from forms.models import contactUs
from django.http import HttpResponse
from django.views.generic import ListView, CreateView
from django.views.generic.edit import FormMixin
from forms.AsdaForms import ContactUsForm


# class FormListView(ListView, FormMixin):
#     def get(self, request, *args, **kwargs):
#         form_class = self.get_form_class
#         self.form = self.get_form(form_class)
#
#         self.object_list = self.get_queryset()
#         context = self.get_context_data(object_list=self.object_list,
#                                         form=self.form)
#         return self.render_to_response(context)
#
#     def post(self, request, *args, **kwargs):
#         return self.get(request, *args, **kwargs)
#
#
# class Index(FormListView):
#     model = BlogPost
#     form_class = ContactUsForm
#     queryset = BlogPost.objects.filter(approved=True).order_by('-date')[:4]
#     template_name = 'ASDAWebApp/Home/Index.html'


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
