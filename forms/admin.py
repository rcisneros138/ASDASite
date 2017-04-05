from django.contrib import admin
from forms.models import contactUs, PreDentalSignUp


class HiddenModelAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return{}


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject')


class PreDentalSignUpAdmin(admin.ModelAdmin):
    list_display = ('name', 'Phone', 'Email', 'School', 'Verified')

admin.site.register(contactUs, ContactUsAdmin)

admin.site.register(PreDentalSignUp, PreDentalSignUpAdmin)
