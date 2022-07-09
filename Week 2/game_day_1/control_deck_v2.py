
######### Import Modules ##############

import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


import random
import time

#function starts as binary and turns into inputed text
print("Hello World")

def binary_text(string):
    length = len(string)
    binary = ""
    #creates binary digits
    for i in range(length):
        one_zero = random.randint(0, 1)
        binary += str(one_zero)
    print(binary, end="\r")

    output = ""

    #loop changes 1 binary digit to a letter at a time
    for i in range(length):
        time.sleep(0.1)

        #turns string to list
        binary = list(binary)

        #changes the binary digit to letter from string
        binary[i] = string[i]

        output = ""

        #turns list to string
        for k in range(length):
            output += binary[k]

        #prints output, deletes line after printed unless it is finished output
        if i == (length - 1):
            print(output)
        else:
            print(output, end="\r")


########## Declare Variables for Section###############


consoles = ['1', '2', '3']
current_console = None

########## Declare Functions ###############

def gap():
    print('\n')


######### How can I import Lee's binary type function? ############
def scene_intro():
    print('You head towards the Command Deck\n')
    input("Press enter to coninue\n")
    print('As you slowly walk through aluminium passageways you notice words of wisdom marked into the ceiling')
    time.sleep(4)
    print('"If I have seen further than most, it is because I have stood upon the shoulders of giants." I. Newton.\n')
    time.sleep(4)
    print('After navigating through these halls, you arrive on the main deck.')
    time.sleep(3)
    print('You see three black command consoles at the front of the room.\n')
    time.sleep(3)


def choose_console():
    global consoles #### gets the global variable for this section - 'consoles'
    
    ########## check that there are still consoles / riddles to be solved
    if len(consoles) > 0:
        global current_console

        console_choice = input(f'Which console do you choose to approach? {consoles}\n')
        
        for console in consoles:
            if console == console_choice:
                clearConsole()
                print(f'You move over to console {console}')
                current_console = console
                launch_riddle()
                return choose_console()
            ##### EDGE CASE - User inputs values 1, 2 or 3 despite being completed ####
            elif console_choice != '1' or console_choice != "2" or console_choice != "3":
                print('You must choose one of the console terminals.')
                return choose_console()
    else:
        current_console = "puzzle completed"
        launch_riddle()



def launch_riddle():
    if current_console == "1":
        console_1_riddle()
    elif current_console == "2":
        console_2_riddle()
    elif current_console == "3":
        console_3_riddle()
    elif current_console == "puzzle completed":
        give_player_key()


def console_1_riddle():
    global consoles
    if consoles[0] != "1":
        print("Select a different console.")
        gap()
        time.sleep(2)
        return choose_console()
    
    answer = "Love"
    print('The console reads:\n\n')
    gap()
    binary_text('Before you reawaken humanity, you must prove that you understand what it is to be human')
    binary_text('Show that you know what being human means by answering the following riddle:')
    gap()
    #### Clue Round 1 ####
    #### Use the binary text function for all text given by the machine
    #### Keep inputs as blank and call binary text on the line before for the prompt
    binary_text("I can make people happy, I can make people cry.")
    binary_text("I can make people want me, and I can drive people crazy.")
    gap()
    binary_text("What am I?")
    player_answer = input()
    gap()

    #### Check if correct ####
    if player_answer.capitalize() == answer:
        consoles.remove("1")
        binary_text("Love must always be an answer, if humanity is to rebuild to it's former glory.")
        gap()
        time.sleep(2)
        return choose_console()
    else:
        clearConsole()
        print(f'{player_answer.capitalize()} is not the right answer.')
        binary_text('Here is another clue to help you:')
        gap()
        
        ##### Clue Round 2 ####
        binary_text("I am invisible")
        binary_text("I make people suffer from symptoms like sweating and nausea")
        binary_text("and yet people can't survive without me.")
        gap()
        binary_text("What am I?")
        player_answer = input()
        
        #### Check if correct ####
        if player_answer.capitalize() == answer:
            gap()
            consoles.remove("1")
            binary_text("Love must always be an answer, if humanity is to rebuild to it's former glory.")
            time.sleep(2)
            return choose_console()
        else:
            clearConsole()
            print(f'{player_answer.capitalize()} is not the right answer.')
            binary_text('Here is another clue to help you:')
            gap()
            
            #### Clue Round 3 ####
            binary_text("I can be blind, I can be powerful.")
            binary_text("I can be difficult, deep, complicated, and tender at the same time.")
            gap()
            binary_text("What am I?")
            player_answer = input()
            gap()
            
            #### Check if correct ####
            if player_answer.capitalize() == answer:
                consoles.remove("1")
                binary_text("Love must always be an answer, if humanity is to rebuild to it\'s former glory.")
                gap()
                time.sleep(2)
                return choose_console()
            
            else:
                gap()
                print(f'{player_answer.capitalize()} is not the right answer.')
                binary_text('You have not found the answer, come back to console 1 to try again')
                time.sleep(2)
                return choose_console()


