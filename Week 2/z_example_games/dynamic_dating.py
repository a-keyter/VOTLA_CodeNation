#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# List of Library imports
import time
from time import sleep
import sys
import random

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# List of Variables

player_name = ""
li_name = ""

relation_points = 0 # Dictates which ending we get. Based on answers given, good and bad.

choice = 0 # Tells events which option the player picked.

Yes_No = ""

player_dialogue_1 = ""
player_dialogue_2 = ""
player_dialogue_3 = ""
player_dialogue_4 = ""

li_dialogue_1 = ""
li_dialogue_2 = ""
li_dialogue_3 = ""
li_dialogue_4 = ""

option_display_1 = ""
option_display_2 = ""
option_display_3 = ""
option_display_4 = ""

left_right = ""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# List of Lists


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# List of Dictionaries


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Non-Event functions

def rp_notification():

    print()
    print()
    rpdisplay = f"You have a total of ▂▃▅▇█▓▒░۩۞۩  {relation_points}  ۩۞۩░▒▓█▇▅▃▂   relation points!"
    for char in rpdisplay:
            sleep(0.03)
            sys.stdout.write(char)
            sys.stdout.flush()

def input_choice_1_to_4():
    global choice
    message = "Choose an option between 1 and 4: "
    for char in message:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
    print()
    choice = input()
    if choice == "1" or choice == "2" or choice == "3" or choice == "4":
        pass
    else:
        print()
        input_choice_1_to_4()

def input_choice_1_to_3():
    global choice
    message = "Choose an option between 1 and 3: "
    for char in message:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
    print()
    choice = input()
    if choice == "1" or choice == "2" or choice == "3":
        pass
    else:
        print()
        input_choice_1_to_3()

def input_choice_1_to_2():
    global choice
    message = "Choose an option between 1 and 2: "
    for char in message:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
    print()
    choice = input()
    if choice == "1" or choice == "2":
        pass
    else:
        print()
        input_choice_1_to_2()

def reset_choice():
    global choice
    choice = 0

def name_choice():

    global player_name
    global Yes_No

    nchoicetext1 = """
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    |                                        |
    |      Please enter your first name      |
    |         so we can begin your           |
    |          dating adventure ;)           |
    |                                        |
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    ENTER FIRST NAME HERE: """
    for char in nchoicetext1:
        sleep(0.01)
        sys.stdout.write(char)
        sys.stdout.flush()
    
    player_name = input("").strip().lower().capitalize()
    print()
    nchoicetext2 = f"Your name is {player_name}? (Please input Yes or No):"
    for char in nchoicetext2:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
    print()
    print()
    Yes_No = input().strip().capitalize()
    if Yes_No == "Yes":
        print()
        print()
        message = f"Welcome, {player_name}! Finding you your potential new partner..."
        for char in message:
            sleep(0.03)
            sys.stdout.write(char)
            sys.stdout.flush()
        print()
        print()
        time.sleep(1)
        print("...")
        print()
        time.sleep(1)
        print("...")
        print()
        time.sleep(1)
        print("...")
        print()
        message = "Match found!"
        for char in message:
            sleep(0.03)
            sys.stdout.write(char)
            sys.stdout.flush()
        print()
        print()
        print()
        pass
    else:
        print()
        print()
        name_choice()

def display_dialogue_1_to_4():
    print()
    print()
    if choice == "1":
        for char in player_dialogue_1:
            sleep(0.05)
            sys.stdout.write(char)
            sys.stdout.flush()
        print("")
        print("")
        for char in li_dialogue_1:
            sleep(0.05)
            sys.stdout.write(char)
            sys.stdout.flush()

    elif choice == "2":
        for char in player_dialogue_2:
            sleep(0.05)
            sys.stdout.write(char)
            sys.stdout.flush()
        print("")    
        print("")    
        for char in li_dialogue_2:
            sleep(0.05)
            sys.stdout.write(char)
            sys.stdout.flush()

    elif choice == "3":
        for char in player_dialogue_3:
            sleep(0.05)
            sys.stdout.write(char)
            sys.stdout.flush()
        print("")    
        print("")    
        for char in li_dialogue_3:
            sleep(0.05)
            sys.stdout.write(char)
            sys.stdout.flush()

    else:
        for char in player_dialogue_4:
            sleep(0.05)
            sys.stdout.write(char)
            sys.stdout.flush()
        print("")    
        print("")    
        for char in li_dialogue_4:
            sleep(0.05)
            sys.stdout.write(char)
            sys.stdout.flush()

def display_dialogue_1_to_3():
    print()
    print()
    if choice == "1":
        for char in player_dialogue_1:
            sleep(0.05)
            sys.stdout.write(char)
            sys.stdout.flush()
        print("")
        print("")
        for char in li_dialogue_1:
            sleep(0.05)
            sys.stdout.write(char)
            sys.stdout.flush()

    elif choice == "2":
        for char in player_dialogue_2:
            sleep(0.05)
            sys.stdout.write(char)
            sys.stdout.flush()
        print("")
        print("")
        for char in li_dialogue_2:
            sleep(0.05)
            sys.stdout.write(char)
            sys.stdout.flush()

    else:
        for char in player_dialogue_3:
            sleep(0.05)
            sys.stdout.write(char)
            sys.stdout.flush()
        print("")    
        print("")    
        for char in li_dialogue_3:
            sleep(0.05)
            sys.stdout.write(char)
            sys.stdout.flush()

def display_dialogue_1_to_2():
    print()
    print()
    if choice == "1":
        for char in player_dialogue_1:
            sleep(0.05)
            sys.stdout.write(char)
            sys.stdout.flush()
        print("")
        print("")
        for char in li_dialogue_1:
            sleep(0.05)
            sys.stdout.write(char)
            sys.stdout.flush()

    else:
        for char in player_dialogue_2:
            sleep(0.05)
            sys.stdout.write(char)
            sys.stdout.flush()
        print("")    
        print("")    
        for char in li_dialogue_2:
            sleep(0.05)
            sys.stdout.write(char)
            sys.stdout.flush()

def display_options_1_to_4():
    for char in option_display_1:
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("")
    print("")
    for char in option_display_2:
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("")
    print("")
    for char in option_display_3:
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("")
    print("")
    for char in option_display_4:
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()

def display_options_1_to_3():
    for char in option_display_1:
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("")
    print("")
    for char in option_display_2:
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()  
    print("")
    print("")
    for char in option_display_3:
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()  

def display_options_1_to_2():
    for char in option_display_1:
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("")
    print("")
    for char in option_display_2:
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()        

def swipe_choice():

    global left_right

    message = "Will you swipe left or right?"
    for char in message:
            sleep(0.03)
            sys.stdout.write(char)
            sys.stdout.flush()
    print()
    print()
    left_right = input("INPUT LEFT OR RIGHT: ").lower().capitalize()
    if left_right == "Left":
        pass
    elif left_right == "Right":
        pass
    else:
        swipe_choice()

def display_profile_1():
    print("""
                _____    ____
             .#########.#######..
          .#######################.
        .############################.
       .################################.
      .#########,##,#####################.
     .#########-#,'########## ############.
    .######'#-##' # ##'### #. `####:#######.
    #####:'# #'###,##' # # +#. `###:':######
   .####,'###,##  ###  # # #`#. -####`######.
  .####+.' ,'#  ##' #   # # #`#`.`#####::####
  ####'    #  '##'  #   #_'# #.## `#######;##
  #:##'      '       #   # ``..__# `#######:#
  #:##'  .#######s.   #.  .s######.\`#####:##
  #:##   ."______""'    '""_____"". `.#####:#
 .#:##   ><'(##)'> )    ( <'(##)`><   `####;#
 ##:##  , , -==-' '.    .` `-==- . \  ######'
 #|-'| / /      ,  :    : ,       \ ` :####:'
 :#  |: '  '   /  .     .  .  `    `  |`####
 #|  :|   /   '  '       `  \   . ,   :  #:# 
 #L. | | ,  /   `.-._ _.-.'   .  \ \  : ) J##
 ##\ `  /  '                   \  : : |  /##
 ## #|.:: '       _    _        ` | | |'####
 #####|\  |  (.-'.__`-'__.`-.)   :| ' ######
 ######\:      `-...___..-' '     :: /######
 #######\``.                   ,'|  /#######
 # ######\  \       ___       / /' /#######
 ##'#####|\  \    -     -    /  ,'|### #. #.
 `# #####| '-.`             ' ,-'  |### #  #
    #' `#|    '._         ,.-'     #`#`#.
         |       .'------' :       |#   #
         |       :         :       |
         |       :         :       |
                 :         :            """)

    profile1 ="""
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    |                                        |
    |            Name: John Smith            |
    |                Age: 38                 |
    |                                        |
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """
    for char in profile1:
        sleep(0.01)
        sys.stdout.write(char)
        sys.stdout.flush()
    print()
    swipe_choice()
    print()
    print()
    print()
    if left_right == "Left":
        message = "You have chosen to swipe left. Finding you your potential new partner..."
        for char in message:
            sleep(0.03)
            sys.stdout.write(char)
            sys.stdout.flush()
        print()
        print()
        time.sleep(1)
        print("...")
        print()
        time.sleep(1)
        print("...")
        print()
        time.sleep(1)
        print("...")
        print()
        print()
        message = "Match found!"
        for char in message:
            sleep(0.03)
            sys.stdout.write(char)
            sys.stdout.flush()
        print()
        print()
        print()
        display_profile_2()
    else: 
        global li_name
        li_name = "John Smith"
        message = f"You have found your new potential partner {li_name}! Connecting you now..."
        for char in message:
            sleep(0.03)
            sys.stdout.write(char)
            sys.stdout.flush()
        print()
        print()
        time.sleep(1)
        print("...")
        print()
        time.sleep(1)
        print("...")
        print()
        time.sleep(1)
        print("...")
        print()
        print()
        message = "Connected. Say something nice - And always remember staff will not ask you for your password!"
        for char in message:
            sleep(0.03)
            sys.stdout.write(char)
            sys.stdout.flush()
        text1()

def display_profile_2():
    print("""
              _...._
         _.dMMMMMMMMMb.
     ..dMMMMMMMMMMMMMMMb
   .dMMMMMMMMMMMMMMMMMMMMb.
  dMMMMMMMMMMMMMMMMMMMMMMMM.
  MMMMMMMP'`YMMMMMMMMMMMMMMMb
  MMMMMMP    MMMMMMMMMMMMMMMM
 dMMMMMP     `MMMMMMMMMMMMMMMb
 MMMMMM~=,,_  `MMMMMMMMMMMMMMM
 MMMMMMP,6;    `MMMMMMMMMMMMMMb
 MMMMMM|         ```^YMMMMMMMMM
 MMMMMM:   -~        / |MMMMMMMb
 `MMMMM/\  _.._     /  |MMMMMMMM
   `YMM\_`.`~--'    \__/MMMMMMMM!
     MMMMMM\       _.' _sS}MMMMMb
     `YMMMMMb.__.sP.---.  MMMMMMM
       ``YMMMMMMMP'        \MMMMMb
           ``MMMd;          MMMMMM
               dP|          :MMMMMb.
           _.sP'             :MMMMMM
       _.s888P'   ,  .-. .-. |MMMMM}
    .s888888P    ,_|(  fsc  )|MMMM
  .d88888888;     `\ `-._.-' ;;M'
  8888888888|       :         :;,
  8888888888;       |         |`;,_
  `Y88888888b     _,:         |/Y\;
     `^Y88888ssssSP~":        ;SsP/
         "" \        |         ;
             ;       |         |
             ;       ;         |
            /      .'          |
          .'    .-'            ;
         /_...-'             .':
        .'              _..-'   :
       /         __.--""         :""")

    profile2 ="""
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    |                                        |
    |             Name: Jane Doe             |
    |                Age: 22                 |
    |                                        |
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """
    for char in profile2:
        sleep(0.01)
        sys.stdout.write(char)
        sys.stdout.flush()
    swipe_choice()
    print()
    print()
    print()
    if left_right == "Left":
        message = "You have chosen to swipe left. Finding you your potential new partner..."
        for char in message:
            sleep(0.03)
            sys.stdout.write(char)
            sys.stdout.flush()
        print()
        print()
        time.sleep(1)
        print("...")
        print()
        time.sleep(1)
        print("...")
        print()
        time.sleep(1)
        print("...")
        print()
        print()
        message = "Match found!"
        for char in message:
            sleep(0.03)
            sys.stdout.write(char)
            sys.stdout.flush()
        print()
        print()
        print()
        display_profile_3()
    else: 
        global li_name
        li_name = "Jane Doe"
        message = f"You have found your new potential partner {li_name}! Connecting you now..."
        for char in message:
            sleep(0.03)
            sys.stdout.write(char)
            sys.stdout.flush()
        print()
        print()
        time.sleep(1)
        print("...")
        print()
        time.sleep(1)
        print("...")
        print()
        time.sleep(1)
        print("...")
        print()
        print()
        message = "Connected. Say something nice - And always remember staff will not ask you for your password!"
        for char in message:
            sleep(0.03)
            sys.stdout.write(char)
            sys.stdout.flush()
        text1()

