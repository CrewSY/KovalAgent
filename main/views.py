# -*- coding: utf-8 -*-
"""Views for main app of PowerSocket project."""

from django.shortcuts import render
from django.http import HttpResponse

from .models import Equipment, EquipmentLog, Status


def equipment(request):
    """Render page with equipment list."""
    iteams = Equipment.objects.all().order_by('status')
    return render(request, 'main/equipment.html', {'iteams': iteams})


def iteam_details(request, pk):
    """Render page with iteam details."""
    iteam = Equipment.objects.get(id=pk)
    return render(request, 'main/iteam_details.html', {'iteam': iteam})


def change_status(request):
    """Change status and create log object for this action."""
    user = request.user
    data = request.POST

    if user.is_authenticated():
        iteam_id = data.get('iteam_id')
        post_status_id = data.get('post_status_id')

        iteam = Equipment.objects.get(id=iteam_id)
        post_status = Status.objects.get(id=post_status_id)
        pre_status = iteam.status.name

        EquipmentLog.objects.create(owner=user,
                                    iteam=iteam,
                                    pre_status=pre_status,
                                    post_status=post_status)
        iteam.status = post_status
        iteam.save()

    return HttpResponse()
