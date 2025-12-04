# teams/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Team, Player
from .forms import TeamForm, PlayerForm
from django.urls import reverse
from django.db.models import Sum
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

def delete_team(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    if request.method == 'POST':
        team.delete()
        return redirect('team_list')
    return render(request, 'teams/delete_team.html', {'team': team})

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



def top_scorers(request):
    scorers = PlayerMatchStats.objects.values(
        'player__name', 'player__team__name'
    ).annotate(
        total_goals=Sum('goals')
    ).order_by('-total_goals')

    return render(request, 'futsal/top_scorers.html', {'scorers': scorers})

def mark_availability(request, match_id):
    match = Match.objects.get(id=match_id)
    players = Player.objects.filter(team=match.home_team)  # or both teams

    if request.method == "POST":
        for player in players:
            status = request.POST.get(f"status_{player.id}", "available")
            PlayerAvailability.objects.update_or_create(
                player=player,
                match=match,
                defaults={'status': status}
            )
        return redirect('match_detail', match_id=match.id)

    return render(request, 'futsal/mark_availability.html', {
        'match': match,
        'players': players,
    })

def take_attendance(request, match_id):
    match = Match.objects.get(id=match_id)
    players = Player.objects.filter(team=match.home_team)

    if request.method == "POST":
        for player in players:
            present = request.POST.get(f"present_{player.id}") == "on"
            MatchAttendance.objects.update_or_create(
                match=match,
                player=player,
                defaults={'present': present}
            )
        return redirect('match_detail', match_id=match.id)

    return render(request, 'futsal/take_attendance.html', {
        'match': match,
        'players': players,
    })

class Match(models.Model):
    # if you have a separate matches app, adapt import
    team = models.ForeignKey('Team', on_delete=models.CASCADE)
    opponent = models.CharField(max_length=100)
    match_date = models.DateTimeField()

class PlayerMatchStats(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    player = models.ForeignKey('Player', on_delete=models.CASCADE)
    goals = models.PositiveIntegerField(default=0)
    assists = models.PositiveIntegerField(default=0)
    yellow_cards = models.PositiveIntegerField(default=0)
    red_cards = models.PositiveIntegerField(default=0)

def player_performance_summary(request):
    """
    Aggregates per-player totals:
    - matches_played (from PlayerMatchStats)
    - total_goals, total_assists
    - attendance_count (MatchAttendance.present=True)
    - availability_percent (available / total availability marks) * 100
    """

    players = Player.objects.all().annotate(
        # Totals from PlayerMatchStats
        total_goals=Coalesce(Sum('playermatchstats__goals'), 0),
        total_assists=Coalesce(Sum('playermatchstats__assists'), 0),
        matches_played=Coalesce(Count('playermatchstats__match', distinct=True), 0),

        # Attendance count (present=True)
        attendance_count=Coalesce(Count('matchattendance', filter=Q(matchattendance__present=True)), 0),

        # Availability counts: available vs total
        available_count=Coalesce(Count('playeravailability', filter=Q(playeravailability__status='available')), 0),
        availability_total=Coalesce(Count('playeravailability'), 0),
    )