def display_profile_3():
    print("""          ,     ,  ._  ,
                _.MMmm.mMm_Mm.MMm_:mMMmmm.._  .
           _ .-mmMMMMMMMMMMMMm:MMm:MMMMMMMMMm._
            `-.mm.MMMMMMM:MMMMMMMmmMMMMMMMMMmm._
         _.mMMMMMmMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM"~.
          .MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm._
         _.MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm._
      ..mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmmm.
     _.mmMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm.
      _.MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm_
  .mmMMMMMMMMMMMMMMMMMMMMMMMM' `MMMMMMMMMMMMMMMMMMMMMMm,
 _.-' _.mMMMMMMMMMMMMMMMMMMM'      `MMMMMMMMMMMMMMMM""`
  _,MMMmMMMMMMMMMMMMMMMM'            `MMMMMMMMMMMMMMmm.
    _.-'MMMMMMMMMMMMMMM.'""`.    ,'""`.MMMMMMMMMMMMMMMM.
   .mmMMMMMMMMMMMMMMMM' <(o)>`  '<(o)>` MMMMMMMMMMMMMMMm.
      .MMMMMMMMMMMMMMM                 'MMMMMMMMMMMMMMM:
   ,MMMmMMMMMMMMMMMMM'                 `MMMMMMMMMMMMmm.
  ,ME:MMMMMMMMMMMMMM_6       -  -       7_MMMMMMMMM:Mm_
  !M:MmmMMMMMMMMMMMMML_                _JMMMMMMMMMm:MMm.
  '':mMMMMMMMMMMMMMMMM\     ______     /dMMMMMMMMMMM:'Mm.
   ':MMM:MMMMMMMMMMMMMM\    `.__.'    /MMMMMM:MMMMMMm: `
  .M:MMM:MMMMMMMMMMMMMMM`.          ,'MMMMMMM:MMMMMMMm
    .Mm:mMMMMMMMMMMMMMMM| `.      .' |MMMMMMm:.MMMMM.
   .Mm:mMMMMMMMMMMMMMMMM|   `----':: |MMMMMMMmm`MMMMMm.
     !:mMMMMMMMMMMMMMMMM|      ::::. |MMMMMMMMMMM``mMm.
       !MMMMMMMMM'MMMMMM|      .:::. |MMMMMMMMMMMMM.._
       MMMMMMMMM'MMMM'M/       ::::'  \MMMMMMMMMMMMMMm,
      .mMMMMMMM'MMMM'MMm.       '     .`".MMMMMMMMMMMMm.
       !!JmMMM'MMM' `M:.      ,  ,     .. M.".MMMMMMMMm.
        FMMMMMm.`M   M..              .. `Mm   `"".MMMmm.
        MMMM'    M      ..           ..    `M      MM`.M!
        Mm'               ..        ..      M      M'   :
        /                                                \ """)

    profile1 ="""
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    |                                        |
    |           Name: Charlie Swift          |
    |                Age: 27                 |
    |                                        |
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """
    for char in profile1:
        sleep(0.01)
        sys.stdout.write(char)
        sys.stdout.flush()
    swipe_choice()
    print()
    print()
    print()
    if left_right == "Left":
        message = "You have chosen to swipe left. Finding you your potential new partner..."
        for char in message:
            sleep(0.03)
            sys.stdout.write(char)
            sys.stdout.flush()
        print()
        print()
        time.sleep(1)
        print("...")
        print()
        time.sleep(1)
        print("...")
        print()
        time.sleep(1)
        print("...")
        print()
        print()
        message = "Match found!"
        for char in message:
            sleep(0.03)
            sys.stdout.write(char)
            sys.stdout.flush()
        print()
        print()
        print()
        display_profile_1()
    else: 
        global li_name
        li_name = "Charlie Swift"
        message = f"You have found your new potential partner {li_name}! Connecting you now..."
        for char in message:
            sleep(0.03)
            sys.stdout.write(char)
            sys.stdout.flush()
        print()
        print()
        time.sleep(1)
        print("...")
        print()
        time.sleep(1)
        print("...")
        print()
        time.sleep(1)
        print("...")
        print()
        print()
        message = "Connected. Say something nice - And always remember staff will not ask you for your password!"
        for char in message:
            sleep(0.03)
            sys.stdout.write(char)
            sys.stdout.flush()
        text1()

def check_ending():
    message = f"You have earned a total of ▂▃▅▇█▓▒░۩۞۩ {relation_points} relationship points ۩۞۩░▒▓█▇▅▃▂"
    for char in message:
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()
    if relation_points <=149:

        message = "▂▃▅▇█▓▒░۩۞۩ Disaster..! You got the bad ending! ۩۞۩░▒▓█▇▅▃▂"
        for char in message:
            sleep(0.05)
            sys.stdout.write(char)
            sys.stdout.flush()
        print()
        print()
        bad_ending()
    else:
        message = "▂▃▅▇█▓▒░۩۞۩ Congratulations! You got the good ending! ۩۞۩░▒▓█▇▅▃▂"
        for char in message:
            sleep(0.05)
            sys.stdout.write(char)
            sys.stdout.flush()
        print()
        print()
        good_ending()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Event Functions

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Run the game. 

def run_game():
    displaywelcome ="""
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    |                                        |
    |     Welcome to Dynamic Dating, a       |
    |  'realistic' Tinder Dating Simulator.  |
    |                                        |
    |    Press the enter key to continue.    |
    |                                        |
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """
    for char in displaywelcome:
        sleep(0.01)
        sys.stdout.write(char)
        sys.stdout.flush()
    input()
    name_choice()
    display_profile_1()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Texting Event 1 Part 1s

def text1():
    
    global player_dialogue_1
    global player_dialogue_2
    global player_dialogue_3
    global player_dialogue_4
    global li_dialogue_1
    global li_dialogue_2
    global li_dialogue_3
    global li_dialogue_4
    global option_display_1
    global option_display_2
    global option_display_3
    global option_display_4

    print("")
    print("")
    option_display_1 = "1. Hi, nice to meet you"  #Start of game dialogue goes here
    option_display_2 = "2. You're well fit"
    option_display_3 = "3. I really hoped we'd match"
    option_display_4 = "4. I love your tattoo"
    print("")
    print("")
    display_options_1_to_4()
    print("")
    print("")
    input_choice_1_to_4()
    if choice == "1":
        player_dialogue_1 = f"{player_name}: Hi, nice to meet you"
        li_dialogue_1 = f"{li_name}: Nice to meet you too. How are you?"
        display_dialogue_1_to_4()
        text1_coversation1_part1()

    elif choice == "2":
        player_dialogue_2 = f"{player_name}: You're well fit"
        li_dialogue_2 = f"{li_name}: You look good to me!"
        display_dialogue_1_to_4()
        text1_coversation2_part1()

    elif choice == "3":
        player_dialogue_3 = f"{player_name}: I really hoped we'd match"
        li_dialogue_3 = f"{li_name}: Oh I didn’t expect someone like you to choose me"
        display_dialogue_1_to_4()
        text1_coversation3_part1()

    else:
        player_dialogue_4 = f"{player_name}: I love your tattoo"
        li_dialogue_4 = f"{li_name}: Have you got any?"
        display_dialogue_1_to_4()
        text1_coversation4_part1()

def text1_coversation1_part1():

    global player_dialogue_1
    global player_dialogue_2
    global li_dialogue_1
    global li_dialogue_2
    global option_display_1
    global option_display_2
    global relation_points

    print("")
    print("")
    option_display_1 = "1.	Really nervous - my insides are churning!"
    option_display_2 = "2.	I was wondering if you had an extra heart? Mine was just stolen!"
    display_options_1_to_2()
    print("")
    print("")
    input_choice_1_to_2()
    if choice == "1":
        player_dialogue_1 = f"{player_name}: Really nervous - my insides are churning!"
        li_dialogue_1 = f"{li_name}: What are your hobbies?"
        relation_points += 2
        display_dialogue_1_to_2()
        text1_coversation1_part2()

    else:
        player_dialogue_2 = f"{player_name}: I was wondering if you had an extra heart? Mine was just stolen! "
        li_dialogue_2 = f"{li_name}: What are your hobbies?"
        relation_points += 5
        display_dialogue_1_to_2()
        text1_coversation1_part2()
    
def text1_coversation2_part1():

    global player_dialogue_1
    global player_dialogue_2
    global li_dialogue_1
    global li_dialogue_2
    global option_display_1
    global option_display_2
    global relation_points

    print("")
    print("")
    option_display_1 = "1.	You’re hotter than the bottom of my laptop"
    option_display_2 = "2.	My appearance is the most important thing to me"
    display_options_1_to_2()
    print("")
    print("")
    input_choice_1_to_2()
    if choice == "1":
        player_dialogue_1 = f"{player_name}: You’re hotter than the bottom of my laptop"
        li_dialogue_1 = f"{li_name}: Where do you work out?"
        relation_points += 5
        display_dialogue_1_to_2()
        text1_coversation2_part2()

    else:
        player_dialogue_2 = f"{player_name}: My appearance is the most important thing to me"
        li_dialogue_2 = f"{li_name}: Where do you work out?"
        relation_points += 2
        display_dialogue_1_to_2()
        text1_coversation2_part2()

def text1_coversation3_part1():

    global player_dialogue_1
    global player_dialogue_2
    global li_dialogue_1
    global li_dialogue_2
    global option_display_1
    global option_display_2
    global relation_points

    print("")
    print("")
    option_display_1 = "1.	I’m not a photographer, but I can definitely picture me and you together"
    option_display_2 = "2.	You remind me of a parking ticket cos you’ve got fine written all over you "
    display_options_1_to_2()
    print("")
    print("")
    input_choice_1_to_2()
    if choice == "1":
        player_dialogue_1 = f"{player_name}: I’m not a photographer, but I can definitely picture me and you together"
        li_dialogue_1 = f"{li_name}: You’re such a charmer! Do you think we’re an ideal couple"
        relation_points += 5
        display_dialogue_1_to_2()
        text1_coversation3_part2()

    else:
        player_dialogue_2 = f"{player_name}: You remind me of a parking ticket cos you’ve got fine written all over you "
        li_dialogue_2 = f"{li_name}: You’re such a charmer! Do you think we’re an ideal couple"
        relation_points += 2
        display_dialogue_1_to_2()
        text1_coversation3_part2()

def text1_coversation4_part1():

    global player_dialogue_1
    global player_dialogue_2
    global li_dialogue_1
    global li_dialogue_2
    global option_display_1
    global option_display_2
    global relation_points

    print("")
    print("")
    option_display_1 = "1.	I have one of my ex-partner on my arm"
    option_display_2 = "2.	Yes, but if you want to know where, you’ll have to agree to a date"
    display_options_1_to_2()
    print("")
    print("")
    input_choice_1_to_2()
    if choice == "1":
        player_dialogue_1 = f"{player_name}: I have one of my ex-partner on my arm"
        li_dialogue_1 = f"{li_name}: At work I have to keep my tattoo covered up"
        relation_points += 2
        display_dialogue_1_to_2()
        text1_coversation4_part2()

    else:
        player_dialogue_2 = f"{player_name}: Yes, but if you want to know where, you’ll have to agree to a date"
        li_dialogue_2 = f"{li_name}: At work I have to keep my tattoo covered up"
        relation_points += 5
        display_dialogue_1_to_2()
        text1_coversation4_part2()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Texting Event 1 Part 2s

def text1_coversation1_part2():

    global player_dialogue_1
    global player_dialogue_2
    global li_dialogue_1
    global li_dialogue_2
    global option_display_1
    global option_display_2
    global relation_points

    print("")
    print("")
    option_display_1 = "1.	Skydiving – I love adventure!"
    option_display_2 = "2.	I’m the local tiddly winks champion"
    display_options_1_to_2()
    print("")
    print("")
    input_choice_1_to_2()
    if choice == "1":
        player_dialogue_1 = f"{player_name}: Skydiving – I love adventure!"
        li_dialogue_1 = f"{li_name}: I love being wined and dined. Where do you like to eat?"
        relation_points += 5
        display_dialogue_1_to_2()
        text1_coversation1_part3()
    else:
        player_dialogue_2 = f"{player_name}: I’m the local tiddly winks champion"
        li_dialogue_2 = f"{li_name}: I love being wined and dined. Where do you like to eat?"
        relation_points += 2
        display_dialogue_1_to_2()
        text1_coversation1_part3()
    
