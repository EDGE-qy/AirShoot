import game

print("Welcome to play AirShoot, by EDGE_qy.")
mode = int(input("Please select gamemode.\n0 for PVP mode."))
new_game = game.game(mode)
new_game.play()