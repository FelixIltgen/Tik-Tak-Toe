import numpy as num
import os
import random
import msvcrt as m

game_field=[1,2,3,
            4,5,6,
            7,8,9,]

current_player = None
x_or_o = ""

def start_game():
    #Delete previous printed lines
    os.system("cls")
    print("Drücke eine Taste, um das Spiel zu Starten...")
    print("----------------------------------------")
    #Wait for any user input
    m.getch() 
    choose_first_player() 

def choose_first_player():
    global current_player
    print("Die Spielreihenfolge wird zufällig zugewiesen!")
    random_int = random.randint(0,1)
    if (random_int == 0):
        print("Spiler O beginnt!")
        
        current_player = False
        switch_player()
        #Weiter mit erstem Spielzug von O
    else:
        print("Spieler X beginnt")
        current_player = True
        switch_player()
        #Weiter mit erstem Spielzug von X
        
def switch_player():
    global x_or_o
    global current_player
    
    if (current_player is True):
        current_player = False
        x_or_o = "O"
    else:
        current_player = True
        x_or_o = "X"
        
        

def choose_field():
    #Try user input. Check if input is valid.
    try:
        current_input = int(input("Wähle ein freies Feld, durch eingabe der Angezeigten zahlen:"))
    except :
        print("Bitte gebe eine Valide Ganzzahl ein!")
        current_input = int(input("Wähle ein freies Feld, durch eingabe der Angezeigten zahlen:"))
        
    # Check if choosen field is availabel  
    if( current_input in game_field):
        print("Zahl passt")
        game_field.insert(current_input-1, x_or_o)
        print_game_field()
    else:
        print("Das Feld ist bereits vergeben!")
        choose_field()

    
    
#prints all tree rows of the gamfield list
def print_game_field():
    
    #delete previous printed fields 
    #os.system("cls") # => not all fields only specified ones

    print(f"{game_field[0]} | {game_field[1]} | {game_field[2]}")
    print(f"--+---+--")
    print(f"{game_field[3]} | {game_field[4]} | {game_field[5]}")
    print(f"--+---+--")
    print(f"{game_field[6]} | {game_field[7]} | {game_field[8]}")

choose_first_player()

