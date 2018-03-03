"""Views for main app of PowerSocket project."""

from django.shortcuts import render

from .models import Equipment


def equipment(request):
    """Render page with equipment list."""
    iteams = Equipment.objects.all().order_by('status')
    return render(request, 'main/equipment.html', {'iteams': iteams})


def iteam_details(request, pk):
    """Render page with iteam details."""
    iteam = Equipment.objects.get(id=pk)
    return render(request, 'main/iteam_details.html', {'iteam': iteam})
