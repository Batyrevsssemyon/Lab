from Player import *

players = []

players.append(Player("Hinata", "Blocker", "Karasuno"))

while True:
    command = input("Write command \r\n")

    if command == "add":
        new_player = Player()
        new_player.add()
        players.append(new_player)

    if command == "show":
        for player in players:
            print(player.show())
