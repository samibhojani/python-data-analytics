import statistics

print("Sports Science: Average Points per Game (PPG)")

# Points scored by a basketball player in the last 5 games
player_name = input("Player name: ")
games_played = int(
    input(f"No. of games played by Player: {player_name} are: "))
points = []
for match in range(1, games_played + 1):
    scored_points = int(
        input(f"{player_name} score in match # {match}: "))
    points.append(scored_points)


average_points_per_game = statistics.mean(points)
print(f"Player PPG: {average_points_per_game}")
