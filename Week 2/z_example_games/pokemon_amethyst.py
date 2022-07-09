import random, time, sys

current_xp = 0
still_alive = True
pet_name = " "
user_attack = True
damage = 0
attack_option = " "
i = 0
z = 0
spell_name = " "
game_over = False
attack_damage = 0
max_hp = 50
user_hp = max_hp
enemy_type = 0
ele_attack = " "
ele_check = " "
ele_effect = 1
user_name = " "
enemy_hp = 50
enemy_name = " "
first_time = True
end_scaling = 0
hyper_potion = 0
pokeballs = 1
difficulty_select = 1
# setting variables to initial conditions so they are able to function and be modified later

pokemon_list = [
        "Bulbasaur", "Squirtle", "Charmander", "Growlithe", "Marril", 
        "Kakuna", "Pidgey", "Diglett", "Nidorino", "Kadabra", "Hitmonchan"
]
# the list of pokemon names used in the game

types = [
        "grass", "water", "fire", "fire", "water", "grass", "normal", "normal", "normal", "normal", "normal"
]
# the types of the pokemon in the previous list in same order

damage = 0
# for xp scaling, replaced by xp code

current_pet = 1
pet_one_hp = 50
pet_two_hp = 0
pet_two_name = " "
# for setting more variables for use of 2 pets, pet_two_hp = 0 will be required in game until the capture code is used which will replace the input here

boss_fight = 0
battle_count = 0
# variables for tracking specific fight/ progress

## battle() function
def initial_conditions():
    global still_alive, enemy_hp, enemy_name, boss_fight, end_scaling, pokeballs, is_npc_battle, difficulty_select
    enemy_type = random.randint(1, 5)
    if boss_fight == 0:
        enemy_name = pokemon_list[enemy_type+2]
        print(f"A wild {pokemon_list[enemy_type+2]} ({types[enemy_type+2]}) appears")
    elif boss_fight == 1:
        enemy_name = "Nidorino"
        print(f"Gus chooses {enemy_name}")
    elif boss_fight == 2:
        enemy_name = "Kadabra"
        print(f"Gus chooses {enemy_name}")
    elif boss_fight == 3:
        enemy_name = "Hitmonchan"
        print(f"Gus chooses {enemy_name}")
    else:
        print("avoid this")
# creates a random enemy from 5 types (middle of the pokemon_list) if it's not the defined boss fight where it picks them specific fights (1, 2, 3)
# else line never happens
    still_alive = True
    enemy_hp = round(random.randint(40, 50) + 3 * damage + 2 * end_scaling)
# provides a random hp between 40 and 50 with some minor scaling from the xp scaling code
    if pokeballs >= 1:
        menu_bush()
    else:
        menu()
    return enemy_name, still_alive
# calls menu function

def menu():
    global user_hp, max_hp, is_npc_battle, hyper_potion, user_name
    print (f"Current Pokemon ({user_name}) hp: {user_hp}/{max_hp}, you currently have {hyper_potion} hyper potions")
    print("Choose a number")
    opt_menu = input("1 - Attack        2 - Swap Pokemon\n3 - Heal          4 - Run\n")
    if opt_menu == "1":
        battle()
    elif opt_menu == "2":
        pet_health()
        menu()
    elif opt_menu == "3":
        if hyper_potion > 0:
            print("You used a Hyper Potion!")
            time.sleep(2)
            print("You recovered all your pokemon's HP")
            user_hp = max_hp
            hyper_potion -= 1
        else:
            print("You don't have any hyper potions")
        menu()
    elif opt_menu == "4":
        if is_npc_battle == False:
            print("CAN ESCAPE")
        else:
            print("You can't run away from this battle ")
            menu()
    else:
        print("Choose a number from the options!")
        menu()
    return hyper_potion

def menu_bush():
    global hyper_potion, user_hp, max_hp, is_npc_battle, user_name
    print (f"Current Pokemon ({user_name}) hp: {user_hp}/{max_hp}, you currently have {hyper_potion} hyper potions")
    print("Choose a number")
    opt_menu = input("1 - Attack        2 - Capture Pokemon\n3 - Heal          4 - Run\n")
    if opt_menu == "1":
        battle()
    elif opt_menu == "2":
        if is_npc_battle == True:
            print("You can't capture pokemon from others")
            menu_bush()
        else:
            capt_pokemon()
    elif opt_menu == "3":
        if hyper_potion > 0:
            print("You used a Hyper Potion!")
            time.sleep(2)
            print("You recovered all your pokemon's HP")
            user_hp = max_hp
            hyper_potion -= 1
        else:
            print("You don't have any hyper potions")
        menu_bush()
    elif opt_menu == "4":
        if is_npc_battle == False:
            print("CAN ESCAPE")
        else:
            print("You can't run away from this battle ")
            menu_bush()
    else:
        print("Choose a number from the options!")
        menu_bush()



def capt_pokemon():
    global pokeballs, pet_two_hp, enemy_name, max_hp, pet_two_name, difficulty_select
    if pokeballs >= 1:
        print("You can only capture one pokemon, choose wisely")
        capt_ = input(f"Are you sure you want to capture {enemy_name}? Yes/No\n").lower()
        if capt_ == "y" or capt_ == "yes" or capt_ == "YES":
            print("the pokeball swings and... ")  
            time.sleep(2)
            print(f"You captured {enemy_name}!!")
            pet_two_name = enemy_name
            pet_two_hp = max_hp
            pokeballs -= 1
            time.sleep(2)
        else:
            print(f"You didn't want to capture {enemy_name}")
            time.sleep(2)
            menu_bush()
    else:
        print("You don't have any pokeballs")
        menu()
    return pet_two_name, pet_two_hp, pokeballs

