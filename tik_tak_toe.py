import os
import random
import msvcrt as m
import sys
#Gamfield array 
# frontend_game_field= ["1️⃣","2️⃣","3️⃣",
#                       "4️⃣","5️⃣","6️⃣",
#                       "7️⃣","8️⃣","9️⃣",]
frontend_game_field = {"1":"-1-","2":"-2-","3":"-3-","4":"-4-","5":"-5-","6":"-6-","7":"-7-","8":"-8-","9":"-9-"}
game_field = [1,2,3,
              4,5,6,
              7,8,9]

#Current player is used to determine the diferent players
current_player = None

#Stores user input for calculation
current_input = int

#Stores X/O to calculate
x_or_o = ""

#Player names
player_one = None
player_two = None

#Player points
points_player_one = 0
points_player_two = 0

#Filename & Path to save gamedata
file_name = "last_game.txt"
current_path = os.path.abspath(file_name)

def start_game():
    global player_one, player_two
    #Delete previous printed lines in console
    os.system("cls")
    print("⭕ Tic-Tac-Toe ❌")
    print("Drücke eine Taste, um das Spiel zu Starten...")
    print("----------------------------------------")
    
    #Wait for any user input
    m.getch()
    delete_line(3)

    #Ask user to load the priviouse game
    if(ask_user_yes_no("Möchtest du das letzte Spiel wieder aufnehmen? J/N: ")):
        if(check_for_file()):
            #Load gamedata and start the game
            print("Spielerdaten werden geladen")
            read_current_game_data(current_path)
            delete_line(3)
            choose_first_player()
        else:
            delete_line(1)
            print("Es konnten keine Daten gefunden werden!")
    
    player_one = input("Spieler 1, Bitte gebe deinen Namen ein: ")
    player_two = input("Spieler 2, Bitte gebe deinen Namen ein: ")
    #Delete unnecessary lines 
    delete_line(4)
    choose_first_player() 

    
def choose_first_player():
    #Use global variables in thise scope
    global current_player, x_or_o
    
    #Assign random player to start 
    print("Die Spielreihenfolge wird zufällig zugewiesen!")
    random_int = random.randint(0,1)
    
    #For each player set the necessary variables
    if (random_int == 0):
        print(f"{player_two} beginnt das Spiel mit: ⭕")
        current_player = player_two
        x_or_o = "⭕ "
        print_game_field()
        choose_field()
    else:
        print(f"{player_one} beginnt das Spiel mit: ❌")
        current_player = player_one
        x_or_o = "❌ "
        print_game_field()
        choose_field()
        
def switch_player():
    #Use global variables in thise scope
    global x_or_o, current_player
    
    #Switch player to the other player and set necessary variables
    if (current_player is player_one):
        print(f"{player_two} ist an der Reihe!")
        current_player = player_two
        x_or_o = "⭕ "
        print_game_field()
        choose_field()
    else:
        print(f"{player_one} ist an der Reihe!")
        current_player = player_one
        x_or_o = "❌ "
        print_game_field()
        choose_field()
        
def check_win_condition(input):
    #For input 1, 3, 5, 7, 9 check all win conditions
    if(input == 1 or input == 3 or input == 5 or input == 7 or input == 9):
        #Check win condition, If true => game win else check for draw
        if(check_horizontal_win(input) or check_vertical_win(input) or check_diagonal_win(input)):
            add_points(current_player)
            print_game_field()
            print(f"{current_player} hat das Spiel gewonnen 🎉🎊")
            start_again()
        elif(check_draw()):
            print_game_field()
            print("Unentschieden")
            start_again() 
        else:
            switch_player()
            
    #Check only horizontal an vertical win conditions       
    elif(input == 2 or input == 4 or input == 6 or input == 8):
        #Check win condition, If true => game win else check for draw
        if(check_horizontal_win(input) or check_vertical_win(input)):
            add_points(current_player)
            print_game_field()
            print(f"{current_player} hat das Spiel gewonnen 🎉🎊")
            start_again()
        elif(check_draw()):
            print_game_field()
            print("Unentschieden 😑") 
            start_again() 
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
        if(game_field[input-1] == x_or_o and game_field[input-4] == x_or_o and game_field[input-7] == x_or_o):
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
    global game_field, filed_is_full
    
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
    global current_input, frontend_game_field
    
    #Try given user input, only string allowed
    try:
        #Request user input 
        current_input = int(input("Wähle ein freies Feld, durch eingabe der Angezeigten zahlen: "))
        
    except :
        #Point out error and request user input again
        delete_line(1)
        print("Bitte gebe eine Valide Ganzzahl ein! 😩")
        choose_field()

    # Check if choosen field is availabel  
    if( current_input in game_field):
        #Remove current value in array 
        game_field.remove(current_input)
        
        #Replace array value 
        game_field.insert(current_input-1, x_or_o)
        frontend_game_field.update({str(current_input):x_or_o})
        #Delet current printed gamefield
        delete_line(11)
        
        #Start checking win conditions
        check_win_condition(current_input)
    else:
        print("Das Feld ist bereits vergeben! 😩")
        choose_field()
        
