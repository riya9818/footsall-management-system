from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def add_match(request):
    if request.method == 'POST':
        form = MatchForm(request.POST)
        if form.is_valid():
            match = form.save(commit=False)
            
            # Prevent same team playing itself
            if match.home_team == match.away_team:
                messages.error(request, "Home and Away team must be different!")
                return redirect('add_match')

            match.save()
            messages.success(request, "Match Scheduled Successfully!")
            return redirect('match_list')
    else:
        form = MatchForm()

    return render(request, 'futsal/add_match.html', {'form': form})

def match_list(request):
    matches = Match.objects.all().order_by('-match_date', '-match_time')
    return render(request, 'futsal/match_list.html', {'matches': matches})

def add_match_result(request, match_id):
    match = Match.objects.get(id=match_id)

    if request.method == 'POST':
        form = MatchResultForm(request.POST)
        if form.is_valid():
            result = form.save(commit=False)
            result.match = match
            result.save()
            messages.success(request, "Match result added!")
            return redirect('match_detail', match_id=match.id)
    else:
        form = MatchResultForm()

    return render(request, 'futsal/add_match_result.html', {'form': form, 'match': match})

def match_detail(request, match_id):
    match = Match.objects.get(id=match_id)
    try:
        result = match.matchresult
    except MatchResult.DoesNotExist:
        result = None

    return render(request, 'futsal/match_detail.html', {
        'match': match,
        'result': result
    })

def league_standings(request):
    standings = calculate_standings()

    # Convert dict to list and sort by points, GD, GF
    table = sorted(
        standings.items(),
        key=lambda x: (x[1]['points'], x[1]['gd'], x[1]['gf']),
        reverse=True
    )

    return render(request, 'futsal/standings.html', {'table': table})

def add_player_stats(request, match_id):
    match = Match.objects.get(id=match_id)
    players = Player.objects.filter(team__in=[match.home_team, match.away_team])

    if request.method == "POST":
        for player in players:
            goals = request.POST.get(f"goals_{player.id}", 0)
            assists = request.POST.get(f"assists_{player.id}", 0)
            yellow = request.POST.get(f"yellow_{player.id}", 0)
            red = request.POST.get(f"red_{player.id}", 0)

            PlayerMatchStats.objects.update_or_create(
                match=match,
                player=player,
                defaults={
                    'goals': goals,
                    'assists': assists,
                    'yellow_cards': yellow,
                    'red_cards': red
                }
            )

        return redirect('match_detail', match_id=match.id)

    return render(request, 'futsal/add_player_stats.html', {
        'match': match,
        'players': players
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