def battle():
    global attack_damage, battle_count, user_hp, enemy_type, ele_attack, ele_check, ele_effect, spell_name, user_attack, pet_name, still_alive, enemy_hp, enemy_name, current_xp, end_scaling
    while still_alive == True:
        if enemy_hp <= 0:
            still_alive = False
# while loop ends if either user or enemy has <=0 hp
        else: 
            user_attack = True
            pet_name = user_name
            pokemon_selection()
            pet_name = enemy_name
            type_check()
            effectiveness()
# calls the required functions based on if check while setting the variable pet_name to the correct side of the battle for each call and that is it's the users turn to attack
            x = round(attack_damage * ele_effect)
            enemy_hp = enemy_hp - x
            print(f"{user_name} used {spell_name} for {x} damage")
            if ele_effect == 1.5:
                print(f"It's super effective")
            elif ele_effect == 0.75:
                print(f"It's not very effective")
            else:
                pass
# prints the outcomes of the combat for the user showing their dmg, and if 'effective'
# caculates the change in the enemy health in the background
            if enemy_hp <= 0:
                print("You won")
                xp_gain()
                stat_gain()
                battle_count += 1
# user goes first so enemy_hp calculation is first and fight ends if enemy_hp <=0
            else:
                user_attack = False
                pet_name = enemy_name
                pokemon_selection()
                pet_name = user_name
                type_check()
                effectiveness()
# the enemy turn using the same functions as previously to calculate the requirements for their dmg dealt
                y = round(((attack_damage + end_scaling) * ele_effect) * difficulty_select)
                user_hp = user_hp - y
                if user_hp < 0:
                    user_hp = 0
                else:
                    pass
                print(f"{enemy_name} used {spell_name} for {y} damage")                       
                if ele_effect == 1.5:
                    print(f"It's super effective")
                elif ele_effect == 0.75:
                    print(f"It's not very effective")
                else:
                    pass
# prints the outcomes of the combat for the user showing their dmg, and if 'effective'
# caculates the change in the enemy health in the background
# if user dies sets the hp to 0 rather than negative values
                print(f"Current hp: {user_hp} vs Enemy hp: {enemy_hp}")
# updates the user on the current hp of those involved in the battle
                if user_hp <= 0:
                    pet_health()
# runs the function to check if the user has a 2nd pokemon to use to carry on with the fight
                else:
                    print("Next Turn")
# if user survives, precedes to next turn
    return user_hp, battle_count, end_scaling
# sends user_hp and battle_count back to main script

## effectuvenes_user() function
def effectiveness():
    global ele_attack, ele_check, ele_effect
    if ele_attack == "grass":
        if ele_check == "water":
            ele_effect = 1.5
        elif ele_check == "fire":
            ele_effect = 0.75
        else:
            ele_effect = 1
    elif ele_attack == "water":
        if ele_check == "fire":
            ele_effect = 1.5
        elif ele_check == "grass":
            ele_effect = 0.75
        else:
            ele_effect = 1
    elif ele_attack == "fire":
        if ele_check == "grass":
            ele_effect = 1.5
        elif ele_check == "water":
            ele_effect = 0.75
        else:
            ele_effect = 1
    else:
        ele_effect = 1
    return ele_effect
# calculates if you using a strong, weak or neutral element compared to the enemies type
# provides a 1.5 multiplier is strong, 0.75 if weak and no change if neutral
# fire > grass > water > fire strength, normal type attacks are never effected

## pet_health() function
def pet_health():
    global user_hp, pet_one_hp, pet_two_hp, current_pet, user_name, pet_one_name, pet_two_name, game_over
    if current_pet == 1:
        pet_one_hp = user_hp
    elif current_pet == 2:
        pet_two_hp = user_hp
    else:
        print("not allowed to happen")
    if pet_one_hp <= 0 and pet_two_hp <= 0:
        game_over = True
        print("Game Over")
        sys.exit()
    elif current_pet == 1:
        current_pet = 2
        user_hp = pet_two_hp
        user_name = pet_two_name
        if pet_one_hp <= 0:
            print(f"{pet_one_name} fainted so swapped to {pet_two_name}")
        else:
            print(f"You recall {pet_one_name} and choose {pet_two_name}")
    elif current_pet == 2:
        current_pet = 1
        user_hp = pet_one_hp
        user_name = pet_one_name
        if pet_two_hp <= 0:
            print(f"{pet_two_name} fainted so swapped to {pet_one_name}")
        else:
            print(f"You recall {pet_two_name} and choose {pet_one_name}")
    else:
        print("exactly the thing we don't want to happen")
    return user_hp, user_name, game_over
# checks which pet is currently active and updates its hp from the user hp in battle
# if after this update both pets <=0 it ends combat
# if one pet is still alive it automatically swap to the other pet so they can carry on with combat and updates the variables in battle()

# pokemon_selection() function
def pokemon_selection():
    global spell_name, ele_attack, attack_damage, ele_check
    if (pet_name in pokemon_list):
        i = pokemon_list.index(pet_name)
        if user_attack == True:
            z = damage
        else:
            z = 0
            attack_option = random.randint(1,3)
