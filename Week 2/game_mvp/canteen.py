from pydoc import synopsis
import time

########FUCTIONS & VARIABLES#############
hotdog = ["Bun", "Sausage", "Hotdog", "Onions", "Ketchup", "Mustard"]
bolognese = ["Pasta", "Cheese", "Mince", "Minced Meat", "Beef", "Tomato Sauce", "Tomato", "Tomatoes", "Onions"]
hamburger = ["Bun", "Roll", "Burger", "Patty", "Onions", "Lettuce", "Tomato", "Cheese", "Sauce", "Kechup"]
recipes = [hotdog, bolognese, hamburger]
attempts = 0
ingredient_list = None
chosen_recipe = None
#########################################



#player chooses recipe 
def choose_recipe():
    global ingredient_list
    chosen_recipe = input("What would you like to make? A Hotdog, Bolognese or Hamburger? \n").capitalize()
    if chosen_recipe.capitalize() == "Hotdog" or chosen_recipe == "Bolognese" or chosen_recipe == "Hamburger":
        print(f"You chose to make a {chosen_recipe.capitalize()}. Excellent choice flesh face...I mean sir! \n")
        ingredient_list = chosen_recipe.capitalize()
        return chosen_recipe.capitalize()
    else:
        print("Please choose a valid recipe")
        return choose_recipe



#player lists ingredient and program checks if true in recipe
def check_ingredients_hotdog(chosen_recipe):
    for ingredients in hotdog or ingredients in bolognese or ingredients in hamburger:
        list_ingredients = input(f"Now type 1 ingredient needed to make your chosen meal & you should be good to go: \n").capitalize()
        time.sleep(2)
        if list_ingredients in hotdog or list_ingredients in bolognese or list_ingredients in hamburger:
            print(f"Great job, you just used the MIX-O-MATIC and made a meal! That wasn't so hard was it... \n")
            return check_ingredients_hotdog
        else:
            print("Not quite, try another one?")

#Introduction & Synopsis of objective
def introduction(synopsis):
    print("Hi there, “HUGO” here! \n")
    time.sleep(2)
    print("It seems you've found your way into the “Canteen”. Here you have access to the MIX-O-MATIC food printer which allows crew members to make a meal of their choice based on the ingredients available in the database. \n")
    time.sleep(4)
    print("You're a human, you like to eat right? \n")
    player = input("Yes or No?: \n").capitalize()
    if player.capitalize() == "Yes":
        print("Ahh that meat suit needing some fuel huh... \n")
    else:
        print("That's odd, I don't sense any bio circuitry in you... \n")
    print("Anyway... Why don't you have a go at making something in the MIX-O-MATIC. \n")
    time.sleep(4)

#############################################################
#Outro & Key
def mission_objective():
    global key_canteen
    print("CONGRATULATIONS HUMAN, YOU WIN! Here's your meal and a prize for playing the game.")
    key_canteen = True
    time.sleep(3)
#############################################################

def play_canteen():
    introduction(synopsis)
    choose_recipe()
    check_ingredients_hotdog(chosen_recipe)
    mission_objective()











