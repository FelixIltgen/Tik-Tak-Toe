import numpy as num
import os
import random
import msvcrt as m

game_field=[1,2,3,
            4,5,6,
            7,8,9,]

current_player = None
current_input = int
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
    #use global variabels
    global current_player
    global x_or_o
    
    print("Die Spielreihenfolge wird zufällig zugewiesen!")
    random_int = random.randint(0,1)
    if (random_int == 0):
        print("Spiler O beginnt!")
        current_player = False
        x_or_o = "O"
        print_game_field()
        choose_field()
    else:
        print("Spieler X beginnt")
        current_player = True
        x_or_o = "X"
        print_game_field()
        choose_field()
        
def switch_player():
    global x_or_o
    global current_player
    
    if (current_player is True):
        print("Spieler O ist an der Reihe!")
        current_player = False
        x_or_o = "O"
        choose_field()
    else:
        print("Spieler X ist an der Reihe!")
        current_player = True
        x_or_o = "X"
        choose_field()
        
def check_win_condition(input):
    
    match input:
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case 5:
            pass
        case 6:
            pass
        case 7:
            pass
        case 8:
            pass
        case 9:
            pass
def check_horizontal_win(input):
    #check all horizontal win conditions for every row
    if (input == 1 or 4 or 7):
        if (game_field[input-1] and game_field[input] and game_field[input+1] == x_or_o):
            print("Spiel Gewonnen")
            return True
    elif(input == 2 or 5 or 8):
        if(game_field[input-1] and game_field[input-2] and game_field[input] == x_or_o):
            print("Spiel Gewonnen")
            return True
    elif(input == 3 or 6 or 9):
        if(game_field[input-1] and game_field[input-2] and game_field[input-3]):
            print("Spiel gewonnen")
            return True
    else:
        return False

def check_vertical_win(input):
    #check all vertical win conditions for every colum
    if(input == 1 or 2 or 3):
        if(game_field[input-1] and game_field[input+2] or game_field[input+5] == x_or_o):
            print("Spiel gewonnen")
            return True
    elif(input == 4 or 5 or 6):
        if(game_field[input-1] and game_field[input-4] or game_field[input+2] == x_or_o):
            print("Spiel gewonnen")
            return True
    elif(input == 7 or 8 or 9):
        if(game_field[input-1] and game_field[input-3] or game_field[input-6] == x_or_o):
            print("Spiel gewonnen")
            return True
    else:
        return False

def check_diagonal_win(input):
    # check all diagonal win conditions
    if(input == 1 or 9):
        if(game_field[input-1] and game_field[input+3] or game_field[input-5] and game_field[input+7] or game_field[input-9] == x_or_o):
            print("Spiel gewonnen")
            return True
    elif(input == 3 or 7):
        if(game_field[input-1] and game_field[input+1] or game_field[input-3] and game_field[input+3] or game_field[input-5] == x_or_o):
            print("Spiel gewonnen")
            return True
        pass
    else:
        return False

def choose_field():
    global current_input
    #Try user input. Check if input is valid.
    try:
        current_input = int(input("Wähle ein freies Feld, durch eingabe der Angezeigten zahlen:"))
    except :
        print("Bitte gebe eine Valide Ganzzahl ein!")
        current_input = int(input("Wähle ein freies Feld, durch eingabe der Angezeigten zahlen:"))
        
    # Check if choosen field is availabel  
    if( current_input in game_field):
        print("Zahl passt")
        game_field.remove(current_input)
        game_field.insert(current_input-1, x_or_o)
        print_game_field()
        switch_player()
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

start_game()

#To do's: 
# - Unentschieden überprüfen => Function die, das speilfeld checkt ob noch freie Felder sind
# - Zuvor gezeichnete Linien löschen
# - Keine Möglichkeit mehr zu gewinnen

