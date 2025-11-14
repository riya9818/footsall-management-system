from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def add_match(request):
    if request.method == 'POST':
        form = MatchForm(request.POST)
        if form.is_valid():
            match = form.save(commit=False)
            