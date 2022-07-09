
######### Import Modules ##############

import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


########## Declare Variables ###############


consoles = ['1', '2', '3']
current_console = None

########## Declare Functions ###############

def scene_intro():
    print('You head towards the Command Deck\n')

    print('As you slowly walk along througgh aluminium passageways you notice words of wisdom marked into the ceiling\n')
    print('If I have seen further than most, it is because I have stood upon the shoulders of giants. I. Newton.\n\n')

    print('After navigating through these halls, you arrive on the main deck.')
    print('You see three black command consoles at the front of the room.\n')


def choose_console():
    global consoles
    
    if len(consoles) > 0:
        global current_console

        console_choice = input(f'Which console do you choose to approach? {consoles}\n')
        
        for console in consoles:
            if console_choice == console:
                print(f'You move over to console {console}')
                current_console = console
                launch_riddle()
                return choose_console()
            else:
                print('Pick choose one of the available consoles')
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
    answer = "Love"
    print('The console reads:\n\n')
    print('Before you reawaken humanity, you must prove that you understand what it is to be human')
    print('Show that you know what being human means by answering the following riddle:\n')
    
    #### Clue Round 1 ####
    player_answer = input("I can make people happy, I can make people cry. \nI can make people want me, and I can drive people crazy.\nWhat am I?\n")
    #### Check if correct ####
    if player_answer.capitalize() == answer:
        consoles.remove("1")
        print('Love must always be an answer, if humanity is to rebuild to it\'s former glory.')
        return choose_console()
    else:
        clearConsole()
        print('Here is another clue to help you:\n\n')
        ##### Clue Round 2 ####
        player_answer = input("I am invisible\n I make people suffer from symptoms like sweating and nausea \nand yet people can't survive without me?\nWhat am I?\n")
        #### Check if correct ####
        if player_answer.capitalize() == answer:
            consoles.remove("1")
            print('Love must always be an answer, if humanity is to rebuild to it\'s former glory.')
            return choose_console()
        else:
            clearConsole()
            print('Here is another clue to help you:\n\n')
            #### Clue Round 3 ####
            player_answer = input("I am invisible\n I make people suffer from symptoms like sweating and nausea \nand yet people can't survive without me?\nWhat am I?\n")
            #### Check if correct ####
            if player_answer.capitalize() == answer:
                consoles.remove("1")
                print('Love must always be an answer, if humanity is to rebuild to it\'s former glory.\n\n')
                return choose_console()
            else:
                print('You have not found the answer, come back to console 1 to try again')
                return choose_console()


def console_2_riddle():
    global consoles
    answer = "Imagination"

    print('Before you reawaken humanity, you must prove that you understand what it is to be human')
    print('Show that you know what being human means by answering the following riddle:\n\n')
    
    #### Clue Round 1 ####
    player_answer = input("I am the future that may never happen. \nI am the only weapon in the war against reality. \nWhat am I?\n")
    #### Check if correct ####
    if player_answer.capitalize() == answer:
        consoles.remove("2")
        print('Imagination is fundamental to our experience of life, and will serve us well in the future.')
        return choose_console()
    else:
        clearConsole()
        print('Here is another clue to help you:')
        ##### Clue Round 2 ####
        player_answer = input("A book shall ignite me. A mystery shall delight me. The artist shall invite me. \nWhat am I?\n")
        #### Check if correct ####
        if player_answer.capitalize() == answer:
            consoles.remove("2")
            print('Imagination is fundamental to our experience of life, and will serve us well in the future.')
            return choose_console()
        else:
            clearConsole()
            print('Here is another clue to help you:')
            #### Clue Round 3 ####
            player_answer = input("I can carry you to worlds that have never existed. And yet, without me, you would go nowhere. \nWhat am I?")
            #### Check if correct ####
            if player_answer.capitalize() == answer:
                consoles.remove("2")
                print('Imagination is fundamental to our experience of life, and will serve us well in the future.')
                return choose_console()
            else:
                print('You have not found the answer, come back to console 2 to try again')
                return choose_console()


def console_3_riddle():
    global consoles
    answer = "Responsibility"

    print('Before you reawaken humanity, you must prove that you understand what it is to be human')
    print('Show that you know what being human means by answering the following riddle:\n\n')
    
    #### Clue Round 1 ####
    player_answer = input("I can make people happy, I can make people cry. \nI can make people want me, and I can drive people crazy.\nWhat am I?\n")
    #### Check if correct ####
    if player_answer.capitalize() == answer:
        consoles.remove("3")
        print('Responsibility is essential to the the work you do. Without it we are all lost.')
        return choose_console()
    else:
        clearConsole()
        print('Here\'s another clue:')
        ##### Clue Round 2 ####
        player_answer = input("You cannot change the circumstances, the seasons, or the wind, but you can change yourself by embracing me. \nWhat am I?\n")
        #### Check if correct ####
        if player_answer.capitalize() == answer:
            consoles.remove("3")
            print('Responsibility is essential to the the work you do. Without it we are all lost.')
            return choose_console()
        else:
            clearConsole()
            print('Here\'s another clue:')
            #### Clue Round 3 ####
            player_answer = input("\nI come with freedom. \nI come with priviledge. I come with great power\n What am I?\n")
            #### Check if correct ####
            if player_answer.capitalize() == answer:
                consoles.remove("3")
                print('Responsibility is essential to the the work you do. Without it we are all lost.')
                return choose_console()
            else:
                print('You have not found the answer, come back to console 3 to try again')
                return choose_console()



def give_player_key():
    print('Player receives key')

######### Execute Program ###########

clearConsole()
scene_intro()
choose_console()
