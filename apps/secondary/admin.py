from django.contrib import admin
from apps.secondary import models
# Register your models here.
class SlideFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title',)
    search_fields = ('title',)

class PartnersFilterAdmin(admin.ModelAdmin):
    list_filter = ('image', )
    list_display = ('image',)
    search_fields = ('image',)
    
class EuroFilterAdmin(admin.ModelAdmin):
    list_filter = ('disc', )
    list_display = ('disc',)
    search_fields = ('disc',)

class GalleryFilterAdmin(admin.ModelAdmin):
    list_filter = ('image', )
    list_display = ('image',)
    search_fields = ('image',)    
    
admin.site.register(models.Gallery, GalleryFilterAdmin)
admin.site.register(models.Explanation, EuroFilterAdmin)
admin.site.register(models.Slide, SlideFilterAdmin)
admin.site.register(models.Parthers, PartnersFilterAdmin)
admin.site.register(models.Advantages1 )
admin.site.register(models.Advantages2 )