def text1_coversation2_part2():

    global player_dialogue_1
    global player_dialogue_2
    global li_dialogue_1
    global li_dialogue_2
    global option_display_1
    global option_display_2
    global relation_points

    print("")
    print("")
    option_display_1 = "1.	My job is very physical and keeps me fit"
    option_display_2 = "2.	I spend every spare moment I have at the gym"
    display_options_1_to_2()
    print("")
    print("")
    input_choice_1_to_2()
    if choice == "1":
        player_dialogue_1 = f"{player_name}: My job is very physical and keeps me fit"
        li_dialogue_1 = f"{li_name}: Do you speak any languages?"
        relation_points += 5
        display_dialogue_1_to_2()
        text1_coversation2_part3()

    else:
        player_dialogue_2 = f"{player_name}: I spend every spare moment I have at the gym"
        li_dialogue_2 = f"{li_name}: Do you speak any languages?"
        relation_points += 2
        display_dialogue_1_to_2()
        text1_coversation2_part3()

def text1_coversation3_part2():

    global player_dialogue_1
    global player_dialogue_2
    global li_dialogue_1
    global li_dialogue_2
    global option_display_1
    global option_display_2
    global relation_points

    print("")
    print("")
    option_display_1 = "1.	Yes, we’re as good as Boris and Carrie any day"
    option_display_2 = "2.	Hey, you’re pretty and I’m cute. Together we’d be Pretty Cute"
    display_options_1_to_2()
    print("")
    print("")
    input_choice_1_to_2()
    if choice == "1":
        player_dialogue_1 = f"{player_name}: Yes, we’re as good as Boris and Carrie any day"
        li_dialogue_1 = f"{li_name}: What would your friends think of me?"
        relation_points += 5
        display_dialogue_1_to_2()
        text1_coversation3_part3()
    else:
        player_dialogue_2 = f"{player_name}: Hey, you’re pretty and I’m cute. Together we’d be Pretty Cute"
        li_dialogue_2 = f"{li_name}: What would your friends think of me?"
        relation_points += 2
        display_dialogue_1_to_2()
        text1_coversation3_part3()

def text1_coversation4_part2():

    global player_dialogue_1
    global player_dialogue_2
    global li_dialogue_1
    global li_dialogue_2
    global option_display_1
    global option_display_2
    global relation_points

    print("")
    print("")
    option_display_1 = "1.	Aside from being sexy, what do you do for a living?"
    option_display_2 = "2.	Nobody tells me what to do!"
    display_options_1_to_2()
    print("")
    print("")
    input_choice_1_to_2()
    if choice == "1":
        player_dialogue_1 = f"{player_name}: Aside from being sexy, what do you do for a living?"
        li_dialogue_1 = f"{li_name}: I work in an office and it’s important to look smart?"
        relation_points += 5
        display_dialogue_1_to_2()
        text1_coversation4_part3()
    else:
        player_dialogue_2 = f"{player_name}: Nobody tells me what to do!"
        li_dialogue_2 = f"{li_name}: I work in an office and it’s important to look smart?"
        relation_points += 2
        display_dialogue_1_to_2()
        text1_coversation4_part3()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Texting Event 1 part 3s

def text1_coversation1_part3():

    global player_dialogue_1
    global player_dialogue_2
    global li_dialogue_1
    global li_dialogue_2
    global option_display_1
    global option_display_2
    global relation_points

    print("")
    print("")
    option_display_1 = "1.	Anywhere you enjoy eating"
    option_display_2 = "2.	It’s cheaper to eat at home"
    display_options_1_to_2()
    print("")
    print("")
    input_choice_1_to_2()
    if choice == "1":
        player_dialogue_1 = f"{player_name}: Anywhere you enjoy eating"
        li_dialogue_1 = f"{li_name}: What films do you like?"
        relation_points += 5
        display_dialogue_1_to_2()
        rp_notification()
        text1_coversation5_part1()
    else:
        player_dialogue_2 = f"{player_name}: It’s cheaper to eat at home"
        li_dialogue_2 = f"{li_name}: What films do you like?"
        relation_points += 2
        display_dialogue_1_to_2()
        rp_notification()
        text1_coversation5_part1()
    
def text1_coversation2_part3():

    global player_dialogue_1
    global player_dialogue_2
    global li_dialogue_1
    global li_dialogue_2
    global option_display_1
    global option_display_2
    global relation_points

    print("")
    print("")
    option_display_1 = "1.	I’ve never been outside my town, so don’t see the need"
    option_display_2 = "2.	No, but I want to learn French because Eiffel for you"
    display_options_1_to_2()
    print("")
    print("")
    input_choice_1_to_2()
    if choice == "1":
        player_dialogue_1 = f"{player_name}: I’ve never been outside my town, so don’t see the need"
        li_dialogue_1 = f"{li_name}: What films do you like?"
        relation_points += 2
        display_dialogue_1_to_2()
        rp_notification()
        text1_coversation5_part1()

    else:
        player_dialogue_2 = f"{player_name}: No, but I want to learn French because Eiffel for you"
        li_dialogue_2 = f"{li_name}: What films do you like?"
        relation_points += 5
        display_dialogue_1_to_2()
        rp_notification()
        text1_coversation5_part1()

def text1_coversation3_part3():

    global player_dialogue_1
    global player_dialogue_2
    global li_dialogue_1
    global li_dialogue_2
    global option_display_1
    global option_display_2
    global relation_points

    print("")
    print("")
    option_display_1 = "1.	They’ll be worried I’ll want to spend all my time with you"
    option_display_2 = "2.	We always rate our dates and I’m sure you’ll do well"
    display_options_1_to_2()
    print("")
    print("")
    input_choice_1_to_2()
    if choice == "1":
        player_dialogue_1 = f"{player_name}: They’ll be worried I’ll want to spend all my time with you"
        li_dialogue_1 = f"{li_name}: What films do you like?"
        relation_points += 5
        display_dialogue_1_to_2()
        rp_notification()
        text1_coversation5_part1()
    else:
        player_dialogue_2 = f"{player_name}: We always rate our dates and I’m sure you’ll do well"
        li_dialogue_2 = f"{li_name}: What films do you like?"
        relation_points += 2
        display_dialogue_1_to_2()
        rp_notification()
        text1_coversation5_part1()

def text1_coversation4_part3():

    global player_dialogue_1
    global player_dialogue_2
    global li_dialogue_1
    global li_dialogue_2
    global option_display_1
    global option_display_2
    global relation_points

    print("")
    print("")
    option_display_1 = "1.	You’ve got the perfect body and will look good in anything! "
    option_display_2 = "2.	That sounds a boring job – I’m a nuclear physicist"
    display_options_1_to_2()
    print("")
    print("")
    input_choice_1_to_2()
    if choice == "1":
        player_dialogue_1 = f"{player_name}: You’ve got the perfect body and will look good in anything! "
        li_dialogue_1 = f"{li_name}: What films do you like?"
        relation_points += 5
        display_dialogue_1_to_2()
        rp_notification()
        text1_coversation5_part1()
    else:
        player_dialogue_2 = f"{player_name}: That sounds a boring job – I’m a nuclear physicist"
        li_dialogue_2 = f"{li_name}: What films do you like?"
        relation_points += 2
        display_dialogue_1_to_2()
        rp_notification()
        text1_coversation5_part1()


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Texting Event 2

def text1_coversation5_part1():

    global player_dialogue_1
    global player_dialogue_2
    global li_dialogue_1
    global li_dialogue_2
    global option_display_1
    global option_display_2
    global relation_points

    print("")
    print("")
    option_display_1 = "1.	Anything I can watch with you!"
    option_display_2 = "2.	I only watch horror films"
    display_options_1_to_2()
    print("")
    print("")
    input_choice_1_to_2()
    if choice == "1":
        player_dialogue_1 = f"{player_name}: Anything I can watch with you!"
        li_dialogue_1 = f"{li_name}: Do you eat snacks at the movies?"
        relation_points += 5
        display_dialogue_1_to_2()
        text1_coversation5_part2()
    else:
        player_dialogue_2 = f"{player_name}: I only watch horror films"
        li_dialogue_2 = f"{li_name}: Do you eat snacks at the movies?"
        relation_points += 2
        display_dialogue_1_to_2()
        text1_coversation5_part2()
    
def text1_coversation5_part2():

    global player_dialogue_1
    global player_dialogue_2
    global li_dialogue_1
    global li_dialogue_2
    global option_display_1
    global option_display_2
    global relation_points

    print("")
    print("")
    option_display_1 = "1.	I'd take you to the movies, but they don't let you bring in your own snacks!"
    option_display_2 = "2.	Yes I take in a lollipop and make it last the entire film."
    display_options_1_to_2()
    print("")
    print("")
    input_choice_1_to_2()
    if choice == "1":
        player_dialogue_1 = f"{player_name}: I'd take you to the movies, but they don't let you bring in your own snacks!"
        li_dialogue_1 = f"{li_name}: Who’s your favourite film star?"
        relation_points += 5
        display_dialogue_1_to_2()
        text1_coversation5_part3()

    else:
        player_dialogue_2 = f"{player_name}: Yes I take in a lollipop and make it last the entire film."
        li_dialogue_2 = f"{li_name}: Who’s your favourite film star?"
        relation_points += 2
        display_dialogue_1_to_2()
        text1_coversation5_part3()

def text1_coversation5_part3():

    global player_dialogue_1
    global player_dialogue_2
    global li_dialogue_1
    global li_dialogue_2
    global option_display_1
    global option_display_2
    global relation_points

    print("")
    print("")
    option_display_1 = "1.	Mr Bean"
    option_display_2 = "2.	I’d love to see you on the big screen"
    display_options_1_to_2()
    print("")
    print("")
    input_choice_1_to_2()
    if choice == "1":
        player_dialogue_1 = f"{player_name}: Mr Bean"
        li_dialogue_1 = f"{li_name}: I’m very sporty. Do you play any sports?"
        relation_points += 2
        display_dialogue_1_to_2()
        rp_notification()
        text1_coversation6_part1()
    else:
        player_dialogue_2 = f"{player_name}: I’d love to see you on the big screen"
        li_dialogue_2 = f"{li_name}: I’m very sporty. Do you play any sports?"
        relation_points += 5
        display_dialogue_1_to_2()
        rp_notification()
        text1_coversation6_part1()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Texting Event 3

def text1_coversation6_part1():

    global player_dialogue_1
    global player_dialogue_2
    global li_dialogue_1
    global li_dialogue_2
    global option_display_1
    global option_display_2
    global relation_points

    print("")
    print("")
    option_display_1 = "1.	I’d love to play some one to one sports with you!"
    option_display_2 = "2.	I prefer Solitaire."
    display_options_1_to_2()
    print("")
    print("")
    input_choice_1_to_2()
    if choice == "1":
        player_dialogue_1 = f"{player_name}: I’d love to play some one to one sports with you!"
        li_dialogue_1 = f"{li_name}: I like to run marathons. Could I persuade you to join me?"
        relation_points += 5
        display_dialogue_1_to_2()
        text1_coversation6_part2()
    else:
        player_dialogue_2 = f"{player_name}: I prefer Solitaire."
        li_dialogue_2 = f"{li_name}: I like to run marathons. Could I persuade you to join me?"
        relation_points += 2
        display_dialogue_1_to_2()
        text1_coversation6_part2()
    
def text1_coversation6_part2():

    global player_dialogue_1
    global player_dialogue_2
    global li_dialogue_1
    global li_dialogue_2
    global option_display_1
    global option_display_2
    global relation_points

    print("")
    print("")
    option_display_1 = "1.	I’d follow you anywhere!"
    option_display_2 = "2.	Too tiring for me."
    display_options_1_to_2()
    print("")
    print("")
    input_choice_1_to_2()
    if choice == "1":
        player_dialogue_1 = f"{player_name}: I’d follow you anywhere!"
        li_dialogue_1 = f"{li_name}: How would you suggest I relax after a marathon"
        relation_points += 5
        display_dialogue_1_to_2()
        text1_coversation6_part3()

    else:
        player_dialogue_2 = f"{player_name}: Too tiring for me."
        li_dialogue_2 = f"{li_name}: How would you suggest I relax after a marathon"
        relation_points += 2
        display_dialogue_1_to_2()
        text1_coversation6_part3()

def text1_coversation6_part3():

    global player_dialogue_1
    global player_dialogue_2
    global li_dialogue_1
    global li_dialogue_2
    global option_display_1
    global option_display_2
    global relation_points

    print("")
    print("")
    option_display_1 = "1.	Watch a boxset of  Friends"
    option_display_2 = "2.	I’m happy to offer you a massage "
    display_options_1_to_2()
    print("")
    print("")
    input_choice_1_to_2()
    if choice == "1":
        player_dialogue_1 = f"{player_name}: Watch a boxset of  Friends"
        li_dialogue_1 = f"{li_name}: What would you do to impress me?"
        relation_points += 2
        display_dialogue_1_to_2()
        rp_notification()
        date1()
    else:
        player_dialogue_2 = f"{player_name}: I’m happy to offer you a massage"
        li_dialogue_2 = f"{li_name}: What would you do to impress me?"
        relation_points += 5
        display_dialogue_1_to_2()
        rp_notification()
        date1()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Date Event 1

