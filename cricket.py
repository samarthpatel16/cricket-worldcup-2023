# Simulate a sports tournament

import csv
import sys
import random

# Number of tournaments to run
N = 10000


def main():

    # Ensure correct usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python tournament.py FILENAME")

    teams = []
    csv_path=sys.argv[1]
    with open(csv_path) as csv_file:
        reader=csv.DictReader(csv_file)
        for row in reader:
            teams.append({
                'team': row['team'],
                'rating': int(row['rating'])
            })

    counts = {}
    for i in range(N):
        winner=simulate_tournament(teams)#return india for example
        counts[winner]= counts.get(winner,0)+1

    for team in sorted(counts, key=lambda team: counts[team], reverse=True):
        print(f"{team}: {counts[team] * 100 / N:.1f}% chance of winning")


def simulate_game(team1, team2):
    """Simulate a game. Return True if team1 wins, False otherwise."""
    rating1 = team1["rating"]
    rating2 = team2["rating"]
    probability = 1 / (1 + 10 ** ((rating2 - rating1) / 600))
    return random.random() < probability


def simulate_round(teams):
    """Simulate a round. Return a list of winning teams."""
    winners = []

    for i in range(0, len(teams), 2):
        if simulate_game(teams[i], teams[i + 1]):
            winners.append(teams[i])
        else:
            winners.append(teams[i + 1])

    return winners


def simulate_tournament(teams):
    """Simulate a tournament. Return name of winning team."""
    # TODO
    winners= teams
    while len(winners)!=1:
        winners= simulate_round(winners)
    return winners[0]['team']


if __name__ == "__main__":
    main()
