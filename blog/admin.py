from django.contrib import admin
from blog.models import BlogPost


class BlogPostAdmin(admin.ModelAdmin):
    class Media:
        js = (
            '/media/tiny_mce/tinymce.min.js',
            '/media/textArea.js',
        )

    def get_readonly_fields(self, request, obj=None):
        if obj and not request.user.is_superuser:
            return ['approved']
        else:
            return []

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        obj.save()

admin.site.register(BlogPost, BlogPostAdmin)