def date1():
    
    global player_dialogue_1
    global player_dialogue_2
    global player_dialogue_3
    global li_dialogue_1
    global li_dialogue_2
    global li_dialogue_3
    global option_display_1
    global option_display_2
    global option_display_3
    global relation_points

    print("")
    print("")
    event_start = f"Congratulations, you can now go on a date. Your date has chosen to meet you for dinner at a very posh Indian restaurant in town. You are keen to impress and have put in a lot of time and effort getting ready for the occasion. The food and drink are amazing, and you are just thinking to yourself how well the evening has gone when disaster strikes halfway through your second course: {li_name} knocks over their expensive drink and proceeds to slurp it up from the table."

    option_display_1 = "1.	You think it’s hilarious. Your date obviously shares your sense of humour!"  
    option_display_2 = "2.	You feign a migraine and leave the restaurant and your date’s life as quickly as possible."
    option_display_3 = "3.	You feel really embarrassed but you’re always happy to give someone a second chance"
    for char in event_start:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("")
    print("")
    display_options_1_to_3()
    print("")
    print("")
    input_choice_1_to_3()
    if choice == "1":
        player_dialogue_1 = f"{player_name}: You think it’s hilarious. Your date obviously shares your sense of humour!"
        display_dialogue_1_to_3()
        text1_coversation7_part1()

    elif choice == "2":
        player_dialogue_2 = f"{player_name}: You feign a migraine and leave the restaurant and your date’s life as quickly as possible."
        li_dialogue_1 = ""
        display_dialogue_1_to_3()
        bad_ending()

    else:
        player_dialogue_3 = f"{player_name}: 3.	You feel really embarrassed but you’re always happy to give someone a second chance."
        display_dialogue_1_to_3()
        text1_coversation7_part1()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Texting Event 4

def text1_coversation7_part1():

    global player_dialogue_1
    global player_dialogue_2
    global li_dialogue_1
    global li_dialogue_2
    global option_display_1
    global option_display_2
    global relation_points

    message = f"{li_name}: What would you do to impress me?"
    for char in message:
            sleep(0.05)
            sys.stdout.write(char)
            sys.stdout.flush()
    print("")
    print("")
    option_display_1 = "1.	I’d cook you my favourite meal of liver and onions"
    option_display_2 = "2.	I’d write a love song just for you."
    display_options_1_to_2()
    print("")
    print("")
    input_choice_1_to_2()
    if choice == "1":
        player_dialogue_1 = f"{player_name}: I’d cook you my favourite meal of liver and onions"
        li_dialogue_1 = f"{li_name}: I can be very high maintenance - are you up for the challenge?"
        relation_points += 2
        display_dialogue_1_to_2()
        text1_coversation7_part2()
    else:
        player_dialogue_2 = f"{player_name}: 2.	I’d write a love song just for you."
        li_dialogue_2 = f"{li_name}: I can be very high maintenance - are you up for the challenge?"
        relation_points += 5
        display_dialogue_1_to_2()
        text1_coversation7_part2()
    
def text1_coversation7_part2():

    global player_dialogue_1
    global player_dialogue_2
    global li_dialogue_1
    global li_dialogue_2
    global option_display_1
    global option_display_2
    global relation_points

    print("")
    print("")
    option_display_1 = "1.	As long as you fit in with me and my friends, we’re good."
    option_display_2 = "2.	I thrive on a challenge!"
    display_options_1_to_2()
    print("")
    print("")
    input_choice_1_to_2()
    if choice == "1":
        player_dialogue_1 = f"{player_name}: As long as you fit in with me and my friends, we’re good."
        li_dialogue_1 = f"{li_name}: I always like my dates to have impeccable manners?"
        relation_points += 2
        display_dialogue_1_to_2()
        text1_coversation7_part3()

    else:
        player_dialogue_2 = f"{player_name}: I thrive on a challenge!"
        li_dialogue_2 = f"{li_name}: I always like my dates to have impeccable manners?"
        relation_points += 5
        display_dialogue_1_to_2()
        text1_coversation7_part3()

def text1_coversation7_part3():

    global player_dialogue_1
    global player_dialogue_2
    global li_dialogue_1
    global li_dialogue_2
    global option_display_1
    global option_display_2
    global relation_points

    print("")
    print("")
    option_display_1 = "1.	Here, let me open the door for you."
    option_display_2 = "2.	You don’t mind if I burp do you – better out than in!"
    display_options_1_to_2()
    print("")
    print("")
    input_choice_1_to_2()
    if choice == "1":
        player_dialogue_1 = f"{player_name}: Here, let me open the door for you."
        li_dialogue_1 = f"{li_name}: I love eating pasta. What’s your favourite food?"
        relation_points += 5
        display_dialogue_1_to_2()
        rp_notification()
        text1_coversation8_part1()
    else:
        player_dialogue_2 = f"{player_name}: You don’t mind if I burp do you – better out than in!"
        li_dialogue_2 = f"{li_name}: I love eating pasta. What’s your favourite food?"
        relation_points += 2
        display_dialogue_1_to_2()
        rp_notification()
        text1_coversation8_part1()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Texting Event 5

def text1_coversation8_part1():

    global player_dialogue_1
    global player_dialogue_2
    global li_dialogue_1
    global li_dialogue_2
    global option_display_1
    global option_display_2
    global relation_points

    print("")
    print("")
    option_display_1 = "1.	Dates. How about one?"
    option_display_2 = "2.	Bubble and squeak."
    display_options_1_to_2()
    print("")
    print("")
    input_choice_1_to_2()
    if choice == "1":
        player_dialogue_1 = f"{player_name}: Dates. How about one?"
        li_dialogue_1 = f"{li_name}: I’m not very good in the kitchen. How are your culinary skills?"
        relation_points += 5
        display_dialogue_1_to_2()
        text1_coversation8_part2()
    else:
        player_dialogue_2 = f"{player_name}: Bubble and squeak."
        li_dialogue_2 = f"{li_name}: I’m not very good in the kitchen. How are your culinary skills?"
        relation_points += 2
        display_dialogue_1_to_2()
        text1_coversation8_part2()
    
def text1_coversation8_part2():

    global player_dialogue_1
    global player_dialogue_2
    global li_dialogue_1
    global li_dialogue_2
    global option_display_1
    global option_display_2
    global relation_points

    print("")
    print("")
    option_display_1 = "1.	I’m great at heating up a supermarket ready meal."
    option_display_2 = "2.	Let music be the food of love and I will serenade you."
    display_options_1_to_2()
    print("")
    print("")
    input_choice_1_to_2()
    if choice == "1":
        player_dialogue_1 = f"{player_name}: I’m great at heating up a supermarket ready meal."
        li_dialogue_1 = f"{li_name}: Do you follow any particular diet"
        relation_points += 2
        display_dialogue_1_to_2()
        text1_coversation8_part3()

    else:
        player_dialogue_2 = f"{player_name}: Let music be the food of love and I will serenade you."
        li_dialogue_2 = f"{li_name}: Do you follow any particular diet"
        relation_points += 5
        display_dialogue_1_to_2()
        text1_coversation8_part3()

def text1_coversation8_part3():

    global player_dialogue_1
    global player_dialogue_2
    global li_dialogue_1
    global li_dialogue_2
    global option_display_1
    global option_display_2
    global relation_points

    print("")
    print("")
    option_display_1 = "1.	Yes, the seafood diet – I eat all I see!"
    option_display_2 = "How can I think about food when I now have you to focus on?"
    display_options_1_to_2()
    print("")
    print("")
    input_choice_1_to_2()
    if choice == "1":
        player_dialogue_1 = f"{player_name}: Yes, the seafood diet – I eat all I see!"
        li_dialogue_1 = f"{li_name}: Do you have any nicknames?"
        relation_points += 2
        display_dialogue_1_to_2()
        rp_notification()
        text1_coversation9_part1()
    else:
        player_dialogue_2 = f"{player_name}: How can I think about food when I now have you to focus on?"
        li_dialogue_2 = f"{li_name}: Do you have any nicknames?"
        relation_points += 5
        display_dialogue_1_to_2()
        rp_notification()
        text1_coversation9_part1()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Texting Event 6

def text1_coversation9_part1():

    global player_dialogue_1
    global player_dialogue_2
    global li_dialogue_1
    global li_dialogue_2
    global option_display_1
    global option_display_2
    global relation_points

    print("")
    print("")
    option_display_1 = "1.	No, but yours must be Google because you have everything I’ve been searching for."
    option_display_2 = "2.	Farty-pants. Go figure!"
    display_options_1_to_2()
    print("")
    print("")
    input_choice_1_to_2()
    if choice == "1":
        player_dialogue_1 = f"{player_name}: No, but yours must be Google because you have everything I’ve been searching for."
        li_dialogue_1 = f"{li_name}: : I love Disney films, especially Aladdin."
        relation_points += 5
        display_dialogue_1_to_2()
        text1_coversation9_part2()
    else:
        player_dialogue_2 = f"{player_name}: 2.	Farty-pants. Go figure!"
        li_dialogue_2 = f"{li_name}: : I love Disney films, especially Aladdin."
        relation_points += 2
        display_dialogue_1_to_2()
        text1_coversation9_part2()
    
def text1_coversation9_part2():

    global player_dialogue_1
    global player_dialogue_2
    global li_dialogue_1
    global li_dialogue_2
    global option_display_1
    global option_display_2
    global relation_points

    print("")
    print("")
    option_display_1 = "1.	Disney’s for kids!"
    option_display_2 = "2.	I may not be a genie, but I can make your dreams come true."
    display_options_1_to_2()
    print("")
    print("")
    input_choice_1_to_2()
    if choice == "1":
        player_dialogue_1 = f"{player_name}: Disney’s for kids!"
        li_dialogue_1 = f"{li_name}: Disney films are just so magical!"
        relation_points += 2
        display_dialogue_1_to_2()
        text1_coversation9_part3()

    else:
        player_dialogue_2 = f"{player_name}: I may not be a genie, but I can make your dreams come true."
        li_dialogue_2 = f"{li_name}: Disney films are just so magical!"
        relation_points += 5
        display_dialogue_1_to_2()
        text1_coversation9_part3()

def text1_coversation9_part3():

    global player_dialogue_1
    global player_dialogue_2
    global li_dialogue_1
    global li_dialogue_2
    global option_display_1
    global option_display_2
    global relation_points

    print("")
    print("")
    option_display_1 = "1.	I must be a magician - whenever I look at you, everyone else disappears!"
    option_display_2 = "2.	It’s not real!"
    display_options_1_to_2()
    print("")
    print("")
    input_choice_1_to_2()
    if choice == "1":
        player_dialogue_1 = f"{player_name}: I must be a magician - whenever I look at you, everyone else disappears!"
        li_dialogue_1 = ""
        relation_points += 5
        display_dialogue_1_to_2()
        rp_notification()
        date2()
    else:
        player_dialogue_2 = f"{player_name}: It’s not real!"
        li_dialogue_2 = ""
        relation_points += 2
        display_dialogue_1_to_2()
        rp_notification()
        date2()


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Date Event 2

def date2():
    
    global player_dialogue_1
    global player_dialogue_2
    global player_dialogue_3
    global li_dialogue_1
    global li_dialogue_2
    global li_dialogue_3
    global option_display_1
    global option_display_2
    global option_display_3
    global relation_points

    print("")
    print("")
    event_start = f"Congratulations, you can now go on another date with {li_name}! They have agreed to visit Chester Zoo with you. You are looking forward to spending the day getting up close and personal with the animals … and each other. Then disaster strikes: your date has turned up with the mother from hell who won’t stop talking, who insists that you pay for everything, and who permanently positions herself between you and your date."
    option_display_1 = "1.	You suggest visiting the bat house, and then make your escape under the cover of darkness."  
    option_display_2 = "2.	You plan how you can feed the mother from hell to the lions"
    option_display_3 = "3.	You take the opportunity to really get to know your future mother-in-law."
    for char in event_start:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("")
    print("")
    display_options_1_to_3()
    print("")
    print("")
    input_choice_1_to_3()
    if choice == "1":
        player_dialogue_1 = f"{player_name}: You suggest visiting the bat house, and then make your escape under the cover of darkness."
        display_dialogue_1_to_3()
        text1_coversation10_part1()

    elif choice == "2":
        player_dialogue_2 = f"{player_name}: You plan how you can feed the mother from hell to the lions"
        li_dialogue_1 = ""
        display_dialogue_1_to_3()
        bad_ending()

    else:
        player_dialogue_3 = f"{player_name}: You take the opportunity to really get to know your future mother-in-law."
        display_dialogue_1_to_3()
        text1_coversation10_part1()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Texting Event 7

