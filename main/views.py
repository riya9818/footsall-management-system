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