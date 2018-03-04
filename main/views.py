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


def logs(request):
    """Render page with logs."""
    logs = EquipmentLog.objects.all().order_by('-date')
    return render(request, 'main/logs.html', {'logs': logs})


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


def update_content(request, sort_by):
    """Update content according value of sort_by."""
    if sort_by == 'title':
        iteams = Equipment.objects.all().order_by('title')
    elif sort_by == 'status':
        iteams = Equipment.objects.all().order_by('status__id')
    else:
        iteams = Equipment.objects.all()

    return render(request, 'equipment_content.html', {'iteams': iteams})
