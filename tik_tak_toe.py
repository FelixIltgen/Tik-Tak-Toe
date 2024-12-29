import numpy
import os

game_field = [["X","-","-"],
          ["-","O","-"],
          ["-","-","X"]]

#prints all tree rows of the gamfield list
def print_game_field():
    #delete previous printed fields 
    os.system("cls") # => not all fields only specified ones

    print(f"{game_field[0][0]} | {game_field[0][1]} | {game_field[0][2]}")
    print(f"--+---+--")
    print(f"{game_field[1][0]} | {game_field[1][1]} | {game_field[1][2]}")
    print(f"--+---+--")
    print(f"{game_field[2][0]} | {game_field[2][1]} | {game_field[2][2]}")
print_game_field()