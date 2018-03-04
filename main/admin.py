"""Management of main app admin panel."""

from django.contrib import admin

from .models import Equipment, EquipmentLog


class EquipmentAdmin(admin.ModelAdmin):
    """Config equipment on admin page."""

    list_display = ('id',
                    'title',
                    'status',
                    'description',
                    )
    list_filter = ('status', )
    search_fields = ['title', ]

    class Meta:
        """Meta data of EquipmentAdmin."""

        model = Equipment


admin.site.register(Equipment, EquipmentAdmin)


class EquipmentLogAdmin(admin.ModelAdmin):
    """Config equipment log on admin page."""

    list_display = ('owner',
                    'iteam',
                    'pre_status',
                    'post_status',
                    'date',
                    )
    list_filter = ('owner', 'pre_status', 'post_status', )
    search_fields = ('owner',
                     'owner.user__first_name',
                     'owner.user__last_name',
                     'iteam.title',
                     )

    class Meta:
        """Meta data of EquipmentLogAdmin."""

        model = EquipmentLog


admin.site.register(EquipmentLog, EquipmentLogAdmin)
