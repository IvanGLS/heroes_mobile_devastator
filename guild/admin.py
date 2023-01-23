from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from guild.models import (GuildMember,
                          Heroes,
                          Enemy,
                          Battle,)


@admin.register(Heroes)
class Admin(admin.ModelAdmin):
    list_display = ["name", "image"]
    list_filter = ["name"]
    search_fields = ["name"]


@admin.register(GuildMember)
class UserAdmin(UserAdmin):
    list_display = UserAdmin.list_display
    fieldsets = UserAdmin.fieldsets + (
        (("Additional info", {"fields": ("power",
                                         "heroes",)}),)
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Info", {"fields": (
            "first_name",
            "last_name",
            "username",
            "power",
            "heroes",
        )}),)


admin.site.register(Enemy)
admin.site.register(Battle)
admin.site.unregister(Group)
