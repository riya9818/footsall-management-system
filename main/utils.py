from .models import Match, MatchResult

def calculate_standings():
    standings = {}

    for match in Match.objects.all():
        try:
            result = match.matchresult
        except MatchResult.DoesNotExist:
            continue  # Skip matches with no result

        home = match.home_team
        away = match.away_team

        # Initialize teams
        for team in [home, away]:
            if team not in standings:
                standings[team] = {
                    'played': 0,
                    'wins': 0,
                    'draws': 0,
                    'losses': 0,
                    'gf': 0,
                    'ga': 0,
                    'gd': 0,
                    'points': 0,
                }