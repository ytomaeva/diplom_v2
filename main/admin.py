from django.contrib import admin

from main.models import Variants


# Register your models here.
class VariantsAdmin(admin.ModelAdmin):
    list_display = ('number', 'description', 'L1', 'R1', 'F', 'Voltage')
    list_display_links = ('number', 'description', 'L1', 'R1', 'F', 'Voltage')
    search_fields = ('number', 'description', 'L1', 'R1', 'F', 'Voltage')
    list_per_page = 25


admin.site.register(Variants, VariantsAdmin)
