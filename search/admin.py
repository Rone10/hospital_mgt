from django.contrib import admin
from . models import City

# Register your models here.

@admin.register(City)
class CitiesAdmin(admin.ModelAdmin):

    list_display = ('name', 'region', 'population', )
    list_filter = ('name',)
    search_fields = ('name', )
    ordering = ('name', )

