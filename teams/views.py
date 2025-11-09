from django.shortcuts import render, redirect, get_object_or_404
from .models import Team, Player
from .forms import TeamForm, PlayerForm

def player_list(request):
    players = Player.objects.all()
    return render(request, 'teams/player_list.html', {'players': players})

def add_player(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('player_list')
    else:
        form = PlayerForm()
    return render(request, 'teams/add_player.html', {'form': form})
