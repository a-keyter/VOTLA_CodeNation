
##### eneter the room do you want to play yes or no #####

def enter_room():
    print("you have just entered the oxygen genrator room")
    print("you notice the oxygen generator isn't working")

    fix_generator = input("Will you fix it?: [y/n]")

##### 'yes' will take you to the game #####
    if fix_generator == "yes":
        print("you have dcided to fix the oxygen generator!") 
        instruction_manual()
##### 'no' will take you back to the main room #####
    elif  fix_generator  == "no":
        print("go back to main room")
##### anything other than 'yes' or 'no' #####      
    else:
        print("please choose yes or no")
        return enter_room()

def instruction_manual():
    print("#####oxygen generator instruction manual#####")

    print("To operate the oxygen generator")
    print("you must first check that the")
    print("battery is in working condition,") 
    print("if not then replace it.") 

    print("Secondly turn the valve to")
    print("let water in to the chamber.")

    print("Finally make sure that the generator")
    print("is connected to the air concentrator") 
    print("to filter out the nitrogen.") 
   

def start_game():

    correct_choice_1 = ("battery")
    correct_choice_2 = ("valve")
    correct_choice_3 = ("air concentrator")

    print("Firstly I replace the")
    choice_1 = input("Enter choice: ")

    print("Secondly I operate the")
    choice_2 = input("Enter choice: ")

    print("Finally I make sure that the generator is connected to the")
    choice_3 = input("Enter choice: ")

    if choice_1 == correct_choice_1 and choice_2 == correct_choice_2 and choice_3 == correct_choice_3:
        print("You have correctly fixed the Oxygen Generator")
        print("A panel on the side opens up and reveals the Oxgen Key")
    else:
        print("incorrect! please try again.")
        return start_game()

   ################ main program ################
def play_oxygen():
    enter_room()
    instruction_manual()
    start_game()
