def text1_coversation10_part1():

    global player_dialogue_1
    global player_dialogue_2
    global li_dialogue_1
    global li_dialogue_2
    global option_display_1
    global option_display_2
    global relation_points

    message = f"{li_name}: Do you do much reading?"
    for char in message:
            sleep(0.05)
            sys.stdout.write(char)
            sys.stdout.flush()
    print("")
    print("")
    option_display_1 = "1.  Yes, my favourite book is War and Peace"
    option_display_2 = "2.  Yes, and if you were a library book I’d definitely check you out"
    display_options_1_to_2()
    print("")
    print("")
    input_choice_1_to_2()
    if choice == "1":
        player_dialogue_1 = f"{player_name}: Yes, my favourite book is War and Peace"
        li_dialogue_1 = f"{li_name}: What music do you listen to?"
        relation_points += 2
        display_dialogue_1_to_2()
        text1_coversation10_part2()
    else:
        player_dialogue_2 = f"{player_name}: Yes, and if you were a library book I’d definitely check you out"
        li_dialogue_2 = f"{li_name}: What music do you listen to?"
        relation_points += 5
        display_dialogue_1_to_2()
        text1_coversation10_part2()
    
def text1_coversation10_part2():

    global player_dialogue_1
    global player_dialogue_2
    global li_dialogue_1
    global li_dialogue_2
    global option_display_1
    global option_display_2
    global relation_points

    print("")
    print("")
    option_display_1 = "1.	Drake is the best artist and he would call you and me “God’s Plan”"
    option_display_2 = "2.	I like classical - good to hum to."
    display_options_1_to_2()
    print("")
    print("")
    input_choice_1_to_2()
    if choice == "1":
        player_dialogue_1 = f"{player_name}: Drake is the best artist and he would call you and me “God’s Plan”"
        li_dialogue_1 = f"{li_name}: What do you do In your spare time?"
        relation_points += 5
        display_dialogue_1_to_2()
        text1_coversation10_part3()

    else:
        player_dialogue_2 = f"{player_name}: I like classical - good to hum to."
        li_dialogue_2 = f"{li_name}: What do you do In your spare time?"
        relation_points += 2
        display_dialogue_1_to_2()
        text1_coversation10_part3()

def text1_coversation10_part3():

    global player_dialogue_1
    global player_dialogue_2
    global li_dialogue_1
    global li_dialogue_2
    global option_display_1
    global option_display_2
    global relation_points

    print("")
    print("")
    option_display_1 = "1.	I’m interested in fine art and that’s why I’m so attracted to you."
    option_display_2 = "2.	Facebook is the best!"
    display_options_1_to_2()
    print("")
    print("")
    input_choice_1_to_2()
    if choice == "1":
        player_dialogue_1 = f"{player_name}: I’m interested in fine art and that’s why I’m so attracted to you."
        li_dialogue_1 = f"{li_name}: Are you an organised person?"
        relation_points += 5
        display_dialogue_1_to_2()
        rp_notification()
        text1_coversation11_part1()
    else:
        player_dialogue_2 = f"{player_name}: Facebook is the best!"
        li_dialogue_2 = f"{li_name}: Are you an organised person?"
        relation_points += 2
        display_dialogue_1_to_2()
        rp_notification()
        text1_coversation11_part1()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Texting Event 8

def text1_coversation11_part1():

    global player_dialogue_1
    global player_dialogue_2
    global li_dialogue_1
    global li_dialogue_2
    global option_display_1
    global option_display_2
    global relation_points

    print("")
    print("")
    option_display_1 = "1.	I guess"
    option_display_2 = "2.	I'm happy for you to take charge and organise my life!"
    display_options_1_to_2()
    print("")
    print("")
    input_choice_1_to_2()
    if choice == "1":
        player_dialogue_1 = f"{player_name}: I guess"
        li_dialogue_1 = f"{li_name}: What’s your favourite drink?"
        relation_points += 2
        display_dialogue_1_to_2()
        text1_coversation11_part2()
    else:
        player_dialogue_2 = f"{player_name}: I'm happy for you to take charge and organise my life!"
        li_dialogue_2 = f"{li_name}: What’s your favourite drink?"
        relation_points += 5
        display_dialogue_1_to_2()
        text1_coversation11_part2()
    
def text1_coversation11_part2():

    global player_dialogue_1
    global player_dialogue_2
    global li_dialogue_1
    global li_dialogue_2
    global option_display_1
    global option_display_2
    global relation_points

    print("")
    print("")
    option_display_1 = "1.	Anything that’s cheap and cheerful."
    option_display_2 = "2.	Earl Grey cos it reminds me of you – a ‘hot-tea’."
    display_options_1_to_2()
    print("")
    print("")
    input_choice_1_to_2()
    if choice == "1":
        player_dialogue_1 = f"{player_name}: Anything that’s cheap and cheerful."
        li_dialogue_1 = f"{li_name}: Do you enjoy fancy dress parties?"
        relation_points += 2
        display_dialogue_1_to_2()
        text1_coversation11_part3()

    else:
        player_dialogue_2 = f"{player_name}: Earl Grey cos it reminds me of you – a ‘hot-tea’."
        li_dialogue_2 = f"{li_name}: Do you enjoy fancy dress parties?"
        relation_points += 2
        display_dialogue_1_to_2()
        text1_coversation11_part3()

def text1_coversation11_part3():

    global player_dialogue_1
    global player_dialogue_2
    global li_dialogue_1
    global li_dialogue_2
    global option_display_1
    global option_display_2
    global relation_points

    print("")
    print("")
    option_display_1 = "1.	Yes, if it was Halloween and you were a jack-o-lantern, I’d definitely light your candle"
    option_display_2 = "2.	They’re cringy, so no!"
    display_options_1_to_2()
    print("")
    print("")
    input_choice_1_to_2()
    if choice == "1":
        player_dialogue_1 = f"{player_name}: Yes, if it was Halloween and you were a jack-o-lantern, I’d definitely light your candle"
        li_dialogue_1 = f"{li_name}: Do you have any pets?"
        relation_points += 5
        display_dialogue_1_to_2()
        rp_notification()
        text1_coversation12_part1()
    else:
        player_dialogue_2 = f"{player_name}: They’re cringy, so no!"
        li_dialogue_2 = f"{li_name}: Do you have any pets?"
        relation_points += 5
        display_dialogue_1_to_2()
        rp_notification()
        text1_coversation12_part1()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Texting Event 9

def text1_coversation12_part1():

    global player_dialogue_1
    global player_dialogue_2
    global li_dialogue_1
    global li_dialogue_2
    global option_display_1
    global option_display_2
    global relation_points

    print("")
    print("")
    option_display_1 = "1.	I have two donkeys who are jealous because you’ve got one fine ass"
    option_display_2 = "2.	My guinea pig died last year, so I keep spiders now instead"
    display_options_1_to_2()
    print("")
    print("")
    input_choice_1_to_2()
    if choice == "1":
        player_dialogue_1 = f"{player_name}: I have two donkeys who are jealous because you’ve got one fine ass"
        li_dialogue_1 = f"{li_name}: What’s your biggest hope for the future?"
        relation_points += 5
        display_dialogue_1_to_2()
        text1_coversation12_part2()
    else:
        player_dialogue_2 = f"{player_name}: My guinea pig died last year, so I keep spiders now instead"
        li_dialogue_2 = f"{li_name}: What’s your biggest hope for the future?"
        relation_points += 2
        display_dialogue_1_to_2()
        text1_coversation12_part2()
    
def text1_coversation12_part2():

    global player_dialogue_1
    global player_dialogue_2
    global li_dialogue_1
    global li_dialogue_2
    global option_display_1
    global option_display_2
    global relation_points

    print("")
    print("")
    option_display_1 = "1.	To be mega rich and order everyone around."
    option_display_2 = "2.	To have your last name."
    display_options_1_to_2()
    print("")
    print("")
    input_choice_1_to_2()
    if choice == "1":
        player_dialogue_1 = f"{player_name}: To be mega rich and order everyone around."
        li_dialogue_1 = f"{li_name}: What do you do for a living?"
        relation_points += 2
        display_dialogue_1_to_2()
        text1_coversation12_part3()

    else:
        player_dialogue_2 = f"{player_name}: To have your last name."
        li_dialogue_2 = f"{li_name}: What do you do for a living?"
        relation_points += 5
        display_dialogue_1_to_2()
        text1_coversation12_part3()

def text1_coversation12_part3():

    global player_dialogue_1
    global player_dialogue_2
    global li_dialogue_1
    global li_dialogue_2
    global option_display_1
    global option_display_2
    global relation_points

    print("")
    print("")
    option_display_1 = "1.	I’m a lawyer. Obviously my work has to be my main priority"
    option_display_2 = "2.	I own a large company, so I can help you out if you ever need a job"
    display_options_1_to_2()
    print("")
    print("")
    input_choice_1_to_2()
    if choice == "1":
        player_dialogue_1 = f"{player_name}: I’m a lawyer. Obviously my work has to be my main priority"
        li_dialogue_1 = ""
        relation_points += 2
        display_dialogue_1_to_2()
        rp_notification()
        date3()
    else:
        player_dialogue_2 = f"{player_name}: I own a large company, so I can help you out if you ever need a job"
        li_dialogue_2 = ""
        relation_points += 5
        display_dialogue_1_to_2()
        rp_notification()
        date3()


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Date Event 3

def date3():
    
    global player_dialogue_1
    global player_dialogue_2
    global player_dialogue_3
    global li_dialogue_1
    global li_dialogue_2
    global li_dialogue_3
    global option_display_1
    global option_display_2
    global option_display_3
    global relation_points

    print("")
    print("")
    event_start = f"Congratulations, you can now go on a date with {li_name}! They have persuaded you to go on a hike with them. Although you have never been hiking before, your date assures you that they are a very experienced hiker and that they know the perfect trail to explore with you. They are even able to lend you a pair of walking boots. So far, so good! When you reach the start of the trail you realise it is definitely off the beaten track, but all is well as your date has an ordnance survey map and you are looking forward to spending time alone with them. The further you walk, the more interested you are in your date. Then disaster strikes: after walking for 2 hours, your date casually mentions that they know the perfect method for killing someone and disposing of the body without anybody ever finding out, and that they have a history of their dates not ending well. All of a sudden you wonder whether it’s not really survival provisions that they are carrying in their rather large rucksack, or something more sinister."
    option_display_1 = "1.	You wrestle your date to the ground, grab their rucksack and map and run for cover"  
    option_display_2 = "2.	You plan how you’re going to kill your date before they kill you."
    option_display_3 = "3.	You appreciate their sense of humour."
    for char in event_start:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("")
    print("")
    display_options_1_to_3()
    print("")
    print("")
    input_choice_1_to_3()
    if choice == "1":
        player_dialogue_1 = f"{player_name}: You wrestle your date to the ground, grab their rucksack and map and run for cover"
        display_dialogue_1_to_3()
        text1_coversation13_part1()

    elif choice == "2":
        player_dialogue_2 = f"{player_name}: You plan how you’re going to kill your date before they kill you."
        li_dialogue_1 = ""
        display_dialogue_1_to_3()
        bad_ending()

    else:
        player_dialogue_3 = f"{player_name}: You appreciate their sense of humour."
        display_dialogue_1_to_3()
        text1_coversation13_part1()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Texting Event 10

def text1_coversation13_part1():

    global player_dialogue_1
    global player_dialogue_2
    global li_dialogue_1
    global li_dialogue_2
    global option_display_1
    global option_display_2
    global relation_points

    message = f"{li_name}: What football team do you support?"
    for char in message:
            sleep(0.05)
            sys.stdout.write(char)
            sys.stdout.flush()
    print("")
    print("")
    option_display_1 = "1.	I find football boring"
    option_display_2 = "2.	I follow Manchester because I see us as united"
    display_options_1_to_2()
    print("")
    print("")
    input_choice_1_to_2()
    if choice == "1":
        player_dialogue_1 = f"{player_name}: I find football boring"
        li_dialogue_1 = f"{li_name}: If you could travel anywhere, where would you go?"
        relation_points += 2
        display_dialogue_1_to_2()
        text1_coversation13_part2()
    else:
        player_dialogue_2 = f"{player_name}: I follow Manchester because I see us as united"
        li_dialogue_2 = f"{li_name}: If you could travel anywhere, where would you go?"
        relation_points += 5
        display_dialogue_1_to_2()
        text1_coversation13_part2()
    
