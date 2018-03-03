"""Views for main app of PowerSocket project."""

from django.shortcuts import render

from .models import Equipment


def equipment(request):
    """Render page with equipment list."""
    iteams = Equipment.objects.all().order_by('status')
    return render(request, 'main/equipment.html', {'iteams': iteams})
