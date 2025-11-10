# teams/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Team, Player
from .forms import TeamForm, PlayerForm
from django.urls import reverse

# Players
def player_list(request):
    players = Player.objects.all().order_by('name')
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

# Teams
def team_list(request):
    teams = Team.objects.all().order_by('name')
    return render(request, 'teams/team_list.html', {'teams': teams})

def add_team(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            team = form.save()
            return redirect('team_list')
    else:
        form = TeamForm()
    return render(request, 'teams/add_team.html', {'form': form})

def team_detail(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    players = Player.objects.exclude(id__in=team.members.all())
    return render(request, 'teams/team_detail.html', {'team': team, 'players': players})


def edit_team(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    if request.method == 'POST':
        form = TeamForm(request.POST, instance=team)
        if form.is_valid():
            form.save()
            return redirect('team_list')
    else:
        form = TeamForm(instance=team)
    return render(request, 'teams/edit_team.html', {'form': form, 'team': team})

def add_player_to_team(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    if request.method == 'POST':
        player_id = request.POST.get('player_id')
        if player_id:
            player = get_object_or_404(Player, id=player_id)
            team.members.add(player)
    return redirect('team_detail', team_id=team.id)

def remove_player_from_team(request, team_id, player_id):
    team = get_object_or_404(Team, id=team_id)
    player = get_object_or_404(Player, id=player_id)
    if request.method == 'POST':
        team.members.remove(player)
    return redirect('team_detail', team_id=team.id)

def edit_player(request, player_id):
    player = get_object_or_404(Player, id=player_id)
    if request.method == 'POST':
        form = PlayerForm(request.POST, instance=player)
        if form.is_valid():
            form.save()
            return redirect('player_list')
    else:
        form = PlayerForm(instance=player)
    return render(request, 'teams/edit_player.html', {'form': form, 'player': player})

def delete_player(request, player_id):
    player = get_object_or_404(Player, id=player_id)
    if request.method == 'POST':
        player.delete()
        return redirect('player_list')
    return render(request, 'teams/delete_player.html', {'player': player})