from django.contrib import admin
from CheckPoint.apps.registration.models import CostumUser
from CheckPoint.apps.subject.models import Subject

class TeachSubjectInline(admin.TabularInline):
    model = CostumUser.attendingSubject.through
    extra = 1 # how many rows to show

class CostumUserAdmin(admin.ModelAdmin):
    inlines = (TeachSubjectInline,)
    exclude = ('attendingSubject',)

admin.site.register(CostumUser,CostumUserAdmin)
