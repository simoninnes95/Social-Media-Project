from django.contrib import admin
from . import models

# Register your models here.
class GroupMemeberInLine(admin.TabularInline):
    model = models.GroupMemeber

admin.site.register(models.Group)