def console_2_riddle():
    global consoles
    answer = "Imagination"

    binary_text("Before you reawaken humanity, you must prove that you understand what it is to be human")
    binary_text('Show that you know what being human means by answering the following riddle:')
    gap()
    
    #### Clue Round 1 ####
    binary_text("I am the future that may never happen.")
    binary_text("I am the only weapon in the war against reality.")
    gap()
    binary_text("What am I?")
    player_answer = input()
    gap()

    #### Check if correct ####
    if player_answer.capitalize() == answer:
        consoles.remove("2")
        binary_text('Imagination is fundamental to our experience of life, and will serve us well in the future.')
        time.sleep(2)
        return choose_console()

    else:
        clearConsole()
        print(f'{player_answer} is not the right answer.')
        binary_text('Here is another clue to help you:')
        gap()
        
        ##### Clue Round 2 ####
        binary_text("A book shall ignite me.")
        binary_text("A mystery shall delight me.")
        binary_text("The artist shall invite me.")
        gap()
        binary_text("What am I?")
        player_answer = input()
        gap()
        
        #### Check if correct ####
        if player_answer.capitalize() == answer:
            consoles.remove("2")
            binary_text('Imagination is fundamental to our experience of life, and will serve us well in the future.')
            time.sleep(2)
            return choose_console()
        else:
            clearConsole()
            print(f'{player_answer.capitalize()} is not the right answer.')
            binary_text('Here is another clue to help you:')
            gap()

            #### Clue Round 3 ####
            binary_text("I can carry you to worlds that have never existed.")
            binary_text("And yet, without me, you would go nowhere.")
            gap()
            binary_text("What am I?")
            player_answer = input()
            gap()

            #### Check if correct ####
            if player_answer.capitalize() == answer:
                consoles.remove("2")
                binary_text('Imagination is fundamental to our experience of life, and will serve us well in the future.')
                return choose_console()
            else:
                print(f'{player_answer.capitalize()} is not the right answer.')
                gap()
                binary_text('You have not found the answer, come back to console 2 to try again')
                time.sleep(2)
                return choose_console()


def console_3_riddle():
    global consoles
    answer = "Responsibility"

    binary_text('Before you reawaken humanity, you must prove that you understand what it is to be human')
    binary_text('Show that you know what being human means by answering the following riddle:')
    gap()
    
    #### Clue Round 1 ####
    binary_text("I am the price of greatness and the banishment of regret.")
    binary_text("I am the greatest source of meaning of which a man must not forget.")
    gap()
    binary_text("What am I?")
    player_answer = input()
    gap()
    
    #### Check if correct ####
    if player_answer.capitalize() == answer:
        consoles.remove("3")
        binary_text('Responsibility is essential to the the work you do. Without it we are all lost.')
        time.sleep(2)
        return choose_console()
    else:
        clearConsole()
        print(f'{player_answer.capitalize()} is not the right answer.')
        binary_text('Here is another clue to help you:\n\n')
        gap()

        ##### Clue Round 2 ####
        binary_text("You cannot change the circumstances, the seasons, or the wind,")
        binary_text("but you can change yourself by embracing me.")
        gap()
        binary_text("What am I?")
        player_answer = input()
        gap()

        #### Check if correct ####
        if player_answer.capitalize() == answer:
            consoles.remove("3")
            binary_text('Responsibility is essential to the the work you do. Without it we are all lost.')
            time.sleep(2)
            return choose_console()
        else:
            clearConsole()
            print(f'{player_answer.capitalize()} is not the right answer.')
            binary_text('Here is another clue to help you:')
            gap()

            #### Clue Round 3 ####
            binary_text("I come with freedom.")
            binary_text("I come with priviledge.")
            binary_text("I come with great power")
            gap()
            binary_text("What am I?")
            player_answer = input()
            gap()

            #### Check if correct ####
            if player_answer.capitalize() == answer:
                consoles.remove("3")
                binary_text('Responsibility is essential to the the work you do. Without it we are all lost.')
                time.sleep(2)
                return choose_console()
            else:
                gap()
                print(f'{player_answer.capitalize()} is not the right answer.')
                binary_text('You have not found the answer, come back to console 3 to try again')
                time.sleep(2)
                return choose_console()



def give_player_key():
    print('Player receives key')
    print("You can now move on to the next section of the game.")

######### Execute Program ###########

clearConsole()
scene_intro()
choose_console()
