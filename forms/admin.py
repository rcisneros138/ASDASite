from django.contrib import admin
from forms.models import Signup, PreDentalWeekendSignup, ContactInformation, UsLocation


class HiddenModelAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return{}


class SignupAdmin(admin.ModelAdmin):
    list_display = ('firstName', 'email', 'timeStamp')


class PreDentalWeekendSignupAdmin(admin.ModelAdmin):
    list_display = ['get_name', 'get_lastname', 'get_city', 'needsHotelRoom']

    def get_name(self, obj):
        return obj.applicantContactInfo.firstName

    def get_lastname(self, obj):
        return obj.applicantContactInfo.lastName

    def get_city(self, obj):
        return obj.ApplicantAddress

    get_name.admin_order_field = 'applicantContactInfo'
    get_name.short_description = 'First Name'
    get_lastname.short_description = 'Last Name'
    get_city.admin_order_field = 'ApplicantAddress'


class ContactInformationAdmin(HiddenModelAdmin):
    list_display = ['firstName', 'lastName']


class UsLocationAdmin(HiddenModelAdmin):
    list_display = ['city', 'state']

admin.site.register(Signup, SignupAdmin)
admin.site.register(PreDentalWeekendSignup, PreDentalWeekendSignupAdmin)
admin.site.register(ContactInformation, ContactInformationAdmin)
admin.site.register(UsLocation, UsLocationAdmin)