# damage is the variable obtained from xp code that gives user pokemon more dmg as they lvl up, for enemies this is set to 0 so nothing is added
# picks a random attack_option for enemies between 1-3
# i is the index number in the pokemon.list to use the appropiate if statement below (individual pokemon)
        if i == 0:          # Bulbasaur - Grass
            ele_check = "grass"
            if user_attack == True:
                attack_option = input("Choose attack number: \n [1] Leaf Blade (grass), [2] Frenzy Plant (grass), [3] Vine Whip (normal)\n")
                while attack_option.isdigit() == False:
                    attack_option = input("Enter an actual number: \n")
            else:
                pass
            if int(attack_option) == 1:
                attack_damage = random.randint(5, 35) + z
                ele_attack = "grass"
                spell_name = "Leaf Blade"
            elif int(attack_option) == 2:
                attack_damage = 5 * (random.randint(4, 6) + round(z*0.2))
                ele_attack = "grass"
                spell_name = "Frenzy Plant"
            elif int(attack_option) == 3:
                attack_damage = 2 * (random.randint(10, 16) + round(z*0.5))
                ele_attack = "normal"
                spell_name = "Vine Whip"
            else:
                print("Invalid attack, Please enter correctly")
                pokemon_selection()
# sets the ele_check variable for the selected pokemon, if user asks for their attack input displaying the options, if enemy using the previous random pick
# from this calculates the attack_damage variable to be used in battle(), it's ele_attack type and associated spell_name for user outputs
        elif i == 1:        # Squirtle - Water
            ele_check = "water"
            if user_attack == True:
                attack_option = input("Choose attack number: \n [1] Hydropump (water), [2] Waterbeam (water), [3] Tackle (normal)\n")
                while attack_option.isdigit() == False:
                    attack_option = input("Enter an actual number: \n")
            else:
                pass
            if int(attack_option) == 1:
                attack_damage = random.randint(15, 35) + z
                ele_attack = "water"
                spell_name = "Hydropump"
            elif int(attack_option) == 2:
                attack_damage = 10 * (random.randint(2, 3) + round(z*0.1))
                ele_attack = "water"
                spell_name =  "Waterbeam"
            elif int(attack_option) == 3:
                attack_damage = random.randint(15, 30) + z
                ele_attack == "normal"
                spell_name = "Tackle"
            else:
                print("Invalid attack, Please enter correctly")
                pokemon_selection()                
        elif i == 2:         # Charmander - Fire
            ele_check = "fire"
            if user_attack == True:
                attack_option = input("Choose attack number: \n [1] Pyroblast (fire), [2] Firewhirl (fire), [3] Quick Attack (normal)\n")
                while attack_option.isdigit() == False:
                    attack_option = input("Enter an actual number: \n")
            else:
                pass
            if int(attack_option) == 1:
                attack_damage = random.randint(10, 40) + z
                ele_attack = "fire"
                spell_name = "Pyroblast"
            elif int(attack_option) == 2:
                attack_damage = 3 * (random.randint(7, 11) + (1/3)*z)
                ele_attack = "fire"
                spell_name =  "Firewhirl"
            elif int(attack_option) == 3:
                attack_damage = random.randint(22, 28) + z
                ele_attack = "normal"
                spell_name = "Quick Attack"
            else:
                print("Invalid attack, Please enter correctly")
                pokemon_selection()
        elif i == 3:        # Growlith - Fire
            ele_check = "fire"
            if user_attack == True:
                attack_option = input("Choose attack number: \n [1] Lava Spit (fire), [2] Flamethrower (fire), [3] Quick Attack (normal)\n")
                while attack_option.isdigit() == False:
                    attack_option = input("Enter an actual number: \n")
            else:
                pass
            if int(attack_option) == 1:
                attack_damage = random.randint(10, 20) + z
                ele_attack = "fire"
                spell_name = "Lava Spit"
            elif int(attack_option) == 2:
                attack_damage = 2 * (random.randint(5, 10) + round(z*0.5))
                ele_attack = "fire"
                spell_name = "Flamethrower"
            elif int(attack_option) == 3:
                attack_damage = 16 + z
                ele_attack = "normal"
                spell_name = "Quick Attack"
            else:
                print("Invalid attack, Please enter correctly")
                pokemon_selection()
        elif i == 4:        # Marill - Water
            ele_check = "water"
            if user_attack == True:
                attack_option = input("Choose attack number: \n [1] Aqua Jet (water), [2] Water Shuriken (water), [3] Tackle (normal)\n")
                while attack_option.isdigit() == False:
                    attack_option = input("Enter an actual number: \n")
            else:
                pass
            if int(attack_option) == 1:
                attack_damage = random.randint(5, 25) + z
                ele_attack = "water"
                spell_name = "Aqua Jet"
            elif int(attack_option) == 2:
                attack_damage = 4 * (random.randint(4, 5) + round(0.25*z))
                ele_attack = "water"
                spell_name = "Water Shuriken"
            elif int(attack_option) == 3:
                attack_damage = 15 + z
                ele_attack = "normal"
                spell_name = "Tackle"
            else:
                print("Invalid attack, Please enter correctly")
                pokemon_selection()
        elif i == 5:        # Kakuna - Grass
            ele_check = "grass"
            if user_attack == True:
                attack_option = input("Choose attack number: \n [1] Giga Drain (grass), [2] Leech Seed (grass), [3] Vine Whip (normal)\n")
                while attack_option.isdigit() == False:
                    attack_option = input("Enter an actual number: \n")
            else:
                pass
            if int(attack_option) == 1:
                attack_damage = random.randint(5, 25) + z
                ele_attack = "grass"
                spell_name = "Giga Drain"
            elif int(attack_option) == 2:
                attack_damage = 4 * (random.randint(4, 5) + round(0.25*z))
                ele_attack = "grass"
                spell_name = "Leech Seed"
            elif int(attack_option) == 3:
                attack_damage = 2 * (random.randint(5, 10) + round(z*0.5))
                ele_attack = "normal"
                spell_name = "Vine Whip"
            else:
                print("Invalid attack, Please enter correctly")
                pokemon_selection()
        elif i == 6:        # Pidgey - Normal
            ele_check = "normal"
            if user_attack == True:
                attack_option = input("Choose attack number: \n [1] Gust (normal), [2] Wing Attack (normal), [3] Whirlwind (normal)\n")
                while attack_option.isdigit() == False:
                    attack_option = input("Enter an actual number: \n")
            else:
                pass
            if int(attack_option) == 1:
                attack_damage = random.randint(5, 25) + z
                ele_attack = "normal"
                spell_name = "Gust"
            elif int(attack_option) == 2:
                attack_damage = 4 * (random.randint(4, 5) + round(0.25*z))
                ele_attack = "normal"
                spell_name = "Wing Attack"
            elif int(attack_option) == 3:
                attack_damage = 10 * (random. randint(1, 3) + round(0.1*z))
                ele_attack = "normal"
                spell_name = "Whirlwind"
            else:
                print("Invalid attack, Please enter correctly")
                pokemon_selection()
        elif i == 7:        # Diglett - Normal
            ele_check = "normal"
            if user_attack == True:
                attack_option = input("Choose attack number: \n [1] Scractch (normal), [2] Dig (normal), [3] Earthquake (normal)\n")
                while attack_option.isdigit() == False:
                    attack_option = input("Enter an actual number: \n")
            else:
                pass
            if int(attack_option) == 1:
                attack_damage = random.randint(10, 15) + z
                ele_attack = "normal"
                spell_name = "Scratch"
            elif int(attack_option) == 2:
                attack_damage = random.randint(5, 20) + z
                ele_attack = "normal"
                spell_name = "Dig"
            elif int(attack_option) == 3:
                attack_damage = 3 * (random.randint(3, 8) + round((1/3)*z))
                ele_attack = "normal"
                spell_name = "Earthquake"
            else:
                print("Invalid attack, Please enter correctly")
                pokemon_selection()
        elif i == 8:        # boss fight part 1 - Nidorino 
            ele_check = "normal"
            if attack_option == 1:
                attack_damage = random.randint(25, 40)
                ele_attack = "normal"
                spell_name = "Pound"
            elif attack_option == 2:
                attack_damage = random.randint(30, 35)
                ele_attack = "normal"
                spell_name = "Tackle"
            elif attack_option == 3:
                attack_damage = 4 * random.randint(7, 9)
                ele_attack = "normal"
                spell_name = "Flurry"
            else:
                pass
        elif i == 9:        # boss fight part 2 - Kadabra
            ele_check = "normal"
            if attack_option == 1:
                attack_damage = 2 * random.randint(10, 15)
                ele_attack = "normal"
                spell_name = "Double Jab"
            elif attack_option == 2:
                attack_damage = 4 * random.randint(5, 10)
                ele_attack = "normal"
                spell_name = "Flurry"
            elif attack_option == 3:
                attack_damage = 3 * random.randint(10, 12)
                ele_attack = "normal"
                spell_name = "Triple Kick"
            else:
                pass
        elif i == 10:       # boss fight part 3 - Hitmonchan
            ele_check = "normal"
            if attack_option == 1:
                attack_damage = 35
                ele_attack = "normal"
                spell_name = "Mach Punch"
            elif attack_option == 2:
                attack_damage = random.randint(20, 42)
                ele_attack = "normal"
                spell_name = "Low Sweep"
            elif attack_option == 3:
                attack_damage = 2 * random.randint(15, 17)
                ele_attack = "normal"
                spell_name = "Body Slam"
            else:
                pass
        else:
            print("not a pokemon")
    return spell_name, ele_attack, ele_check, attack_damage
