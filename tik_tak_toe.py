import numpy as num
import os
import random
import msvcrt as m

game_field=[["1","2","3"],
            ["4","5","6"],
            ["7","8","9"]]
availabel_fields = [1,2,3,4,5,6,7,8,9]

current_player = bool

def start_game():
    os.system("cls")
    print("Drücke eine Taste, um das Spiel zu Starten...")
    print("----------------------------------------")
    m.getch() 
    choose_player() 

def choose_player():
    print("Die Spielreihenfolge wird zufällig zugewiesen!")
    random_int = random.randint(0,1)
    if (random_int == 0):
        print("Spiler O beginnt!")
        current_player == False
        print_game_field()
        #Weiter mit erstem Spielzug von O
    else:
        print("Spieler X beginnt")
        current_player == True
        print_game_field()
        #Weiter mit erstem Spielzug von X

def choose_field():
    try:
        current_input = int(input("Wähle ein freies Feld, durch eingabe der Angezeigten zahlen:"))
    except:
        print("Bitte gebe eine Valide Ganzzahl ein!")
        choose_field()
    if( current_input in availabel_fields):
        print("Zahl passt")
    else:
        print("Zahl passt nicht")

    
    
#prints all tree rows of the gamfield list
def print_game_field():
    
    #delete previous printed fields 
    #os.system("cls") # => not all fields only specified ones

    print(f"{game_field[0][0]} | {game_field[0][1]} | {game_field[0][2]}")
    print(f"--+---+--")
    print(f"{game_field[1][0]} | {game_field[1][1]} | {game_field[1][2]}")
    print(f"--+---+--")
    print(f"{game_field[2][0]} | {game_field[2][1]} | {game_field[2][2]}")

choose_field()

