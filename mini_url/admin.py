from django.contrib import admin
from .models import MiniURL

# Register your models here.

class UrlAdmin(admin.ModelAdmin):
    list_display = ('longUrl', 'code', 'pseudo', 'created_date', 'access')
    list_filter = ('pseudo', )
    date_hierarchy = 'created_date'
    ordering = ('created_date', )
    search_fields = ('longUrl', )

    fields = ('longUrl', 'code', 'pseudo', 'created_date', 'access')

admin.site.register(MiniURL, UrlAdmin)
