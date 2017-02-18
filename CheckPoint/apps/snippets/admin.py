from django.contrib import admin
from . import models;
# Register your models here.
#registering the user model so we can edit it in the adming panel
admin.site.register(models.User)
