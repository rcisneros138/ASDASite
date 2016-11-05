from django.contrib import admin

from blog.models import BlogPost

admin.site.register(BlogPost)


class BlogPostAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        obj.save()
