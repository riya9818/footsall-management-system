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