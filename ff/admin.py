from django.contrib import admin
from .models import Shoe

# class adminForVideo(admin.ModelAdmin):
#     search_fields = ('subs',)
#     list_display = ("title", "course")
# admin.site.register(Video, adminForVideo)
admin.site.register(Shoe)

