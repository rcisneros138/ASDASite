from django.contrib import admin
from forms.models import Signup, PreDentalWeekendSignup, ContactInformation


class HiddenModelAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return{}


class SignupAdmin(admin.ModelAdmin):
    list_display = ('firstName', 'email', 'timeStamp')


class PreDentalWeekendSignupAdmin(admin.ModelAdmin):
    list_display = ['get_name', 'get_lastname', 'needsHotelRoom']

    def get_name(self, obj):
        return obj.applicantContactInfo.firstName

    def get_lastname(self, obj):
        return obj.applicantContactInfo.lastName

    get_name.admin_order_field = 'applicantContactInfo'
    get_name.short_description = 'First Name'
    get_lastname.short_description = 'Last Name'


class ContactInformationAdmin(HiddenModelAdmin):
    list_display = ['firstName', 'lastName']

admin.site.register(Signup, SignupAdmin)
admin.site.register(PreDentalWeekendSignup, PreDentalWeekendSignupAdmin)
admin.site.register(ContactInformation, ContactInformationAdmin)