def text1_coversation13_part2():

    global player_dialogue_1
    global player_dialogue_2
    global li_dialogue_1
    global li_dialogue_2
    global option_display_1
    global option_display_2
    global relation_points

    print("")
    print("")
    option_display_1 = "1.	Nowhere – I get travel sick."
    option_display_2 = "2.	You’re the only sight I need to see."
    display_options_1_to_2()
    print("")
    print("")
    input_choice_1_to_2()
    if choice == "1":
        player_dialogue_1 = f"{player_name}: Nowhere – I get travel sick."
        li_dialogue_1 = f"{li_name}: What is your relationship like with your family?"
        relation_points += 2
        display_dialogue_1_to_2()
        text1_coversation13_part3()

    else:
        player_dialogue_2 = f"{player_name}: You’re the only sight I need to see."
        li_dialogue_2 = f"{li_name}: What is your relationship like with your family?"
        relation_points += 5
        display_dialogue_1_to_2()
        text1_coversation13_part3()

def text1_coversation13_part3():

    global player_dialogue_1
    global player_dialogue_2
    global li_dialogue_1
    global li_dialogue_2
    global option_display_1
    global option_display_2
    global relation_points

    print("")
    print("")
    option_display_1 = "1.	I can’t stand my family"
    option_display_2 = "2.	I love my family and I know we’ll love ours."
    display_options_1_to_2()
    print("")
    print("")
    input_choice_1_to_2()
    if choice == "1":
        player_dialogue_1 = f"{player_name}: I can’t stand my family"
        li_dialogue_1 = f"{li_name}: What was your favourite class at school?"
        relation_points += 2
        display_dialogue_1_to_2()
        rp_notification()
        text1_coversation14_part1()
    else:
        player_dialogue_2 = f"{player_name}: I love my family and I know we’ll love ours."
        li_dialogue_2 = ""
        relation_points += 5
        display_dialogue_1_to_2()
        rp_notification()
        text1_coversation14_part1()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Texting Event 11

def text1_coversation14_part1():

    global player_dialogue_1
    global player_dialogue_2
    global li_dialogue_1
    global li_dialogue_2
    global option_display_1
    global option_display_2
    global relation_points

    print("")
    print("")
    option_display_1 = "1.	Physics, but I’m not Bohring"
    option_display_2 = "2.	None. School is for swots"
    display_options_1_to_2()
    print("")
    print("")
    input_choice_1_to_2()
    if choice == "1":
        player_dialogue_1 = f"{player_name}: Physics, but I’m not Bohring"
        li_dialogue_1 = f"{li_name}: : Do you believe in a higher power?"
        relation_points += 5
        display_dialogue_1_to_2()
        text1_coversation14_part2()
    else:
        player_dialogue_2 = f"{player_name}: None. School is for swots"
        li_dialogue_2 = f"{li_name}: : Do you believe in a higher power?"
        relation_points += 2
        display_dialogue_1_to_2()
        text1_coversation14_part2()
    
def text1_coversation14_part2():

    global player_dialogue_1
    global player_dialogue_2
    global li_dialogue_1
    global li_dialogue_2
    global option_display_1
    global option_display_2
    global relation_points

    print("")
    print("")
    option_display_1 = "1.	I believe in Santa."
    option_display_2 = "2.	Well you’re the answer to my prayers."
    display_options_1_to_2()
    print("")
    print("")
    input_choice_1_to_2()
    if choice == "1":
        player_dialogue_1 = f"{player_name}: I believe in Santa."
        li_dialogue_1 = f"{li_name}: What’s your favourite way to stay healthy?"
        relation_points += 2
        display_dialogue_1_to_2()
        text1_coversation14_part3()

    else:
        player_dialogue_2 = f"{player_name}: Well you’re the answer to my prayers."
        li_dialogue_2 = f"{li_name}: What’s your favourite way to stay healthy?"
        relation_points += 5
        display_dialogue_1_to_2()
        text1_coversation14_part3()

def text1_coversation14_part3():

    global player_dialogue_1
    global player_dialogue_2
    global li_dialogue_1
    global li_dialogue_2
    global option_display_1
    global option_display_2
    global relation_points

    print("")
    print("")
    option_display_1 = "1.	Going to Maccies for a breakfast sets me up for the day"
    option_display_2 = "2.	Burning off calories with you."
    display_options_1_to_2()
    print("")
    print("")
    input_choice_1_to_2()
    if choice == "1":
        player_dialogue_1 = f"{player_name}: Going to Maccies for a breakfast sets me up for the day"
        li_dialogue_1 = f"{li_name}: Recite some poetry to me"
        relation_points += 2
        display_dialogue_1_to_2()
        rp_notification()
        text1_coversation15_part1()
    else:
        player_dialogue_2 = f"{player_name}: Burning off calories with you."
        li_dialogue_2 = f"{li_name}: Recite some poetry to me"
        relation_points += 5
        display_dialogue_1_to_2()
        rp_notification()
        text1_coversation15_part1()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Texting Event 12

def text1_coversation15_part1():

    global player_dialogue_1
    global player_dialogue_2
    global li_dialogue_1
    global li_dialogue_2
    global option_display_1
    global option_display_2
    global relation_points

    print("")
    print("")
    option_display_1 = "1.	Roses are red, violets are blue, how would you like it if I came home with you?"
    option_display_2 = "2.	I hate poetry! You and me .. aren’t meant to be"
    display_options_1_to_2()
    print("")
    print("")
    input_choice_1_to_2()
    if choice == "1":
        player_dialogue_1 = f"{player_name}: Roses are red, violets are blue, how would you like it if I came home with you?"
        li_dialogue_1 = f"{li_name}: How much do you like me?"
        relation_points += 5
        display_dialogue_1_to_2()
        text1_coversation15_part2()
    else:
        player_dialogue_2 = f"{player_name}: I hate poetry! You and me .. aren’t meant to be"
        li_dialogue_2 = f"{li_name}: How much do you like me?"
        relation_points += 2
        display_dialogue_1_to_2()
        text1_coversation15_part2()
    
def text1_coversation15_part2():

    global player_dialogue_1
    global player_dialogue_2
    global li_dialogue_1
    global li_dialogue_2
    global option_display_1
    global option_display_2
    global relation_points

    print("")
    print("")
    option_display_1 = "1.	My love for you is like diarrhoea, I just can’t hold it in."
    option_display_2 = "2.	I love you from my head tomatoes."
    display_options_1_to_2()
    print("")
    print("")
    input_choice_1_to_2()
    if choice == "1":
        player_dialogue_1 = f"{player_name}: My love for you is like diarrhoea, I just can’t hold it in."
        li_dialogue_1 = f"{li_name}: I enjoy camping. How about you?"
        relation_points += 2
        display_dialogue_1_to_2()
        text1_coversation15_part3()

    else:
        player_dialogue_2 = f"{player_name}: I love you from my head tomatoes."
        li_dialogue_2 = f"{li_name}: I enjoy camping. How about you?"
        relation_points += 5
        display_dialogue_1_to_2()
        text1_coversation15_part3()

def text1_coversation15_part3():

    global player_dialogue_1
    global player_dialogue_2
    global li_dialogue_1
    global li_dialogue_2
    global option_display_1
    global option_display_2
    global relation_points

    print("")
    print("")
    option_display_1 = "1.	I’d love to sit round a campfire with you - because you’re hot and I want s’more!"
    option_display_2 = "2.	I tried it once but ended up with ants in my pants."
    display_options_1_to_2()
    print("")
    print("")
    input_choice_1_to_2()
    if choice == "1":
        player_dialogue_1 = f"{player_name}: I’d love to sit round a campfire with you - because you’re hot and I want s’more!"
        li_dialogue_1 = ""
        relation_points += 5
        display_dialogue_1_to_2()
        rp_notification()
        date4()
    else:
        player_dialogue_2 = f"{player_name}: I tried it once but ended up with ants in my pants."
        li_dialogue_2 = ""
        relation_points += 2
        display_dialogue_1_to_2()
        rp_notification()
        date4()


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Date Event 4

def date4():
    
    global player_dialogue_1
    global player_dialogue_2
    global player_dialogue_3
    global li_dialogue_1
    global li_dialogue_2
    global li_dialogue_3
    global option_display_1
    global option_display_2
    global option_display_3
    global relation_points

    print("")
    print("")
    event_start = f"Congratulations, you can now go on a date with {li_name}! You have both agreed to meet for coffee and so far the date is going really well. The conversation is flowing, you have lots of shared interests, and you even selected the same cappuccino and blueberry muffin. At the end of the date you both lean in for a kiss across the coffee table and … disaster strikes: your date burps in your mouth and isn’t even slightly apologetic!"
    option_display_1 = "1.	You ignore it – you burp all the time too and what’s a little excess gas between friends!"  
    option_display_2 = "2.	You draw attention to your date’s faux pas by announcing it to everyone in the coffee shop."
    option_display_3 = "3.	You let rip the loud, smelly fart you’ve been holding in to get your own back!"
    for char in event_start:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("")
    print("")
    display_options_1_to_3()
    print("")
    print("")
    input_choice_1_to_3()
    if choice == "1":
        player_dialogue_1 = f"{player_name}: You ignore it – you burp all the time too and what’s a little excess gas between friends!"
        display_dialogue_1_to_3()
        text1_coversation16_part1()

    elif choice == "2":
        player_dialogue_2 = f"{player_name}: You draw attention to your date’s faux pas by announcing it to everyone in the coffee shop."
        li_dialogue_1 = ""
        display_dialogue_1_to_3()
        bad_ending()

    else:
        player_dialogue_3 = f"{player_name}: You let rip the loud, smelly fart you’ve been holding in to get your own back!"
        display_dialogue_1_to_3()
        text1_coversation16_part1()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Texting Event 13

def text1_coversation16_part1():

    global player_dialogue_1
    global player_dialogue_2
    global li_dialogue_1
    global li_dialogue_2
    global option_display_1
    global option_display_2
    global relation_points

    message = f"{li_name}: Who do you live with?"
    for char in message:
            sleep(0.05)
            sys.stdout.write(char)
            sys.stdout.flush()
    print("")
    print("")
    option_display_1 = "1.	My mum and dad"
    option_display_2 = "2.	I’m waiting for you to move in with me"
    display_options_1_to_2()
    print("")
    print("")
    input_choice_1_to_2()
    if choice == "1":
        player_dialogue_1 = f"{player_name}: My mum and dad "
        li_dialogue_1 = f"{li_name}: Where do you like to shop for clothes?"
        relation_points += 2
        display_dialogue_1_to_2()
        text1_coversation16_part2()
    else:
        player_dialogue_2 = f"{player_name}: I’m waiting for you to move in with me"
        li_dialogue_2 = f"{li_name}: Where do you like to shop for clothes?"
        relation_points += 5
        display_dialogue_1_to_2()
        text1_coversation16_part2()
    
def text1_coversation16_part2():

    global player_dialogue_1
    global player_dialogue_2
    global li_dialogue_1
    global li_dialogue_2
    global option_display_1
    global option_display_2
    global relation_points

    print("")
    print("")
    option_display_1 = "1.	Brandy Melville."
    option_display_2 = "2.	I’m a big fan of thrifting. "
    display_options_1_to_2()
    print("")
    print("")
    input_choice_1_to_2()
    if choice == "1":
        player_dialogue_1 = f"{player_name}: Brandy Melville."
        li_dialogue_1 = f"{li_name}: What’s your favourite box of chocolates?"
        relation_points += 5
        display_dialogue_1_to_2()
        text1_coversation16_part3()

    else:
        player_dialogue_2 = f"{player_name}: I’m a big fan of thrifting. "
        li_dialogue_2 = f"{li_name}: What’s your favourite box of chocolates?"
        relation_points += 2
        display_dialogue_1_to_2()
        text1_coversation16_part3()

def text1_coversation16_part3():

    global player_dialogue_1
    global player_dialogue_2
    global li_dialogue_1
    global li_dialogue_2
    global option_display_1
    global option_display_2
    global relation_points

    print("")
    print("")
    option_display_1 = "1.	Any – as long as I don’t have to share!"
    option_display_2 = "2.	Celebrations – I’m always in the mood for celebrating now I’ve met you."
    display_options_1_to_2()
    print("")
    print("")
    input_choice_1_to_2()
    if choice == "1":
        player_dialogue_1 = f"{player_name}: Any – as long as I don’t have to share! "
        li_dialogue_1 = f"{li_name}: Can  you dance?"
        relation_points += 2
        display_dialogue_1_to_2()
        rp_notification()
        text1_coversation17_part1()
    else:
        player_dialogue_2 = f"{player_name}: Celebrations – I’m always in the mood for celebrating now I’ve met you."
        li_dialogue_2 = f"{li_name}: Can  you dance?"
        relation_points += 5
        display_dialogue_1_to_2()
        rp_notification()
        text1_coversation17_part1()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Texting Event 14

