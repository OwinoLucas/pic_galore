from django.contrib import admin
from .models import Category, Image, location


# Register your models here.
class ImageAdmin(admin.ModelAdmin):
    filter_horizontal =('location',)

admin.site.register(Category)
admin.site.register(Image,ImageAdmin)
admin.site.register(location)