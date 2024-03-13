from django.contrib import admin
from .models import CommonProductName, Product


class ProductAdmin(admin.ModelAdmin):
    # readonly_fields = ("highlighted",)
    pass

admin.site.register(Product, ProductAdmin)


class CommonProductNameAdmin(admin.ModelAdmin):
    ordering = ['name']
    # def get_queryset(self, request):
    #     qs = super().get_queryset(request)
    #     return qs.order_by('name')


admin.site.register(CommonProductName, CommonProductNameAdmin)
