from django.contrib import admin
from forms.models import contactUs


class HiddenModelAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return{}


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject')

admin.site.register(contactUs, ContactUsAdmin)
