from django.contrib import admin
from .models import CostumUser

class TeachSubjectInline(admin.TabularInline):
    model = CostumUser.attendingSubject.through
    extra = 1 # how many rows to show

class CostumUserAdmin(admin.ModelAdmin):
    inlines = (TeachSubjectInline,)
    exclude = ('attendingSubject',)

admin.site.register(CostumUser,CostumUserAdmin)
