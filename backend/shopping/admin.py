from django.contrib import admin

from .models import WishListItem

# Register your models here.


class WishListAdmin(admin.ModelAdmin):
    # readonly_fields = ("highlighted",)
    pass

admin.site.register(WishListItem, WishListAdmin)
