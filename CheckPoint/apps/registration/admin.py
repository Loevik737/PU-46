from django.contrib import admin
from CheckPoint.apps.registration.models import CustomUser
from CheckPoint.apps.subject.models import Subject

class TeachSubjectInline(admin.TabularInline):
    model = CustomUser.attendingSubject.through
    extra = 1 # how many rows to show

class CustomUserAdmin(admin.ModelAdmin):
    inlines = (TeachSubjectInline,)
    exclude = ('attendingSubject',)

admin.site.register(CustomUser, CustomUserAdmin)
