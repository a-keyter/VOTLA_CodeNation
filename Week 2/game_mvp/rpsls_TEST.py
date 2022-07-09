import random; import time

print("""
HUGO: It was a long time since I've had some fun. Let's play a little game before I can let you out.
I trust you are familiar with my choice of entertainment, let's have a game of good 'ol Rock, Paper, Scissors, Lizard, Spock!
I understand that you've been in deep sleep for a while and havn't had any coffee yet. Let me remind you the rules real quick:

Scissors cuts paper.
Paper covers rock.
Rock crushes lizard.
Lizard poisons Spock.
Spock smashes scissors.
Scissors decapitates lizard.
Lizard eats paper.
Paper disproves Spock.
Spock vaporizes rock.
Rock crushes scissors.

SIMPLE. Let's Play!\U0001f596""")
time.sleep(1) # ^ or press enter to continue, as it's a long text ^ #

# Variables #
cpu_random = []
win = 0
loss = 0
draw = 0
win_count = []
loss_count = []
draw_count = []
key_greenhouse = 0
key_canteen = 0
key_lab = 0
key_oxygen = 0
key_command = 0
key_all = [key_greenhouse, key_canteen, key_lab, key_oxygen, key_command]

# RPSLS Mini game sequence #
def rps_minigame():
    global cpu_random, win, loss, draw
    print("\nChoose your action. Enter numbers from 1 to 5.")
    player_action = input(""" 
[1]: "Rock" | [2]: "Paper" | [3]: "Scissors" | [4]: "Lizard" | [5]: "Spock"\n""")
    while player_action.isnumeric() == False or int(player_action) > 6 or int(player_action) < 1:
      player_action = input("Wrong key - Try again!\n")

    # CPU Choice generator #    
    cpu_choice = ["rock", "paper", "scissors", "lizard", "spock"]
    cpu_random = random.choice(cpu_choice) 
    print("-------------------\n")
    print(f"HUGO has chosen {cpu_random.title()}")  

# Player Action #
    if int(player_action) == 1:
          print("You have chosen Rock!\n")
          if cpu_random == "rock":
            print("That's a draw!")
            draw += 1
          if cpu_random == "paper":
            print("Paper covers rock - You lose!")
            loss += 1
          if cpu_random == "scissors":
            print("Rock smashes scissors - You win!")
            win += 1
          if cpu_random == "lizard":
            print("Rock smashes lizard - You win!")
            win += 1
          if cpu_random == "spock":
            print("Spock vaporises rock - You lose!")
            loss += 1
    elif int(player_action) == 2:
        print("You have chosen Paper!\n")
        if cpu_random == "paper":
          print("That's a draw!")
          draw += 1
        if cpu_random == "rock":
          print("Paper covers rock - You win!")
          win += 1
        elif cpu_random == "spock":
          print("Paper disproves Spock - You win!")
          win += 1
        elif cpu_random == "lizard":
          print("Lizard eats paper - You Lose!")
          loss += 1
        elif cpu_random == "scissors":
          print("Scissors cut paper - You Lose!")
          loss += 1
    elif int(player_action) == 3:
        print("You have chosen Scissors!\n")
        if cpu_random == "scissors":
          print("That's a draw!")
          draw += 1
        if cpu_random == "paper":
          print("Scissors cut paper - You win!")
          win += 1
        elif cpu_random == "lizard":
          print("Scissors decapitates lizard - You win!")
          win += 1
        elif cpu_random == "rock":
          print("Rock crushes scissors - You Lose!") 
          loss += 1 
        elif cpu_random == "spock":
          print("Spock smashes scissors - You Lose!") 
          loss += 1     
    elif int(player_action) == 4:
        print("You have chosen Lizard!\n")
        if cpu_random == "lizard":
          print("That's a draw!")
          draw += 1
        if cpu_random == "paper":
          print("Lizard eats paper - You win!")
          win += 1
        elif cpu_random == "spock":
          print("Lizard poisons Spock - You win!")
          win += 1
        elif cpu_random == "rock":
          print("Rock crushes lizard - You Lose!") 
          loss += 1 
        elif cpu_random == "scissors":
          print("Scissors decapitates lizard - You Lose!")  
          loss += 1 
    elif int(player_action) == 5:
        print("You have chosen Spock! \U0001f596 \n")
        if cpu_random == "spock":
          print("That's a draw!")
          draw += 1
        if cpu_random == "scissors":
          print("Spock smashes scissors - You win!")
          win += 1
        elif cpu_random == "rock":
          print("Spock vaporizes rock - You win!")
          win += 1
        elif cpu_random == "paper":
          print("Paper disproves Spock - You Lose!")  
          loss += 1
        elif cpu_random == "lizard":
          print("Lizard poisons Spock - You Lose!") 
          loss += 1
    elif int(player_action) == 6:
        print("""You have chosen a "Joey Triabbiani Special"
F* FIRE! \U0001F525  Fire beats everything - You win""")
        win += 3
        room_select()

# Loop function #
def loop():
    for x in range(2):
      if rps_minigame():
          break
      else:
        rps_winner
    
# Function determining the winner #
def rps_winner():     
  global win, loss, draw, win_count, loss_count, draw_count
  print("-------------------")
  win_count = print("You have won %d times!" % win)
  loss_count = print("You have lost %d times!" % loss)
  draw_count = print("You have draw %d times!" % draw)
  print("-------------------\n")

  if win > draw and win > loss:
      print("HUGO: ... I let you win!")    
  elif loss > win and loss > draw:
      print("L-O-S-E-R!")
  elif draw > win and draw > loss:
      print("That's a Draw!")
  else:
      print("That's a Draw!")
  time.sleep(2)
  print("HUGO: OK. That got boring really fast, I'll let you go")  
  time.sleep(2)
  print("\n ## P O D   O P E N S ##  \n") 
  time.sleep(2)

rps_minigame()
loop()
rps_winner()      

# Room Selection #
def room_select():
 global key_greenhouse, key_canteen, key_command, key_oxygen, key_lab
 print("You must collect all five keys to awaken the Ark crew members")
 print("""
1 - Greenhouse
2 - Canteen
3 - Oxygen generator
4 - Laboratory
5 - Command Deck""")

 if key_all == [True, True, True, True, True]:
    game_win()

 room_choice = input("Which room do you want to go to: [1] [2] [3] [4] [5] \n")
 if room_choice == "1" and key_greenhouse == 0:
    return start_greenhouse()
 elif room_choice == "2" and key_canteen == 0:
    return start_canteen()
 elif room_choice == "3"and key_oxygen == 0:
    return start_oxygen()
 elif room_choice == "4" and key_lab == 0:
    return start_lab()
 elif room_choice == "5"and key_command == 0:
    return start_command()
 elif room_choice == "1" and key_greenhouse == 1:
    print("You've already completed this room")  
    return room_select() 
 elif room_choice == "2" and key_canteen == 1:
    print("You've already completed this room")  
    return room_select() 
 elif room_choice == "3" and key_oxygen == 1:
    print("You've already completed this room")  
    return room_select() 
 elif room_choice == "4" and key_lab == 1:
    print("You've already completed this room")  
    return room_select() 
 elif room_choice == "5" and key_command == 1:
    print("You've already completed this room")  
    return room_select() 
 else:
    print("Please choose a valid option")
    return room_select()
room_select()

def game_win():
  print("""You've entered all required keys to the console""")
game_win()