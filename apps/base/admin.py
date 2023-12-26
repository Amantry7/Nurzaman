from django.contrib import admin
from django.contrib.auth.models import User,Group
# Register your models here.
from apps.base import models 

class SettingsPhoneInline(admin.TabularInline):
    model = models.SettingsPhone
    extra =1    

class SettingsFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', 'descriptions')
    search_fields = ('title', 'descriptions')
    inlines = [SettingsPhoneInline]
    
class AboutFilterAdmin(admin.ModelAdmin):
    list_filter = ('discriptions', )
    list_display = ('discriptions', )
    search_fields = ('discriptions',)
    

admin.site.register(models.Settings, SettingsFilterAdmin)
admin.site.register(models.About, AboutFilterAdmin)  
admin.site.register(models.Adres)                            
                          
admin.site.unregister(User)
admin.site.unregister(Group)