def text1_coversation17_part1():

    global player_dialogue_1
    global player_dialogue_2
    global li_dialogue_1
    global li_dialogue_2
    global option_display_1
    global option_display_2
    global relation_points

    print("")
    print("")
    option_display_1 = "1.	Only when nobody’s looking"
    option_display_2 = "2.	It takes two to Tango, so will you be my partner?"
    display_options_1_to_2()
    print("")
    print("")
    input_choice_1_to_2()
    if choice == "1":
        player_dialogue_1 = f"{player_name}: Only when nobody’s looking"
        li_dialogue_1 = f"{li_name}: If you were a piece of fruit what would you be?"
        relation_points += 2
        display_dialogue_1_to_2()
        text1_coversation17_part2()
    else:
        player_dialogue_2 = f"{player_name}: It takes two to Tango, so will you be my partner?"
        li_dialogue_2 = f"{li_name}: If you were a piece of fruit what would you be?"
        relation_points += 5
        display_dialogue_1_to_2()
        text1_coversation17_part2()
    
def text1_coversation17_part2():

    global player_dialogue_1
    global player_dialogue_2
    global li_dialogue_1
    global li_dialogue_2
    global option_display_1
    global option_display_2
    global relation_points

    print("")
    print("")
    option_display_1 = "1.	I’ve often been likened to a lemon."
    option_display_2 = "2.	A medium ripe pear – juicy, but firm."
    display_options_1_to_2()
    print("")
    print("")
    input_choice_1_to_2()
    if choice == "1":
        player_dialogue_1 = f"{player_name}: I’ve often been likened to a lemon."
        li_dialogue_1 = f"{li_name}: Do you have any body piercings?"
        relation_points += 2
        display_dialogue_1_to_2()
        text1_coversation17_part3()

    else:
        player_dialogue_2 = f"{player_name}: 2.	A medium ripe pear – juicy, but firm."
        li_dialogue_2 = f"{li_name}: Do you have any body piercings?"
        relation_points += 5
        display_dialogue_1_to_2()
        text1_coversation17_part3()

def text1_coversation17_part3():

    global player_dialogue_1
    global player_dialogue_2
    global li_dialogue_1
    global li_dialogue_2
    global option_display_1
    global option_display_2
    global relation_points

    print("")
    print("")
    option_display_1 = "1.	I’ll show you mine if you show me yours!"
    option_display_2 = "2.	No, I’m too much of a wimp."
    display_options_1_to_2()
    print("")
    print("")
    input_choice_1_to_2()
    if choice == "1":
        player_dialogue_1 = f"{player_name}: I’ll show you mine if you show me yours!"
        li_dialogue_1 = f"{li_name}: Are you good with your hands?"
        relation_points += 5
        display_dialogue_1_to_2()
        rp_notification()
        text1_coversation18_part1()
    else:
        player_dialogue_2 = f"{player_name}: 2.	No, I’m too much of a wimp."
        li_dialogue_2 = f"{li_name}: Are you good with your hands?"
        relation_points += 2
        display_dialogue_1_to_2()
        rp_notification()
        text1_coversation18_part1()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Texting Event 15

def text1_coversation18_part1():

    global player_dialogue_1
    global player_dialogue_2
    global li_dialogue_1
    global li_dialogue_2
    global option_display_1
    global option_display_2
    global relation_points

    print("")
    print("")
    option_display_1 = "1.	I can’t make anything to save my life"
    option_display_2 = "2.	Why don’t I show you just how good I can be!"
    display_options_1_to_2()
    print("")
    print("")
    input_choice_1_to_2()
    if choice == "1":
        player_dialogue_1 = f"{player_name}: I can’t make anything to save my life"
        li_dialogue_1 = f"{li_name}: If you were an animal, what would you be?"
        relation_points += 2
        display_dialogue_1_to_2()
        text1_coversation18_part2()
    else:
        player_dialogue_2 = f"{player_name}: Why don’t I show you just how good I can be!"
        li_dialogue_2 = f"{li_name}: If you were an animal, what would you be?"
        relation_points += 5
        display_dialogue_1_to_2()
        text1_coversation18_part2()
    
def text1_coversation18_part2():

    global player_dialogue_1
    global player_dialogue_2
    global li_dialogue_1
    global li_dialogue_2
    global option_display_1
    global option_display_2
    global relation_points

    print("")
    print("")
    option_display_1 = "1.	A dog – I’m loyal and I want to be your best friend."
    option_display_2 = "2.	A bear, so I could hibernate."
    display_options_1_to_2()
    print("")
    print("")
    input_choice_1_to_2()
    if choice == "1":
        player_dialogue_1 = f"{player_name}: A dog – I’m loyal and I want to be your best friend."
        li_dialogue_1 = f"{li_name}: How do you rate me?"
        relation_points += 5
        display_dialogue_1_to_2()
        text1_coversation18_part3()

    else:
        player_dialogue_2 = f"{player_name}: A bear, so I could hibernate."
        li_dialogue_2 = f"{li_name}: How do you rate me?"
        relation_points += 2
        display_dialogue_1_to_2()
        text1_coversation18_part3()

def text1_coversation18_part3():

    global player_dialogue_1
    global player_dialogue_2
    global li_dialogue_1
    global li_dialogue_2
    global option_display_1
    global option_display_2
    global relation_points

    print("")
    print("")
    option_display_1 = "1.	You’re off the scale!"
    option_display_2 = "2.	You’re pretty hot but not as hot as my ex."
    display_options_1_to_2()
    print("")
    print("")
    input_choice_1_to_2()
    if choice == "1":
        player_dialogue_1 = f"{player_name}: You’re off the scale!"
        li_dialogue_1 = ""
        relation_points += 5
        display_dialogue_1_to_2()
        rp_notification()
        date5()
    else:
        player_dialogue_2 = f"{player_name}: You’re pretty hot but not as hot as my ex. "
        li_dialogue_2 = ""
        relation_points -= 5
        display_dialogue_1_to_2()
        rp_notification()
        date5()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Date Event 5

def date5():
    
    global player_dialogue_1
    global player_dialogue_2
    global player_dialogue_3
    global li_dialogue_1
    global li_dialogue_2
    global li_dialogue_3
    global option_display_1
    global option_display_2
    global option_display_3
    global relation_points

    print("")
    print("")
    event_start = f"Congratulations, you can now go on a date with {li_name}! You have both agreed to see the latest blockbuster movie together, followed by a drink and a bite to eat afterwards. However, disaster strikes! Your date is a chatterbox, which wouldn’t be a problem if their chatter wasn’t all about the ex they loved and lost and never got over. Even during the film you had to hear all about how your date’s ex loved salted popcorn and wouldn’t have loved the movie you’re both watching. You even had to sit in the front row, right next to the left aisle, because that was the ex’s preference. Clearly your date would rather be on a date with their ex!"
    option_display_1 = "1.	You tell your date you’re just going to the loo but leave the cinema instead."  
    option_display_2 = "2.	You ask your date for their ex’s phone number, as they sound a more suitable match for you."
    option_display_3 = "3.	You love a challenge and you’re sure you can help your date finally get over their ex."
    for char in event_start:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("")
    print("")
    display_options_1_to_3()
    print("")
    print("")
    input_choice_1_to_3()
    if choice == "1":
        player_dialogue_1 = f"{player_name}: You tell your date you’re just going to the loo but leave the cinema instead."
        li_dialogue_1 = ""
        display_dialogue_1_to_3()
        bad_ending()

    elif choice == "2":
        player_dialogue_2 = f"{player_name}: You ask your date for their ex’s phone number, as they sound a more suitable match for you."
        li_dialogue_1 = ""
        display_dialogue_1_to_3()
        bad_ending()

    else:
        player_dialogue_3 = f"{player_name}: You love a challenge and you’re sure you can help your date finally get over their ex."
        li_dialogue_1 = ""
        display_dialogue_1_to_3()
        check_ending()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Ending 1

def good_ending():


    print()
    print()
    print()
    if li_name == "John Smith":
        print("""
                _____    ____
             .#########.#######..
          .#######################.
        .############################.
       .################################.
      .#########,##,#####################.
     .#########-#,'########## ############.
    .######'#-##' # ##'### #. `####:#######.
    #####:'# #'###,##' # # +#. `###:':######
   .####,'###,##  ###  # # #`#. -####`######.
  .####+.' ,'#  ##' #   # # #`#`.`#####::####
  ####'    #  '##'  #   #_'# #.## `#######;##
  #:##'      '       #   # ``..__# `#######:#
  #:##'  .#######s.   #.  .s######.\`#####:##
  #:##   ."______""'    '""_____"". `.#####:#
 .#:##   ><'(##)'> )    ( <'(##)`><   `####;#
 ##:##  , , -==-' '.    .` `-==- . \  ######'
 #|-'| / /      ,  :    : ,       \ ` :####:'
 :#  |: '  '   /  .     .  .  `    `  |`####
 #|  :|   /   '  '       `  \   . ,   :  #:# 
 #L. | | ,  /   `.-._ _.-.'   .  \ \  : ) J##
 ##\ `  /  '                   \  : : |  /##
 ## #|.:: '       _    _        ` | | |'####
 #####|\  |  (.-'.__`-'__.`-.)   :| ' ######
 ######\:      `-...___..-' '     :: /######
 #######\``.                   ,'|  /#######
 # ######\  \       ___       / /' /#######
 ##'#####|\  \    -     -    /  ,'|### #. #.
 `# #####| '-.`             ' ,-'  |### #  #
    #' `#|    '._         ,.-'     #`#`#.
         |       .'------' :       |#   #
         |       :         :       |
         |       :         :       |
                 :         :            """)

    elif li_name == "Jane Doe":
        print("""
              _...._
         _.dMMMMMMMMMb.
     ..dMMMMMMMMMMMMMMMb
   .dMMMMMMMMMMMMMMMMMMMMb.
  dMMMMMMMMMMMMMMMMMMMMMMMM.
  MMMMMMMP'`YMMMMMMMMMMMMMMMb
  MMMMMMP    MMMMMMMMMMMMMMMM
 dMMMMMP     `MMMMMMMMMMMMMMMb
 MMMMMM~=,,_  `MMMMMMMMMMMMMMM
 MMMMMMP,6;    `MMMMMMMMMMMMMMb
 MMMMMM|         ```^YMMMMMMMMM
 MMMMMM:   -~        / |MMMMMMMb
 `MMMMM/\  _.._     /  |MMMMMMMM
   `YMM\_`.`~--'    \__/MMMMMMMM!
     MMMMMM\       _.' _sS}MMMMMb
     `YMMMMMb.__.sP.---.  MMMMMMM
       ``YMMMMMMMP'        \MMMMMb
           ``MMMd;          MMMMMM
               dP|          :MMMMMb.
           _.sP'             :MMMMMM
       _.s888P'   ,  .-. .-. |MMMMM}
    .s888888P    ,_|(  fsc  )|MMMM
  .d88888888;     `\ `-._.-' ;;M'
  8888888888|       :         :;,
  8888888888;       |         |`;,_
  `Y88888888b     _,:         |/Y\;
     `^Y88888ssssSP~":        ;SsP/
         "" \        |         ;
             ;       |         |
             ;       ;         |
            /      .'          |
          .'    .-'            ;
         /_...-'             .':
        .'              _..-'   :
       /         __.--""         :""")

    else:
        print("""          ,     ,  ._  ,
                _.MMmm.mMm_Mm.MMm_:mMMmmm.._  .
           _ .-mmMMMMMMMMMMMMm:MMm:MMMMMMMMMm._
            `-.mm.MMMMMMM:MMMMMMMmmMMMMMMMMMmm._
         _.mMMMMMmMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM"~.
          .MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm._
         _.MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm._
      ..mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmmm.
     _.mmMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm.
      _.MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm_
  .mmMMMMMMMMMMMMMMMMMMMMMMMM' `MMMMMMMMMMMMMMMMMMMMMMm,
 _.-' _.mMMMMMMMMMMMMMMMMMMM'      `MMMMMMMMMMMMMMMM""`
  _,MMMmMMMMMMMMMMMMMMMM'            `MMMMMMMMMMMMMMmm.
    _.-'MMMMMMMMMMMMMMM.'""`.    ,'""`.MMMMMMMMMMMMMMMM.
   .mmMMMMMMMMMMMMMMMM' <(o)>`  '<(o)>` MMMMMMMMMMMMMMMm.
      .MMMMMMMMMMMMMMM                 'MMMMMMMMMMMMMMM:
   ,MMMmMMMMMMMMMMMMM'                 `MMMMMMMMMMMMmm.
  ,ME:MMMMMMMMMMMMMM_6       -  -       7_MMMMMMMMM:Mm_
  !M:MmmMMMMMMMMMMMMML_                _JMMMMMMMMMm:MMm.
  '':mMMMMMMMMMMMMMMMM\     ______     /dMMMMMMMMMMM:'Mm.
   ':MMM:MMMMMMMMMMMMMM\    `.__.'    /MMMMMM:MMMMMMm: `
  .M:MMM:MMMMMMMMMMMMMMM`.          ,'MMMMMMM:MMMMMMMm
    .Mm:mMMMMMMMMMMMMMMM| `.      .' |MMMMMMm:.MMMMM.
   .Mm:mMMMMMMMMMMMMMMMM|   `----':: |MMMMMMMmm`MMMMMm.
     !:mMMMMMMMMMMMMMMMM|      ::::. |MMMMMMMMMMM``mMm.
       !MMMMMMMMM'MMMMMM|      .:::. |MMMMMMMMMMMMM.._
       MMMMMMMMM'MMMM'M/       ::::'  \MMMMMMMMMMMMMMm,
      .mMMMMMMM'MMMM'MMm.       '     .`".MMMMMMMMMMMMm.
       !!JmMMM'MMM' `M:.      ,  ,     .. M.".MMMMMMMMm.
        FMMMMMm.`M   M..              .. `Mm   `"".MMMmm.
        MMMM'    M      ..           ..    `M      MM`.M!
        Mm'               ..        ..      M      M'   :
        /                                                \ """)


    print()
    print()
    print()


    ending_narration = "Congratulations! You and your date are very well matched and are officially a Dynamic Dating couple."
    for char in ending_narration:
            sleep(0.05)
            sys.stdout.write(char)
            sys.stdout.flush()
    pass

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Ending 2

