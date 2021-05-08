from django.contrib import admin

from rango.models import Profile, Page, Category, ImageModel


admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Page)
admin.site.register(ImageModel)