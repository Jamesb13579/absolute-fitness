from django.contrib import admin
from .models import Product, Memberships

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
        'image_url',
        'membership',
        'has_sizes'
    )

    ordering = ('name',)

class MembershipsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

    ordering = ('name',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Memberships, MembershipsAdmin)