# the same i == 1 comment applies to all version of i
# the last else check doesn't happen, "not a pokemon"
# returns the variables for battle() function

def type_check():
    global pet_name, ele_check, types
    j = pokemon_list.index(pet_name)
    ele_check = types[j]
    return ele_check
# checks just the type of the pokemon involved in the battle (due to it's position in battle() this is the one receiving the hit)
# sends back this updated value of ele_check to battle()



bulb_ascii = '''                                           
                        _,.------....___,.' ',.-.
                     ,-'          _,.--"        |
                   ,'         _.-'              .
                  /   ,     ,'                   `
                 .   /     /                     ``.
                 |  |     .                       \.
       ____      |___._.  |       __               \ `.
     .'    `---""       ``"-.--"'`  \               .  
    .  ,            __               `              |   .
    `,'         ,-"'  .               \             |    L
   ,'          '    _.'                -._          /    |
  ,`-.    ,".   `--'                      >.      ,'     |
 . .'    `-'       __    ,  ,-.         /  `.__.-      ,'
 ||:, .           ,'  ;  /  / \ `        `.    .      .'/
 j|:D  \          `--'  ' ,'_  . .         `.__, \   , /
/ L:_  |                 .  "' :_;                `.'.'
.    ""'                  """""'                    V
 `.                                 .    `.   _,..  `
   `,_   .    .                _,-'/    .. `,'   __  `
    ) \`._        ___....----"'  ,'   .'  \ |   '  \  .
   /   `. "`-.--"'         _,' ,'     `---' |    `./  |
  .   _  `""'--.._____..--"   ,             '         |
  | ." `. `-.                /-.           /          ,
  | `._.'    `,_            ;  /         ,'          .
 .'          /| `-.        . ,'         ,           ,
 '-.__ __ _,','    '`-..___;-...__   ,.'\ ____.___.'
 `"^--'..'   '-`-^-'"--    `-^-'`.''"""""`.,^.`.--' '''
