from django.contrib import admin
from .models import Shoe, Skirt, Bag, ProductType

# class adminForVideo(admin.ModelAdmin):
#     search_fields = ('subs',)
#     list_display = ("title", "course")
# admin.site.register(Video, adminForVideo)
admin.site.register(ProductType)
admin.site.register(Shoe)
admin.site.register(Skirt)
admin.site.register(Bag)

