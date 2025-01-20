import os
import random
import msvcrt as m
import sys

#Gamfield array 
game_field=[1,2,3,
            4,5,6,
            7,8,9,]

#Current player is used to determine the diferent players
current_player = None

#Stores user input for calculation
current_input = int

#Stores X/O to calculate
x_or_o = ""


def start_game():
    #Delete previous printed lines in console
    os.system("cls")
    print("Drücke eine Taste, um das Spiel zu Starten...")
    print("----------------------------------------")
    
    #Wait for any user input
    m.getch()
    
    #Delete unnecessary lines 
    delete_line(2)
    choose_first_player() 

def choose_first_player():
    #Use global variables in thise scope
    global current_player
    global x_or_o
    
    #Assign random player to start 
    print("Die Spielreihenfolge wird zufällig zugewiesen!")
    random_int = random.randint(0,1)
    
    #For each player set the necessary variables
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
    #Use global variables in thise scope
    global x_or_o
    global current_player
    
    #Switch player to the other player and set necessary variables
    if (current_player is True):
        print("Spieler O ist an der Reihe!")
        current_player = False
        x_or_o = "O"
        print_game_field()
        choose_field()
    else:
        print("Spieler X ist an der Reihe!")
        current_player = True
        x_or_o = "X"
        print_game_field()
        choose_field()
        
def check_win_condition(input):
    #For input 1, 3, 5, 7, 9 check all win conditions
    if(input == 1 or input == 3 or input == 5 or input == 7 or input == 9):
        #Check win condition, If true => game win else check for draw
        if(check_horizontal_win(input) or check_vertical_win(input) or check_diagonal_win(input)):
            print_game_field()
            print("Spiel gewonnen")
        elif(check_draw()):
            print_game_field()
            print("Unentschieden")
        else:
            switch_player()
            
    #Check only horizontal an vertical win conditions       
    elif(input == 2 or input == 4 or input == 6 or input == 8):
        #Check win condition, If true => game win else check for draw
        if(check_horizontal_win(input) or check_vertical_win(input)):
            print_game_field()
            print("Spiel gewonnen")
        elif(check_draw()):
            print_game_field()
            print("Unentschieden")  
        else:
            switch_player()
        
def check_horizontal_win(input):
    #Check all horizontal win conditions for every colum in the gamefield
    #Compare input in current input with value in the horizontal neighboring fields => return true/false
    if (input == 1 or input == 4 or input == 7):
        if (game_field[input-1] == x_or_o and game_field[input] == x_or_o and game_field[input+1] == x_or_o):
            return True
        else: 
            return False
    elif(input == 2 or input == 5 or input == 8):
        if(game_field[input-1] == x_or_o and game_field[input-2] == x_or_o and game_field[input] == x_or_o):
            return True
        else: 
            return False
    elif(input == 3 or input == 6 or input == 9):
        if(game_field[input-1] == x_or_o and game_field[input-2] == x_or_o and game_field[input-3] == x_or_o):
            return True
        else: 
            return False
    
def check_vertical_win(input):
    #Check all vertical win conditions for every row in the gamefield
    #Compare input in current input with value in the vertically neighboring fields => return true/false
    if(input == 1 or input == 2 or input == 3):
        if(game_field[input-1] == x_or_o and game_field[input+2] == x_or_o and game_field[input+5] == x_or_o):
            return True
        else: 
            return False
    elif(input == 4 or input == 5 or input == 6):
        if(game_field[input-1] == x_or_o and game_field[input-4] == x_or_o and game_field[input+2] == x_or_o):
            return True
        else: 
            return False
    elif(input == 7 or input == 8 or input == 9):
        if(game_field[input-1] == x_or_o and game_field[input-3] == x_or_o and game_field[input-6] == x_or_o):
            return True
        else: 
            return False

def check_diagonal_win(input):
    # Check all diagonal win conditions in the gamefield
    # Compare input in current input with value in the diagonally neighboring fields => return true/false
    match input:
        case 1:
            if(game_field[input-1] == x_or_o and game_field[input+3] == x_or_o and game_field[input+7] == x_or_o):
                return True
            else: 
                return False   
        case 9:
            if(game_field[input-1] == x_or_o and game_field[input-5] == x_or_o and game_field[input-9] == x_or_o):
                return True
            else: 
                return False  
        case 3:
            if(game_field[input-1] == x_or_o and game_field[input+1] == x_or_o and game_field[input+3] == x_or_o):
                return True
            else: 
                return False
        case 7:
            if(game_field[input-1] == x_or_o and game_field[input-3] == x_or_o and game_field[input-5] == x_or_o):
                return True
            else: 
                return False

def check_draw():
    #Use global variables in thise scope
    global game_field
    global filed_is_full
    
    #Locally used
    filed_is_full = 0
    
    #Check each entry if entry is a string (assigned) or a int (unassigned)
    for entry in game_field:
        if (isinstance(entry,int)):
            pass
        else:
            #If field is assigned add one to filed_is_full
            filed_is_full += 1
    else:
        #If field is full => return true/false
        if(filed_is_full == 9):
            return True
        else:
            return False

def choose_field():
    #Use global variables in thise scope
    global current_input
    
    #Try given user input, only string allowed
    try:
        #Request user input 
        current_input = int(input("Wähle ein freies Feld, durch eingabe der Angezeigten zahlen:"))
    except :
        #Point out error and request user input again 
        print("Bitte gebe eine Valide Ganzzahl ein!")
        choose_field()
        
    # Check if choosen field is availabel  
    if( current_input in game_field):
        #Remove current value in array 
        game_field.remove(current_input)
        
        #Replace array value 
        game_field.insert(current_input-1, x_or_o)
        
        #Delet current printed gamefield
        delete_line(10)
        
        #Start checking win conditions
        check_win_condition(current_input)
    else:
        print("Das Feld ist bereits vergeben!")
        choose_field()

def delete_line(count):
    for i in range(count):
        #Cursor up one line
        sys.stdout.write('\x1b[1A')

        #Delete last line
        sys.stdout.write('\x1b[2K')
    
    
#Print gamfield 
def print_game_field():
    
    print("---------")
    print(f"{game_field[0]} | {game_field[1]} | {game_field[2]}")
    print(f"--+---+--")
    print(f"{game_field[3]} | {game_field[4]} | {game_field[5]}")
    print(f"--+---+--")
    print(f"{game_field[6]} | {game_field[7]} | {game_field[8]}")
    print("---------")

start_game()

#To do's: 
# - unentschieden zu spät angezeigt
# - Fehler beim mehrmaligen eingeben von flaschen user input

