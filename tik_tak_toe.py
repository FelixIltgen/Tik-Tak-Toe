import numpy as num
import os
import random
import msvcrt as m

game_field=[1,2,3,
            4,5,6,
            7,8,9,]

current_player = None
current_input = int
x_or_o = "X"

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
    
    if(input == 1 or input == 3 or input == 5 or input == 7 or input == 9):
        if(check_horizontal_win(input) or check_vertical_win(input) or check_diagonal_win(input)):
            print("Spiel gewonnen")
        elif(check_draw()):
            print("Unentschieden")
        else:
            switch_player()        
    elif(input == 2 or input == 4 or input == 6 or input == 8):
        if(check_horizontal_win(input) or check_vertical_win(input)):
            print("Spiel gewonnen")
        elif(check_draw()):
            print("Unentschieden")
        else:
            switch_player()
        
def check_horizontal_win(input):
    #check all horizontal win conditions for every row
    if (input == 1 or input == 4 or input == 7):
        if (game_field[input-1] and game_field[input] and game_field[input+1] == x_or_o):
            print("Spiel Gewonnen")
            return True
        else: 
            return False
    elif(input == 2 or input == 5 or input == 8):
        if(game_field[input-1] and game_field[input-2] and game_field[input] == x_or_o):
            print("Spiel Gewonnen")
            return True
        else: 
            return False
    elif(input == 3 or input == 6 or input == 9):
        if(game_field[input-1] and game_field[input-2] and game_field[input-3]):
            print("Spiel gewonnen")
            return True
        else: 
            return False
    
def check_vertical_win(input):
    #check all vertical win conditions for every colum
    if(input == 1 or input == 2 or input == 3):
        if(game_field[input-1] and game_field[input+2] and game_field[input+5] == x_or_o):
            print("Spiel gewonnen")
            return True
        else: 
            return False
    elif(input == 4 or input == 5 or input == 6):
        if(game_field[input-1] and game_field[input-4] and game_field[input+2] == x_or_o):
            print("Spiel gewonnen")
            return True
        else: 
            return False
    elif(input == 7 or input == 8 or input == 9):
        if(game_field[input-1] and game_field[input-3] and game_field[input-6] == x_or_o):
            print("Spiel gewonnen")
            return True
        else: 
            return False

def check_diagonal_win(input):
    # check all diagonal win conditions
    if(input == 1 or input == 9):
        print(f"{game_field[input-1]},{game_field[input+3]},{game_field[input-5]} ,{game_field[input+7]} ,{game_field[input-9]}")
        if(game_field[input-1] and game_field[input+3] == x_or_o or game_field[input-5] == x_or_o and game_field[input+7] == x_or_o or game_field[input-9] == x_or_o):
            print("Spiel gewonnen")
            return True
        else: 
            return False
    elif(input == 3 or input == 7):
        if(game_field[input-1] and game_field[input+1] == x_or_o or game_field[input-3] == x_or_o and game_field[input+3] == x_or_o or game_field[input-5] == x_or_o):
            print("Spiel gewonnen")
            return True
        else: 
            return False

def check_draw():
    global game_field
    global filed_is_full
    filed_is_full = 0
    for entry in game_field:
        if (isinstance(entry,int)):
            pass
        else:
            filed_is_full += 1
    else:
        if(filed_is_full == 9):
            print("Keine Möglichkeit mehr")
            return True
        else:
            print("Es gibt noch freie Felder")
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
        check_win_condition(current_input)
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
# - 
# - Zuvor gezeichnete Linien löschen
# - Keine Möglichkeit mehr zu gewinnen

