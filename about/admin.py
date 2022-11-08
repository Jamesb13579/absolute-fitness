from django.contrib import admin
from .models import trainers, classes, gym


admin.site.register(trainers)
admin.site.register(classes)
admin.site.register(gym)
