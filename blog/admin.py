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

    # def image_img(self):
    #     if self.image:
    #         return '<img src="%s" />' % self.image.url
    #     else:
    #         return '(No image found)'
    #
    # image_img.short_description = 'Thumb'
    # image_img.allow_tags = True


admin.site.register(BlogPost, BlogPostAdmin)
