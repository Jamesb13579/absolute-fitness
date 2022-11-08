from django.contrib import admin
from .models import Trainers, Classes, Gym


class TrainersAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'about',
        'image_url',
    )

    ordering = ('name',)


class ClassesAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'day_of_week',
        'time',
        'trainers',
    )

    ordering = ('name',)


class GymAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'location',
    )

    ordering = ('name',)


admin.site.register(Trainers, TrainersAdmin)
admin.site.register(Classes, ClassesAdmin)
admin.site.register(Gym, GymAdmin)


