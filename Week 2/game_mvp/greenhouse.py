import random
import time
from os import system, name

def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

#function starts as binary and turns into inputed text
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
        time.sleep(0.02)

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





original_plants = [["alive", "Rose1", 6],
          ["dead", "Dandelion1", 2],
          ["dead", "Daffodil1", 8],
          ["dead", "Daffodil2", 7],
          ["alive", "Daffodil3", 11],
          ["alive", "Dandelion2", 4],
          ["alive", "Rose2", 10],
          ["dead", "Rose3", 13], 
          ["alive", "Dandelion3", 9], 
          ["dead", "Rose4", 1]]
plants = original_plants.copy()



def show_plants():
    global plants
    print(["Status", "Name", "Size"])
    print("----------------------------------------")
    for plant in plants:
        print(plant)



def are_there_dead_plants():
    global plants
    number_dead_plants = 0
    are_there_dead_plants = True
    for plant in plants:
        if plant[0] == "dead":
            number_dead_plants += 1
    if number_dead_plants > 0:
        return True
    else:
        return False



def check_if_input_valid(user_input): 
    potential_inputs = ["pop()", "pop(first)", "pop(last)",
                       "sort(size)", "sort(ascending, size)", "sort(decending, size)", "sort(name)", "sort(ascending, name)", "sort(descending, name)",
                       "random()", "reset"]
    return user_input in potential_inputs


def split_input(user_input):

    split = user_input.split("(")
    method = split[0]
    if "," in user_input:
        split = split[1].split(",")
        option = split[0]
        split = split[1].split(")")
        split = split[0].split(" ")
        atribute = split[1]
    else:
        split = split[1].split(")")
        atribute = split[0]
        option = None
    
    return [method, option, atribute]


def method_pop(option):
    global plants
    if option == "first":
        if plants[0][0] == "dead":
            plants.pop(0)
        else:
            print("Plant is not dead")
    else:
        if plants[len(plants) - 1][0] == "dead":
            plants.pop()
        else:
            print("Plant is not dead")


def method_sort(option, atribute):
    global plants
    new_plants_array = []
    if atribute == "size":
        
        sizes = []
        for plant in plants:
            sizes.append(plant[2])
        if option == "descending":
            sizes.sort(reverse = True)
        else:
            sizes.sort() 

        #use this list of 1 atribute to sort originl array            
        for size in sizes:
            for plant in plants:
                if size == plant[2]:
                    new_plants_array.append(plant)
        
        plants = new_plants_array



    elif atribute == "name":
        
        ordered_plant_names = []
        for plant in plants:
            ordered_plant_names.append(plant[1])
        if option == "descending":
            ordered_plant_names.sort(reverse = True)
        else:
            ordered_plant_names.sort()

        new_plants_array = []
        for plant_name in ordered_plant_names:
            for plant in plants:
                if plant_name == plant[1]:
                    new_plants_array.append(plant)


        plants = new_plants_array

times_randomised = 0
def method_randomise():
    global plants
    global times_randomised

    if times_randomised < 1:
        ordered_numbers = []
        for i in range(len(plants)):
            ordered_numbers.append(i)

        randomised_numbers = []
        for i in range(len(plants)):
            ran_num = random.randint(0, len(ordered_numbers) - 1)
            randomised_numbers.append(ordered_numbers.pop(ran_num))
        
        randomised_plants = []
        for i in range(len(plants)):
            randomised_plants.append(plants[randomised_numbers[i]])
        times_randomised += 1
        plants = randomised_plants


    else:
        print("You have already randomised, you can not do it again")

def method_reset():
    global plants
    global original_plants
    plants = original_plants.copy()


def manipulate(method, option, atribute):
    global plants
    if method == "pop":
        method_pop(atribute)

    
    if method == "sort":
        method_sort(option, atribute)

    if method == "random":
        method_randomise()
        
    if method == "reset":
        method_reset()


def dialog():
    binary_text("It has been awhile since the plants have been watered.")
    binary_text("Now many of the plants have died, I need you to remove the dead plants for me.")


def rules_binary():
    print("")
    binary_text("The rules are:")
    binary_text("You will be given an array of plants, you need to remove the dead ones")
    binary_text("The plant will be in the format: [alive/dead, name, size]")
    binary_text("You will have the following methods:")
    binary_text("pop()- By default it removes the last value, you can remove the first with pop(first)")
    binary_text("sort(atribute) - The atributes you can sort by are name and size ")
    binary_text("random() - Randomises plant positions, but can only be used once")
    binary_text("reset - Resets plant array to give you the original")
    print("")
    
def rules_normal():
    print("The rules are:")
    print("You will be given an array of plants, you need to remove the dead ones")
    print("The plant will be in the format: [alive/dead, name, size]")
    print("You will have the following methods:")
    print("pop()- By default it removes the last value, you can remove the first with pop(first)")
    print("sort(atribute) - The atributes you can sort by are name and size ")
    print("random() - Randomises plant positions, but can only be used once")
    print("reset - Resets plant array to give you the original")
    


def play_greenhouse():     
    global deadplants # checks if all deadplants are removed
    deadplants = True
    dialog()


   
    times_ran = 0
    while deadplants == True:
        if times_ran == 0:
            rules_binary()
            times_ran += 1
        else:
            rules_normal()
        #make sure user input is valid
        is_input_valid = False
        while is_input_valid != True:
            show_plants()
            user_input = input("Input your method, option and atribute: ")

            is_input_valid = check_if_input_valid(user_input)

            if is_input_valid == False:
                print("invalid input\n")
            
        print("Input is valid\n")


        
        if user_input == "random()":
            method = "random"
            option = None
            atribute = None
            
        elif user_input == "reset":
            method = "reset"
            option = None
            atribute = None

        #returns array in form [method, option, atribute]
        else:
            seperated = split_input(user_input)
            method = seperated[0]
            option = seperated[1]
            atribute = seperated[2]
        
        manipulate(method, option, atribute)

        deadplants = are_there_dead_plants()
        clear()

    show_plants()
    print("")
    binary_text("Thankyou, now all the dead plants have been removed")
    binary_text("Here is your key")
    time.sleep(1.5)
    return True




print(play_greenhouse())

