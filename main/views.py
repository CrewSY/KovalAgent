"""Views for main app of PowerSocket project."""

from django.shortcuts import render
from django.http import HttpResponse

from .models import Equipment, EquipmentLog


def equipment(request):
    """Render page with equipment list."""
    iteams = Equipment.objects.all().order_by('status')
    return render(request, 'main/equipment.html', {'iteams': iteams})


def iteam_details(request, pk):
    """Render page with iteam details."""
    iteam = Equipment.objects.get(id=pk)
    return render(request, 'main/iteam_details.html', {'iteam': iteam})


def create_log(request):
    """Render page with equipment list."""
    user = request.user
    data = request.POST

    if user.is_authenticated():
        iteam_id = data.get('iteam_id')
        iteam = Equipment.objects.filer(id=iteam_id)
        pre_status = iteam.status

        post_status = data.get('post_status')
        EquipmentLog.objects.create(owner=user,
                                    iteam=iteam_id,
                                    pre_status=pre_status,
                                    post_status=post_status)
        iteam.update(status=post_status)

    return HttpResponse()
