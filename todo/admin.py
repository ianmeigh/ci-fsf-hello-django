from django.contrib import admin
from .models import Item


class ItemAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "done")
    readonly_fields = ("id",)


# Register your models here.
admin.site.register(Item, ItemAdmin)
