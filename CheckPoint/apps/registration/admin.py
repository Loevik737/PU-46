# -*- coding: utf-8 -*-
from django.contrib import admin
from CheckPoint.apps.registration.models import CustomUser
#from CheckPoint.apps.subject.models import Subject

class SubjectInline(admin.TabularInline):
    model = CustomUser.attendingSubject.through
    model._meta.verbose_name_plural = "Attending subjects"
    extra = 1 # how many rows to show
class TeachSubjectInline(admin.TabularInline):
    model = CustomUser.teachingSubject.through
    model._meta.verbose_name_plural = "Teaching subjects"
    extra = 1 # how many rows to show

class CustomUserAdmin(admin.ModelAdmin):
    inlines = (SubjectInline,TeachSubjectInline,)
    exclude = ('attendingSubject','teachingSubject',)


admin.site.register(CustomUser, CustomUserAdmin)