squirtle_ascii = '''
               _,........__
            ,-'            "`-.
          ,'                   `-.
        ,'                        
      ,'                           .
      .'\               ,"".       `
     ._.'|             / |  `       
     |   |            `-.'  ||       `.
     |   |            '-._,'||       | 
     .`.,'             `..,'.'       , |`-.
     l                       .'`.  _/  |   `.
     `-.._'-   ,          _ _'   -" \  .     `
`."""""'-.`-...,---------','         `. `....__.
.'        `"-..___      __,'\          \  \     
\_ .          |   `""""'    `.           . \     
  `.          |              `.          |  .     L
    `.        |`--...________.'.        j   |     |
      `._    .'      |          `.     .|   ,     |
         `--,\       .            `7""' |  ,      |
            ` `      `            /     |  |      |    _,-'"""`-.
             \ `.     .          /      |  '      |  ,'          `.
              \  v.__  .        '       .   \    /| /              
               \/    `""  """"""`.       \   \  /.''                |
                `        .        `._ ___,j.  `/ .-       ,---.     |
                ,`-.      \         ."     `.  |/        j     `    |
               /    `.     \       /         \ /         |     /    j
              |       `-.   7-.._ .          |"          '         /
              |          `./_    `|          |            .     _,'
              `.           / `----|          |-............`---'
                \          \      |          |
               ,'           )     `.         |
                7____,,..--'      /          |
                                  `---.__,--.' '''
charmander_ascii = '''
              _.--""`-..
            ,'          `.
          ,'          __  `.
         /|          " __   
        , |           / |.   .
        |,'          !_.'|   |
      ,'             '   |   |
     /              |`--'|   |
    |                `---'   |
     .   ,                   |                       ,".
      ._     '           _'  |                    , ' \ `
  `.. `.`-...___,...---""    |       __,.        ,`"   L,|
  |, `- .`._        _,-,.'   .  __.-'-. /        .   ,    
-:..     `. `-..--_.,.<       `"      / `.        `-/ |   .
  `,         """"'     `.              ,'         |   |  ',,
    `.      '            '            /          '    |'. |/
      `.   |              \       _,-'           |       ''
        `._'               \   '"\                .      |
           |                '     \                `._  ,'
           |                 '     \                 .'|
           |                 .      \                | |
           |                 |       L              ,' |
           `                 |       |             /   '
            \                |       |           ,'   /
          ,' \               |  _.._ ,-..___,..-'    ,'
         /     .             .      `!             ,j'
        /       `.          /        .           .'/
       .          `.       /         |        _.'.'
        `.          7`'---'          |------"'_.'
       _,.`,_     _'                ,''-----"'
   _,-_    '       `.     .'      ,
   -" /`.         _,'     | _  _  _.|
    ""--'---"""""'        `' '! |! /
                            `" " - '''
def game_start():
    global char_name
    print("Choose your name, adventurer!")
    char_name=input()
    print(f"Are you sure {char_name} is your name?")
    x = input("[y/n] Yes or No\n").lower()
    if x == "y" or x == "yes" or x == "YES":
        print("Okay lets begin!")
        difficulty_choice()
    elif x == "n" or x == "no" or x == "NO":
        game_start()
    else:
        print("are you dumb?")
        game_start()
# this is to choose the character, and then the game begins

def difficulty_choice():
    global difficulty_select
    x = input("Choose a difficulty, Story [1], Hard [2], Insane [3] \n")
    x = x.lower()
    if x == "1" or x == "story":
        print("Story Mode selected")
        difficulty_select = 1
        intro()
    elif x == "2" or x == "hard":
        print("Hard mode selected")
        difficulty_select = 1.25
        intro()
    elif x == "3" or x == "insane":
        print("Insanity selected")
        difficulty_select = 1.5
        intro()
    else:
        print("Choose a correct difficulty")
        difficulty_choice()
    return difficulty_select


def intro():
    print("""                                  ,'
        _.----.        ____         ,'  _\   ___    ___     ____
    _,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.
    \      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |
     \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |
       \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |
        \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |
         \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |
          \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |
           \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |
            \_.-'       |__|    `-._ |              '-.|     '-.| |   |
                                    `'                            '-._|""")

    print("Welcome to the world of pokemon!")
    print("After 5 years of living in the big city with your father, you decided to return back to your old hometown where your mother Hanako lives.")
    print("Press enter to continue text.")
    input()
    print("You arrive and your mother greets you warmly, and you spend some time catching on up on how things have been over the years.")
    input()
    print('"I think you should go speak to some of the village members too, im sure they have missed you too!"')
    input()
    print("You venture off and catch up with some of the village elders, and a few kids you used to play with out in the fields back in the day, and decide to go play for a bit.")
    input()
    print('In the corner of your eye, you see bushes rumbling within a myterious forest and your curiosity peaks. "What could that be" you think to yourself, and decide to head this way.')
    input()
    print("You follow the bushes for a while, and end up lost in the forest with no clue on how to get back.")
    input()
    print('"ARGGHHHHH"')
    input()
    print('"What was that" you thought to yourself as you heard someone who sounded like they were in danger. Do you Go towards the Danger?')
    danger_event()
