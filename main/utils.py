from .models import Match, MatchResult

def calculate_standings():
    standings = {}

    for match in Match.objects.all():
        try:
            result = match.matchresult
        except MatchResult.DoesNotExist:
            continue  # Skip matches with no result