from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *


class UserModel(UserAdmin):
    list_display = ['username','user_type']
admin.site.register(CustomUser,UserModel)

admin.site.register(Course)
admin.site.register(Session_Year)
admin.site.register(Student)

admin.site.register(Staff)
admin.site.register(Subject)
admin.site.register(Staff_Notification)