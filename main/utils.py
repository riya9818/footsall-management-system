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

        # Update played
        standings[home]['played'] += 1
        standings[away]['played'] += 1

        # Goals
        home_score = result.home_score
        away_score = result.away_score

        standings[home]['gf'] += home_score
        standings[home]['ga'] += away_score
        standings[away]['gf'] += away_score
        standings[away]['ga'] += home_score

         # Win / Draw / Loss
        if home_score > away_score:  # Home wins
            standings[home]['wins'] += 1
            standings[home]['points'] += 3
            standings[away]['losses'] += 1

        elif home_score < away_score:  # Away wins
            standings[away]['wins'] += 1
            standings[away]['points'] += 3
            standings[home]['losses'] += 1

        else:  # Draw
            standings[home]['draws'] += 1
            standings[away]['draws'] += 1
            standings[home]['points'] += 1
            standings[away]['points'] += 1

         # Calculate Goal Difference
    for team in standings:
        standings[team]['gd'] = standings[team]['gf'] - standings[team]['ga']

    return standings