from django.shortcuts import render, get_object_or_404
from .models import Faction

def factions_list(request):
    factions = Faction.objects.all()
    return render(request, 'factions_list.html', {'factions': factions})

def faction_detail(request, pk):

    faction = get_object_or_404(Faction, pk=pk)
    return render(request, 'faction_detail.html', {'faction': faction})

def dashboard(request):
    return render(request, 'dashboard.html')
