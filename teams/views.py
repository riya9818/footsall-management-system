from django.shortcuts import render, redirect, get_object_or_404
from .models import Team, Player
from .forms import TeamForm
from django.contrib.auth.decorators import login_required

def team_list(request):
    teams = Team.objects.all()
    return render(request, 'teams/team_list.html', {'teams': teams})

def team_create(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            team = form.save(commit=False)
            team.save()
            form.save_m2m()  # saves many-to-many relationships (players)
            return redirect('team_list')
    else:
        form = TeamForm()
    return render(request, 'teams/team_form.html', {'form': form})

def team_edit(request, pk):
    team = get_object_or_404(Team, pk=pk)
    if request.method == 'POST':
        form = TeamForm(request.POST, instance=team)
        if form.is_valid():
            form.save()
            return redirect('team_list')
    else:
        form = TeamForm(instance=team)
    return render(request, 'teams/team_form.html', {'form': form})

def team_delete(request, pk):
    team = get_object_or_404(Team, pk=pk)
    if request.method == 'POST':
        team.delete()
        return redirect('team_list')
    return render(request, 'teams/team_confirm_delete.html', {'team': team})

def team_detail(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    players = Player.objects.all()
    return render(request, 'teams/team_detail.html', {'team': team, 'players': players})

def add_player(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    if request.method == 'POST':
        player_id = request.POST.get('player_id')
        new_player_name = request.POST.get('new_player_name')

        if player_id:
            player = Player.objects.get(id=player_id)
        elif new_player_name:
            player = Player.objects.create(name=new_player_name)
        else:
            return redirect('team_detail', team_id=team.id)

        team.members.add(player)
        team.save()
        return redirect('team_detail', team_id=team.id)