def start_again():
    global game_field,player_one, points_player_one, player_two, points_player_two, current_path
    #Ask player to play again
    if(ask_user_yes_no("Möchtet ihr nochmal Spielen? J/N: ")):
        #Reset gamefield and restat game
        game_field=[1,2,3,4,5,6,7,8,9,]
        delete_line(10)
        choose_first_player()
    else:
        delete_line(1)
        #Ask player to save current game
        if(ask_user_yes_no("Möchtest du das Spiel speichern? J/N: ")):
            #Save all necessary data
            save_current_game_data(current_path,player_one,points_player_one,player_two,points_player_two)
            delete_line(11)
            print("Spiel gespeichert 👍🏻")
            #Programme finish
        else:
            delete_line(10)
            print("Spiel beendet 👋🏻")
            #Programme finish

#Delete given lines in the console  
def delete_line(count):
    for i in range(count):
        #Cursor up one line
        sys.stdout.write('\x1b[1A')

        #Delete last line
        sys.stdout.write('\x1b[2K')

#Add points to the corresponding player
def add_points(currentplayer):
    global points_player_one, points_player_two
    #Increment global points
    if(currentplayer == player_one):
        points_player_one += 1
    else:
        points_player_two +=1
#Ask user Y/N question => return True/False
def ask_user_yes_no(message=str):
    yes_no = input(message)
    if (yes_no == "esc" or yes_no == "e"):
        delete_line(10)
        print("Programm beendet!")
        sys.exit(0)
    elif(yes_no =="J" or yes_no == "j"):
        return True
    elif(yes_no == "N" or yes_no == "n"):
        return False
    else:
        delete_line(1)
        print("Bitte gebe nur J oder N ein! 😡")
        ask_user_yes_no(message)
        
#Check if file exists      
def check_for_file():
    global current_path
    if(os.path.exists(current_path)):
        return True
    else:
        return False

#Save game data in txt files
def save_current_game_data(path=str,player_one=str,points_player_one=int, player_two=str,points_player_two= int):
    #Formatted string to save in file
    string_to_save = f"{player_one}\n{points_player_one}\n{player_two}\n{points_player_two}" 
    #Open or creat file and store datastring
    with open(path,"w") as f:
        f.write(string_to_save)
        f.close()        

#Read current game data txt file
def read_current_game_data(path = str):
    global player_one, player_two, points_player_one, points_player_two
    #Open game data file and assign data to corresponding variable
    with open(path) as file:
            data = file.read().splitlines()
            print(data)
            player_one = data[0]
            points_player_one = data[1]
            player_two = data[2]
            points_player_two = data[3]
            file.close()  
    
def print_game_field():
    global current_input,inital_string
    print("---------------")
    print(f"{ frontend_game_field.get("1"):^} | {frontend_game_field.get("2"):^} | {frontend_game_field.get("3"):^} ")
    print("----+-----+----")
    print(f"{ frontend_game_field.get("4"):^} | {frontend_game_field.get("5"):^} | {frontend_game_field.get("6"):^} ")
    print("----+-----+----")
    print(f"{ frontend_game_field.get("7"):^} | {frontend_game_field.get("8"):^} | {frontend_game_field.get("9"):^} ")
    print("---------------")
    print(f"Aktueller Punktestand | {player_one}: {points_player_one} | {player_two}: {points_player_two}")
  
start_game()

    