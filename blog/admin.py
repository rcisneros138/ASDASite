from django.contrib import admin
from blog.models import BlogPost, Image


class InlineImage(admin.TabularInline):
    model = Image


class BlogPostAdmin(admin.ModelAdmin):
    inlines = [InlineImage]

    def get_readonly_fields(self, request, obj=None):
        if obj and not request.user.is_superuser:
            return ['approved']
        else:
            return []

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        obj.save()

    def get_queryset(self, request):
        return super(BlogPostAdmin, self).get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())


admin.site.register(BlogPost, BlogPostAdmin)
