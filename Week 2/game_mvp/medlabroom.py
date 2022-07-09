import time
import os

def dna_logic():
    global player
    global dna_flag
    global dna_choice
    print("Welcome to the DNA Analyser! Designed to analyse the samples you place inside it.\n")
    if dna_flag == False:
        print("...But you had no samples.")

    else:
        
        dna_choice = input("Please insert the DNA samples in their appropriate sequence (nnnnnn):").strip()

        match dna_choice:
            case '145326':
                clear()
                print(f"DNA sequence recognised.\n\nName: {player}\n\nRank: Admin\n\nPassword: drowssap\n")

            case _:
                clear()
                print("DNA sequence not recognised, aborting...\n")

def chemicals():
    global dna_flag
    print("Investigating the chemicals of the lab seemed to give a range of different concoctions. Acids, DNA samples, even ones you don't know how to say.")
    if dna_flag == False:
        print("You picked up DNA samples 1-6.\n")
        dna_flag = True

def drawer():
    global player
    print(f"You open the drawer to a mess of paperwork. You see a patient record listed... {player.strip()}?\n\nSubject is highly irritable and irrational, instant cryo-freezing is advised until further notice.\n\nDNA Code = AG CY AD TB DA RN\n\nDNA Sequence = 1, 4, 5, 3, 2, 6\n\nReport compiled by: HUGO\n")
    
def artifact():
    global am_choice
    am_choice = input("Do you want to turn it on (yes/no)?").strip()
    if am_choice.isdigit() == True:
        print("Please enter characters only.\n")
        return artifact()

    match am_choice.lower():
        case 'yes':
            clear()
            return dna_logic()
        
        case 'no':
            print("You decided to leave it.")

        case _:
            print("That's not an option.\n")
            return artifact()
    

def room_commands():
    global status
    clear()
    check_id = input("What do you want to check (machinery/drawer/chemicals/artifact)?").strip()
    if status.isdigit() == True:
        print("Please enter characters only.\n")
        return room_commands()

    match check_id.lower():
        case 'machinery':
            clear()
            print("After checking the entire room's worth of machinery, only one terminal seemed to respond.\n")
            check_password()
        
        case 'drawer':
            clear()
            drawer()

        case 'chemicals':
            clear()
            chemicals()

        case 'artifact':
            clear()
            print("You check the strange box with 6 vial-shaped holes in it.\n")
            artifact()

        case _:
            print("That's not an option.")
            return room_commands()    


def check_password():
    global player
    global lab_key
    pw = input("ENTER PASSWORD - ENTER 'EXIT' TO QUIT:").strip()
    if pw.isdigit() == True:
        print("ENTER CHARACTERS, NUMBERS ARE RESTRICTED.\n")
        return check_password()

    match pw.lower():
        case 'exit':
            print("NOW EXITING.\n")
            
        case 'drowssap':
            print("PASSWORD CORRECT.\n")
            if lab_key == False:
              #  time.sleep(1.5) <------- TEAM NOTE - DOESN'T SEEM TO WORK ON MAC/IDLE, ONE OF THE TWO, COMMENTED OUT FOR NOW.
                clear()
                print(f"You entered the password into the terminal, and with a click, a component of the mainframe ejected:- It was a key! {player} took it.\n")
                lab_key = True
                # IMPORTANT! ADD TO KEY COUNT IF ONE IS USED IN THE GAME!

        case _:
            print("PASSWORD INCORRECT!\n")
            return check_password()

def game_state():
    global status
    clear()
    status = input("What do you want to do (check/leave)?").strip()
    if status.isdigit() == True:
        print("Please enter characters only.\n")
        return game_state()

    match status.lower():
        case 'check':
            return room_commands()
        
        case 'leave':
            return True

        case _:
            print("That's not an option.\n")
            return game_state()

########################  MAIN FUNCTION, RUN ROOM FROM HERE ##############################

# Laboratory / Med Bay

# These two will need to be initialised at the start of the game as a whole.
lab_key = False
player = "You"
# TODO - Consider a key count global to be placed here?



# Variable initialisation prerequisites.
exit_room = None
am_choice = False
dna_choice = False
dna_flag = False
status = False


# This is the main logic loop. When True is returned from game_state, the room will be left.

def start_lab():
    global key_lab
    print("You have entered the medical bay. The dimly-lit room is illuminated by the faint glow of the abandoned electronics emanating from the laboratory's machines.\n")
    while exit_room == None:
        exit_room = game_state()

    print("You have left the room.")
    