def bad_ending():

    print()
    print()
    print()
    if li_name == "John Smith":
        print("""
                _____    ____
             .#########.#######..
          .#######################.
        .############################.
       .################################.
      .#########,##,#####################.
     .#########-#,'########## ############.
    .######'#-##' # ##'### #. `####:#######.
    #####:'# #'###,##' # # +#. `###:':######
   .####,'###,##  ###  # # #`#. -####`######.
  .####+.' ,'#  ##' #   # # #`#`.`#####::####
  ####'    #  '##'  #   #_'# #.## `#######;##
  #:##'      '       #   # ``..__# `#######:#
  #:##'  .#######s.   #.  .s######.\`#####:##
  #:##   ."______""'    '""_____"". `.#####:#
 .#:##   ><'(##)'> )    ( <'(##)`><   `####;#
 ##:##  , , -==-' '.    .` `-==- . \  ######'
 #|-'| / /      ,  :    : ,       \ ` :####:'
 :#  |: '  '   /  .     .  .  `    `  |`####
 #|  :|   /   '  '       `  \   . ,   :  #:# 
 #L. | | ,  /   `.-._ _.-.'   .  \ \  : ) J##
 ##\ `  /  '                   \  : : |  /##
 ## #|.:: '       _    _        ` | | |'####
 #####|\  |  (.-'.__`-'__.`-.)   :| ' ######
 ######\:      `-...___..-' '     :: /######
 #######\``.                   ,'|  /#######
 # ######\  \       ___       / /' /#######
 ##'#####|\  \    -     -    /  ,'|### #. #.
 `# #####| '-.`             ' ,-'  |### #  #
    #' `#|    '._         ,.-'     #`#`#.
         |       .'------' :       |#   #
         |       :         :       |
         |       :         :       |
                 :         :            """)

    elif li_name == "Jane Doe":
        print("""
              _...._
         _.dMMMMMMMMMb.
     ..dMMMMMMMMMMMMMMMb
   .dMMMMMMMMMMMMMMMMMMMMb.
  dMMMMMMMMMMMMMMMMMMMMMMMM.
  MMMMMMMP'`YMMMMMMMMMMMMMMMb
  MMMMMMP    MMMMMMMMMMMMMMMM
 dMMMMMP     `MMMMMMMMMMMMMMMb
 MMMMMM~=,,_  `MMMMMMMMMMMMMMM
 MMMMMMP,6;    `MMMMMMMMMMMMMMb
 MMMMMM|         ```^YMMMMMMMMM
 MMMMMM:   -~        / |MMMMMMMb
 `MMMMM/\  _.._     /  |MMMMMMMM
   `YMM\_`.`~--'    \__/MMMMMMMM!
     MMMMMM\       _.' _sS}MMMMMb
     `YMMMMMb.__.sP.---.  MMMMMMM
       ``YMMMMMMMP'        \MMMMMb
           ``MMMd;          MMMMMM
               dP|          :MMMMMb.
           _.sP'             :MMMMMM
       _.s888P'   ,  .-. .-. |MMMMM}
    .s888888P    ,_|(  fsc  )|MMMM
  .d88888888;     `\ `-._.-' ;;M'
  8888888888|       :         :;,
  8888888888;       |         |`;,_
  `Y88888888b     _,:         |/Y\;
     `^Y88888ssssSP~":        ;SsP/
         "" \        |         ;
             ;       |         |
             ;       ;         |
            /      .'          |
          .'    .-'            ;
         /_...-'             .':
        .'              _..-'   :
       /         __.--""         :""")

    else:
        print("""          ,     ,  ._  ,
                _.MMmm.mMm_Mm.MMm_:mMMmmm.._  .
           _ .-mmMMMMMMMMMMMMm:MMm:MMMMMMMMMm._
            `-.mm.MMMMMMM:MMMMMMMmmMMMMMMMMMmm._
         _.mMMMMMmMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM"~.
          .MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm._
         _.MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm._
      ..mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmmm.
     _.mmMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm.
      _.MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm_
  .mmMMMMMMMMMMMMMMMMMMMMMMMM' `MMMMMMMMMMMMMMMMMMMMMMm,
 _.-' _.mMMMMMMMMMMMMMMMMMMM'      `MMMMMMMMMMMMMMMM""`
  _,MMMmMMMMMMMMMMMMMMMM'            `MMMMMMMMMMMMMMmm.
    _.-'MMMMMMMMMMMMMMM.'""`.    ,'""`.MMMMMMMMMMMMMMMM.
   .mmMMMMMMMMMMMMMMMM' <(o)>`  '<(o)>` MMMMMMMMMMMMMMMm.
      .MMMMMMMMMMMMMMM                 'MMMMMMMMMMMMMMM:
   ,MMMmMMMMMMMMMMMMM'                 `MMMMMMMMMMMMmm.
  ,ME:MMMMMMMMMMMMMM_6       -  -       7_MMMMMMMMM:Mm_
  !M:MmmMMMMMMMMMMMMML_                _JMMMMMMMMMm:MMm.
  '':mMMMMMMMMMMMMMMMM\     ______     /dMMMMMMMMMMM:'Mm.
   ':MMM:MMMMMMMMMMMMMM\    `.__.'    /MMMMMM:MMMMMMm: `
  .M:MMM:MMMMMMMMMMMMMMM`.          ,'MMMMMMM:MMMMMMMm
    .Mm:mMMMMMMMMMMMMMMM| `.      .' |MMMMMMm:.MMMMM.
   .Mm:mMMMMMMMMMMMMMMMM|   `----':: |MMMMMMMmm`MMMMMm.
     !:mMMMMMMMMMMMMMMMM|      ::::. |MMMMMMMMMMM``mMm.
       !MMMMMMMMM'MMMMMM|      .:::. |MMMMMMMMMMMMM.._
       MMMMMMMMM'MMMM'M/       ::::'  \MMMMMMMMMMMMMMm,
      .mMMMMMMM'MMMM'MMm.       '     .`".MMMMMMMMMMMMm.
       !!JmMMM'MMM' `M:.      ,  ,     .. M.".MMMMMMMMm.
        FMMMMMm.`M   M..              .. `Mm   `"".MMMmm.
        MMMM'    M      ..           ..    `M      MM`.M!
        Mm'               ..        ..      M      M'   :
        /                                                \ """)


    print()
    print()
    print()
    ending_narration = "Oh dear, you and your date are not very compatible! Don’t worry, Dynamic Dating has plenty more potential dates for you to message. Keep swiping!"
    for char in ending_narration:
            sleep(0.05)
            sys.stdout.write(char)
            sys.stdout.flush()
    pass

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Event Skeleton/Template

def four_options():
    
    global player_dialogue_1
    global player_dialogue_2
    global player_dialogue_3
    global player_dialogue_4
    global li_dialogue_1
    global li_dialogue_2
    global li_dialogue_3
    global li_dialogue_4
    global option_display_1
    global option_display_2
    global option_display_3
    global option_display_4

    print("")
    print("")
    event_start = "Choose a topic of conversation from 1 to 4."
    option_display_1 = "potential player choice 1 goes here"  #Start of game dialogue goes here
    option_display_2 = "potential player choice 2 goes here"
    option_display_3 = "potential player choice 3 goes here"
    option_display_4 = "potential player choice 4 goes here"
    for char in event_start:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("")
    print("")
    display_options_1_to_4()
    print("")
    print("")
    input_choice_1_to_4()
    if choice == "1":
        player_dialogue_1 = f"{player_name}: Insert Player Dialogue Here"
        li_dialogue_1 = f"{li_name}: Insert Love Interest Response Dialogue Here"
        display_dialogue_1_to_4()

    elif choice == "2":
        player_dialogue_2 = f"{player_name}: Insert Player Dialogue Here"
        li_dialogue_2 = f"{li_name}: Insert Love Interest Response Dialogue Here"
        display_dialogue_1_to_4()

    elif choice == "3":
        player_dialogue_3 = f"{player_name}: Insert Player Dialogue Here"
        li_dialogue_3 = f"{li_name}: Insert Love Interest Response Dialogue Here"
        display_dialogue_1_to_4()

    else:
        player_dialogue_4 = f"{player_name}: Insert Player Dialogue Here"
        li_dialogue_4 = f"{li_name}: Insert Love Interest Response Dialogue Here"
        display_dialogue_1_to_4() 
    
def three_options():
    
    global player_dialogue_1
    global player_dialogue_2
    global player_dialogue_3
    global li_dialogue_1
    global li_dialogue_2
    global li_dialogue_3
    global option_display_1
    global option_display_2
    global option_display_3

    print("")
    print("")
    event_start = "Choose a topic of conversation from 1 to 3."
    option_display_1 = "potential player choice 1 goes here"  
    option_display_2 = "potential player choice 2 goes here"
    option_display_3 = "potential player choice 3 goes here"
    for char in event_start:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("")
    print("")
    display_options_1_to_4()
    print("")
    print("")
    input_choice_1_to_4()
    if choice == "1":
        player_dialogue_1 = f"{player_name}: Insert Player Dialogue Here"
        li_dialogue_1 = f"{li_name}: Insert Love Interest Response Dialogue Here"
        display_dialogue_1_to_3()

    elif choice == "2":
        player_dialogue_2 = f"{player_name}: Insert Player Dialogue Here"
        li_dialogue_2 = f"{li_name}: Insert Love Interest Response Dialogue Here"
        display_dialogue_1_to_3()

    else:
        player_dialogue_3 = f"{player_name}: Insert Player Dialogue Here"
        li_dialogue_3 = f"{li_name}: Insert Love Interest Response Dialogue Here"
        display_dialogue_1_to_3()
    
def two_options():

    global player_dialogue_1
    global player_dialogue_2
    global li_dialogue_1
    global li_dialogue_2
    global option_display_1
    global option_display_2

    print("")
    print("")
    option_display_1 = "Potential player choice 1 goes here"
    option_display_2 = "Potential player choice 2 goes here"
    display_options_1_to_2()
    print("")
    print("")
    input_choice_1_to_2()
    if choice == "1":
        player_dialogue_1 = f"{player_name}: Insert Player Dialogue Here"
        li_dialogue_1 = f"{li_name}: Insert Love Interest Response Dialogue Here"
        display_dialogue_1_to_2()

    else:
        player_dialogue_2 = f"{player_name}: Insert Player Dialogue Here"
        li_dialogue_2 = f"{li_name}: Insert Love Interest Response Dialogue Here"
        display_dialogue_1_to_2()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Run the Game

run_game()

# RANDOM MESSAGE TO MYSELF (STEVEN): SO WE COVER LISTS, HAVE SOME OF THE DATES PICK A RANDOM INDEX WITHIN A LIST AS THE NAME FOR SOMETHING.

# Select name -> Swipe Menu (swipe one way to deny, one way to accept. Each profile shown contains vague image representing male, female and nondescript gender,
# a bio about them including name and age but not including gender because eh, we don't need to pin anyone down.) -> Texting event 1 -> date event 1 -> text event 2 
# etc up to 6th text and date event -> good or bad based on points threshold.


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#▂▃▅▇█▓▒░۩۞۩ We do be pogging ۩۞۩░▒▓█▇▅▃▂