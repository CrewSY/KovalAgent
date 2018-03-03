"""Management of main app admin panel."""

from django.contrib import admin

from .models import Equipment


class EquipmentAdmin(admin.ModelAdmin):
    """Config equipment on admin page."""

    list_display = [field.name for field in Equipment._meta.fields]
    list_filter = ('status', )
    search_fields = ['title', ]

    class Meta:
        """Meta data of EquipmentAdmin."""

        model = Equipment


admin.site.register(Equipment, EquipmentAdmin)
