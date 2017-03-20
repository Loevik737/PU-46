from django.contrib import admin
from models import CostumUser
from CheckPoint.apps.subject.models import Subject

class TeachSubjectInline(admin.TabularInline):
    model = Subject
    extra = 1 # how many rows to show

class CostumUserAdmin(admin.ModelAdmin):
    inlines = (TeachSubjectInline,)

admin.site.register(CostumUser,CostumUserAdmin)