# danger event triggers

def danger_event():
    x = input("[y/n] Yes or No\n")
    if x == "y" or x == "yes" or x == "YES":
        print("You chose yes")
        danger_yes()
    elif x == "n" or x == "no" or x == "NO":
        print("You chose no")
        danger_no()
    else:
        print("Answer yes or no [y/n]")
        danger_event()
# choose yes or no to decide if you go towards the danger

def danger_yes():
    print("You head towards the source and find an old scientist , holding on to a silver briefcase as he runs from a rather agressive looking creature.")
    input()
    print("The scientist trips over a tree branch and lands facefirst in front of you, the briefcase flew out of his hand")
    input()
    print('"hey you, grab that suitcase and take one of the balls out"')
    input()
    print("You open the suitcase and find an 3 interesting looking balls, it was coloured half white, half red with a peculiar button in the middle.")
    input()
    print('"Choose one, press it and throw it towards the Pokemon" the scientist urged "Those balls contain a Pokemon inside, we will need one to battle off our opponent."')
    input()
    print('"Pokemon? is that what they are called" you thought to yourself')
    input()
    print("You take a brief look and see that below the Pokemon are the names of each Pokemon")
    input()
    print("It is now time to select your Pokemon. You can choose between Squirtle, Charmander or Bulbasaur.")
    pokemon_select()
# function for choosing yes - leads to pokemon selection

def danger_no():
    print("Due to fear, you run off and find yourself lost even further within the woods.")
    input()
    print("You keep running and you eventually bump into an old scientist who was quite surprised to see a young person alone in the woods")
    input()
    print('He was holding a silver suitcase, which peaks your interest. "Are you lost?" He says. ')
    input()
    print("Once again you a hear loud noise and this time its very close.")
    input()
    print('"That sounds like trouble" the old scientist says, whilst unboxing his suitcase.')
    input()
    print('"Choose one, press it and throw it towards the Pokemon" the scientist urged "Those balls contain a Pokemon inside, we will need one to battle off our opponent."')
    input()
    print('"Pokemon? is that what they are called" you thought to yourself')
    input()
    print("You take a brief look and see that below the Pokemon are the names of each Pokemon")
    input()
    print("It is now time to select your Pokemon. You can choose between Squirtle, Charmander or Bulbasaur.")
    pokemon_select()
# function for choosing no - leads to pokemon selection too

def pokemon_select():
    global pokemon_list, user_name, pokemon_choose, is_npc_battle, pet_one_name
    pokemon_choose = input("Choose your Pokemon from the 3 balls:\n")
    if pokemon_choose == "bulbasaur" or pokemon_choose == "Bulbasaur":
        print("You have chosen the grass type, Bulbasaur! ")
        print(bulb_ascii)
        user_name = "Bulbasaur"
    elif pokemon_choose == "squirtle" or pokemon_choose == "Squirtle":
        print("You have chosen the water type, Squirtle! ")
        print(squirtle_ascii)
        user_name = "Squirtle"
    elif pokemon_choose == "charmander" or pokemon_choose == "Charmander":
        print("You have chosen the fire type pokemon, Charmander! ")
        print(charmander_ascii)
        user_name = "Charmander"
    else:
        print("Please choose a Pokemon")
        pokemon_select()
    pet_one_name = user_name
    is_npc_battle = False
    initial_conditions()
    scientist_save()
    return user_name, pet_one_name
# Choose from the three starter pokemon from the list
def xp_gain():
    global current_xp , xp_points
    xp_points = random.randint(50,60)
    current_xp += xp_points
    if current_xp >= 450:
        print(f"Level 10: You gained {xp_points} experience") 
    elif current_xp >= 400:
        print(f"Level 9: You gained {xp_points} experience") 
    elif current_xp >= 350:
        print(f"Level 8: You gained {xp_points} experience") 
    elif current_xp >= 300:
        print(f"Level 7: You gained {xp_points} experience") 
    elif current_xp >= 250:
        print(f"Level 6: You gained {xp_points} experience") 
    elif current_xp >= 200:
        print(f"Level 5: You gained {xp_points} experience") 
    elif current_xp >= 150:
        print(f"Level 4: You gained {xp_points} experience") 
    elif current_xp >= 100:
        print(f"Level 3: You gained {xp_points} experience") 
    elif current_xp >= 50:
        print(f"Level 2: You gained {xp_points} experience") 
    else:
        print(f"Level 1: You have gained {xp_points} experience")
    return current_xp


def stat_gain():
    global current_xp , damage , max_hp
    damage = 0
    max_hp = 50
    if current_xp >= 450:
        damage = damage + 45 
        max_hp = max_hp + 180
    elif current_xp >= 400:
        damage = damage + 40  
        max_hp = max_hp + 160
    elif current_xp >= 350:
        damage = damage + 35  
        max_hp = max_hp + 140
    elif current_xp >= 300:
        damage = damage + 30 
        max_hp = max_hp + 120
    elif current_xp >= 250:
        damage = damage + 25 
        max_hp = max_hp + 100
    elif current_xp >= 200:
        damage = damage + 20 
        max_hp = max_hp + 80
    elif current_xp >= 150:
        damage = damage + 15 
        max_hp = max_hp + 60
    elif current_xp >= 100:
        damage = damage + 10 
        max_hp = max_hp + 40
    elif current_xp >= 50:
        damage = damage + 5 
        max_hp = max_hp + 20
    else:
        print()
    return damage and max_hp

