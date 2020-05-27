from django.contrib import admin
from .models import *


# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'timezone')


class ActivityAdmin(admin.ModelAdmin):
    list_display = ('u_id', 'start_time', 'end_time')


admin.site.register(User, UserAdmin)
admin.site.register(ActivityPeriod, ActivityAdmin)
