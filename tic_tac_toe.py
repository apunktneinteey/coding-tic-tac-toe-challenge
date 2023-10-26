# In this script you can write your code.
# Start by writing all the functions.
# In the last part after if __name__ == "__main__": you can call the functions to play your game.
# If you run `python tic_tac_toe.py` in the command line the game will start. Try it out! ;)

# Function for storing player names
def input_username():
    names = []
    name_1 = input('Please insert your name:')
    name_2 = input('Please insert your name:')
    names.append(name_1)
    names.append(name_2)
    print(f'Hi {name_1} and {name_2} let\'s play tick tack toe!')
    print(f'{name_1} next choose your icon, please.')
    return names

# Function for storing player icons
def input_usericon(names):
    icons = []
    icon_1 = input() #'Please choose your icon (X or O):'
    while icon_1 != 'X' and icon_1 != 'O':               
        print('Only enter X or O, please.')
        icon_1 = input('Please choose your icon (X or O):')
        if icon_1 == 'X' or icon_1 == 'O':
            break
    if icon_1 == 'X':
        icon_2 = 'O'
    elif icon_1 == 'O':
        icon_2 = 'X'
    icons.append(icon_1)
    icons.append(icon_2)
    print(names[0] + f' your icon is {icon_1}.')
    print(names[1] + f' your icon is {icon_2}.')
    print(' ')
    return icons


# Function for game display
display = ['some variable', 1, 2, 3, 4, 5, 6, 7, 8, 9]

def show_display_2(display):
    print(display[1], '|', display[2], '|', display[3])
    print('---------')
    print(display[4], '|', display[5], '|', display[6])
    print('---------')
    print(display[7], '|', display[8], '|', display[9])

# Function to switch player name
def switch_playing_name(playing_name, names):
    if playing_name == names[0]:
        playing_name = names[1]
    else:
        playing_name = names[0]
    return playing_name

# Function to switch player icon
def switch_playing_icon(playing_icon, icons):
    if playing_icon == icons[0]:
        playing_icon = icons[1]
    else:
        playing_icon = icons[0]
    return playing_icon

#Function to define win
game_running = True
display = ['some variable', 1, 2, 3, 4, 5, 6, 7, 8, 9]

def win(game_running, display):
    if display[1] == display[4] and display[1] == display[7]:
        game_running =  False
    elif display[2] == display[5] and display[2] == display[8]:
        game_running =  False
    elif display[3] == display[6] and display[3] == display[9]:
        game_running =  False
    elif display[1] == display[2] and display[1] == display[3]:
        game_running =  False
    elif display[4] == display[5] and display[4] == display[6]:
        game_running =  False
    elif display[7] == display[8] and display[7] == display[9]:
        game_running =  False
    elif display[1] == display[5] and display[1] == display[9]:
        game_running =  False
    elif display[3] == display[5] and display[3 ]== display[7]:
        game_running =  False
    if game_running == False:
        print('We have a winner')
    return game_running

#Function to define draw
def draw(count_rounds, game_running): 
    if count_rounds >= 9:
        game_running = False 
    return game_running

#Function for player turn
def player_turns(names, icons, game_running):
    playing_name = names[0]
    playing_icon = icons[0]
    display = ['some variable', 1, 2, 3, 4, 5, 6, 7, 8, 9]
    count_rounds = 1
    while game_running:
        print("  ")
        print(playing_name + (", please enter a number between 1 and 9:"))
        print("  ")
        user_input = int(input()) #'please enter a number between 1 and 9:'
        display[user_input] = playing_icon
        show_display_2(display)
        game_running = draw(count_rounds, game_running)
        if game_running == False:
            print('We have a draw')
            break
        game_running = win(game_running, display)
        if game_running == False:
            print(playing_name + ' is the winner')   
            break
        count_rounds += 1
        playing_name = switch_playing_name(playing_name, names)
        playing_icon = switch_playing_icon(playing_icon, icons)
    return count_rounds


# Tic-tac-toe game
if __name__ == "__main__":
    names = input_username()
    icons = input_usericon(names)
    show_display_2(display)
    #game_running = True
    win(game_running, display)
    player_turns(names, icons, game_running)
    
   
    # Start a new round of Tic-tac-toe
    print("Welcome to a new round of Tic-Tac-Toe!")