def scientist_save():
    global pokemon_name, user_hp, max_hp, pet_one_hp, pet_two_hp, hyper_potion
    print("Thanks for saving me, I would have used the pokemon myself but they dont answer to me.")
    input()
    print(f'"It seems like that {pokemon_choose} has taken a liking to you. You can keep it"')
    input()
    print('"Follow me to my lab i will heal your pokemon up as a thanks. My name is Proffesor Elm. Whats your name friend?"')
    input()
    print(char_name)
    input()
    print(f"You head back to the lab and Prof.Elm heals your {pokemon_choose} back to full health")
    input()
    print('"You should give your pokemon a name, what will you call him?"')
    pokemon_name = input(f"Choose {pokemon_choose}'s name:\n")
    print(f'"An interesting name choice. Here, take this pokeball so you can keep {pokemon_name} safe"')
    input()
    print('"Also here, before i send you off, i have some information for you, since you seemed to be confused about pokemon"')
    input()
    print('"Pokemon are quite common in this area, i guess its new to you if you came from the big city, but thats okay."')
    input()
    print('"Its become very popular to catch all types of pokemon and people train them up so they can compete in tournaments and many other cool events"')
    input()
    print('"Ill tell you just this much, and let you find out for yourself, but as a start, you should head to Johto"')
    input()
    print('"In Johto you will find plenty of pokemon trainers to battle and gain experience so you can take on Gym leaders, who are known to be the strongest trainers in the region"')
    input()
    print(f'"Take these three healing potions and this map should help you find your way. Its been a pleasure meeting you and i wish you the best on your journey, {char_name}."')
    input()
    print("After that talk with Prof.Elm, you are incredibly excited to set off on your new adventure, but")
    input()
    print("you remember that you might want to tell your mother you are leaving again, at least for a little while.")
    input()
    user_hp = max_hp
    pet_one_hp = max_hp
    if pet_two_name == " ":
        pass
    else:
        pet_two_hp = max_hp
    hyper_potion = 3
    print("Do you choose to")
    print("1: go and say goodbye to your mother, Hanako or")
    print("2: Go straight towards Johto")
    johto()
    return user_hp, max_hp, pet_one_hp, pet_two_hp
# choose to go to mother or straight to johto - activates function

def johto():
    global home_or_not
    home_or_not = input("Choose 1 or 2:\n")
    if home_or_not == "1" :
        print("You chose to say goodbye to Hanako")
        bye_hanako()
    elif home_or_not == "2" :
        print("You chose to head to johto instantly, heartless choice")
        go_johto()
    else:
        johto()
# function for saying goodbye to mother or leaving for johto - leads to bye_hanako or go_johto function

def bye_hanako():
    global user_hp, max_hp, hyper_potion, pet_two_hp
    print("Before you set off to a new region, you decide to say goodbye to your mother, Hanako as you have only just got into the town and now you are leaving again.")
    input()
    user_hp = max_hp
    if pet_two_name == " ":
        pass
    else:
        pet_two_hp = max_hp
    print(f"Once you arrive, you greet Hanako with your new Pokemon and she looks at {pokemon_name} with a smile")
    input()
    print(f'"It seems you have come across the various pokemon in our area already, {char_name}"')
    input()
    print("You inform your mother as to everything that has happened since you got back")
    input()
    print('"I was wondering why you got back so late, well at least you are okay, and im glad you found Prof.Elm when you did cause those pokemon can be quite violent"')
    input()
    print("You then proceed to tell her that you will be leaving to explore Johto and aim to become a top tier pokemon trainer")
    input()
    print('"Well it hasnt been long but im glad to see your face again, I wish you the best on your travels and you do your best!"')
    print('"Here, take this potion, it will restore your pokemon to full if they faint.')
    input()
    print("You thank Hanako for the potion and prepare to kickstart your journey")
    input()
    print('"Goodbye mum, once im back ill be the top pokemon trainer around!"')
    hyper_potion = hyper_potion + 1
    go_johto()
    return user_hp, max_hp, hyper_potion
# function for saying bye to your mother - leads to go_johto function

def go_johto():
    print("You make a headstart on your journey, following your maps directions down a peaceful road.")
    input()
    print("After about 30 minutes of walking, you spot a young man swinging a large net across grass nearby a small river.")
    input()
    print("He notices you and signals you to come over.")
    input()
    print('"Hi there, are you by any chance a pokemon trainer? wanna challenge me?"')
    input()
    print("Do you see this as an opportunity to train your pokemon up. You feel you might need the experience to challenge the gym leader later on.")
    challenge()
# function for going to johto - triggers second challenge vs bug catcher

def challenge():
    global is_npc_battle
    x = input("Choose 1 to fight, and choose 2 to avoid:\n")
    if x == "1":
        print('"I am indeed, lets fight!"')
        is_npc_battle = True
        initial_conditions()
        johto_city()
    elif x == "2":
        print('"Im sorry, im a little busy at the moment"')
        input()
        print('"Ahhh, well if you ever change your mind, dont hesitate to find me, i love a good challenge!"')
        johto_city()
    else:
        print("Choose 1 or 2")
        challenge()
    return is_npc_battle
# Choose to fight bug catcher or not - leads to battle() or johto_city

