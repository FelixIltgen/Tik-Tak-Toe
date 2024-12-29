import numpy as num
import os
import random

game_field=[["-","-","-"],
            ["-","-","-"],
            ["-","-","-"]]
current_player = bool
player_zero = 0
player_one = 1

def choose_player():
    print("Die Spielreihenfolge wird zufällig zugewiesen!")
    random_int = random.randint(0,1)
    if (random_int == 0):
        print("Spiler O beginnt!")
    else:
        print("Spieler X beginnt")


#prints all tree rows of the gamfield list
def print_game_field():
    
    #delete previous printed fields 
    os.system("cls") # => not all fields only specified ones

    print(f"{game_field[0][0]} | {game_field[0][1]} | {game_field[0][2]}")
    print(f"--+---+--")
    print(f"{game_field[1][0]} | {game_field[1][1]} | {game_field[1][2]}")
    print(f"--+---+--")
    print(f"{game_field[2][0]} | {game_field[2][1]} | {game_field[2][2]}")

choose_player()