def johto_city():
    global user_hp, max_hp, pet_one_hp, pet_two_hp
    print("After this, you continue on your path towards Johto and arrive not long after")
    input()
    print("While in johto, you heal up your pokemon at the pokecenter so they are back to good health")
    input()
    user_hp = max_hp
    pet_one_hp = max_hp
    if pet_two_name == " ":
        pass
    else:
        pet_two_hp = max_hp
    print("Before you leave, a friendly trainer signals you for a chat")
    input()
    print("He noticed you seemed quite new to the whole pokemon scene and gives you some advice")
    input()
    print('"So you plan to fight the gym leader hmmmm, well i reccomend going to get your pokemon levelled a bit more beforehand."')
    input()
    print('"The gym leader, Gus is very tough, and he uses two very strong pokemon, Nidorino and Hitmonchan."')
    input()
    print('"They are both normal types, so super effective bonuses will not work, which is why you need to level your pokemon up first"')
    input()
    print("You thank him for the advice, and now its up to you to decide, do you want to level up more or head straight to the gym leader?")
    xp_or_gym()
    return user_hp, max_hp, pet_one_hp, pet_two_hp
# choice to gain xp (fight more pokemon) or go straight to gym with function xp_or_gym


def xp_or_gym():
    global user_hp, max_hp, first_time, is_npc_battle
    is_npc_battle = False
    if first_time == True:
        x = input("Choose 1 to gain more xp, 2 to go straight to Gus:\n")
        if x == "1":
            print ("You head off into the wild to find pokemon to fight and level up")
            initial_conditions()
            first_time = False
        elif x == "2":
            print("You head straight to Gus, but you realise this was soon a mistake, as you lose instantly")
            input()
            print("You go back to the pokemon center to heal your pokemon back up")
            input()
            print("Realising that you made a bad choice, you then proceed to level up your pokemon before going back to challenge Gus")
            initial_conditions()
            first_time = False
        else:
            print("Choose 1 or 2")
        xp_or_gym()
    else:
        b = input("Choose 1 to gain more xp, 2 to go to Gus:\n")
        if b == "1":
            print("You decide for another fight")
            initial_conditions()
            xp_or_gym()
        elif b == "2":
            gym_battle()
        else:
            print("Choose 1 or 2")
            xp_or_gym()
    return user_hp, max_hp, is_npc_battle
# leads to function battle (5 times)

def gym_battle():
    global boss_fight, user_hp, max_hp, is_npc_battle, pet_one_hp, pet_two_hp
    print("After leveling for a while, you heal your pokemon back to full before heading the the gym to fight Gus")
    input()
    user_hp = max_hp
    pet_one_hp = max_hp
    if pet_two_name == " ":
        pass
    else:
        pet_two_hp = max_hp
    is_npc_battle = True
    print("You arrive, feeling more confident now you have trained, and the battle begins")
    input()
    boss_fight = 1
    initial_conditions()
    boss_fight = 2
    initial_conditions()
    boss_fight = 3
    initial_conditions()
    gus_battle()
    return user_hp, max_hp, is_npc_battle, pet_one_hp, pet_two_hp
# triggers boss fight with function gus_battle 

def gus_battle():
    print('"You are promising kid, i wish you the best in future, heres your badge. You earned it"')
    input()
    print('"its best you head to the city next to here, there will be another gym leader in that area rearing to go, but shes even stronger than me"')
    input()
    print(f'"Good luck {char_name} in your future travels."')
    input()
    end_game()
# function that completes the game and puts you on the endgame screen

def end_game():
    print("Thanks for playing, i hope you enjoyed!")
    print("")
    print('''                                             ,-.
                                          _.|  '
                                        .'  | /
                                      ,'    |'
                                     /      /
                       _..----""---.'      /
 _.....---------...,-""                  ,'
 `-._  \                                /
     `-.+_            __           ,--. .
          `-.._     .:  ).        (`--"| 
               7    | `" |         `...'  
               |     `--'     '+"        ,". ,""-
               |   _...        .____     | |/    '
          _.   |  .    `.  '--"   /      `./     j
         \' `-.|  '     |   `.   /        /     /
         '     `-. `---"      `-"        /     /
          \       `.                  _,'     /
           \        `                        .
            \                                j
             \                              /
              `.                           .
                +                          
                |                           L
                |                           |
                |  _ /,                     |
                | | L)'..                   |
                | .    | `                  |
                '  \'   L                   '
                 \  \   |                  j
                  `. `__'                 /
                _,.--.---........__      /
               ---.,'---`         |   -j"
                .-'  '....__      L    |
              ""--..    _,-'       \ l||
                  ,-'  .....------. `||'
               _,'                /
             ,'                  /
            '---------+-        /
                     /         /
                   .'         /
                 .'          /
               ,'           /
             _'....----""""" ''')
    print('''
  .▀█▀.█▄█.█▀█.█▄.█.█▄▀　█▄█.█▀█.█─█
  ─.█.─█▀█.█▀█.█.▀█.█▀▄　─█.─█▄█.█▄█''')

    endless_loop()
# finishing function

def endless_loop():
    global battle_count, game_over, boss_fight, end_scaling, is_npc_battle
    boss_fight = 0
    c = input(f"Do you wish to keep playing? [y/n]")
    if c == "y" or c == "yes" or c == "YES":
        end_scaling += 10
        print("You chose yes, so brave")
        battle_count = 0
        is_npc_battle = True
        while game_over == False:
            print(f"So far you've won an extra {battle_count} battles")
            initial_conditions()
    elif c == "n" or c == "no" or c == "NO":
        print("Aww too bad")
    else:
        print("Answer yes or no [y/n]")
    return end_scaling, battle_count

game_start()
