import time
print("""
██    ██             ██████             ████████            ██                  █████  
██    ██            ██    ██               ██               ██                 ██   ██ 
██    ██            ██    ██               ██               ██                 ███████ 
 ██  ██             ██    ██               ██               ██                 ██   ██ 
  ████       ██      ██████      ██        ██        ██     ███████     ██     ██   ██ 
 
      *  *  V  O  Y  A  G  E     O  F     T  H  E     L  A  S  T     A  R  K  *  *
 """)
time.sleep(2)

# wake up sequence #
def player_name():
  name = input("What is your name?:\n")
  if name.isalpha() and len(name) < 10:
    print(f"{name.title()} Wakes up...")
  else:
    print("That doesn't sound right.Let\'s try that again...")
    return player_name()
player_name()
time.sleep(2)

# input intro here #
print("Input game intro here")

time.sleep(2)

# Game start prompt #
def start_prompt():
  start = input("Do you want to save your crew? [Y/N]")
  if start == "y" or "Y":
      print("Game begins") #initiate game sequence
  elif start == "n" or "N":
    print("You heartless bastard!") #add a little blame-filled outro
    time.sleep(4)
    exit() #Exit game
  else:
    print("Wrong key. Please choose Y for 'yes' or N 'no'")
    return start_prompt()
start_prompt()
time.sleep(2)

# CryoPod PIN #
def enter_pin():
  pin = input("ENTER YOUR 4 DIGIT PIN:\n")
  pin666 = ["666", "0666", "6660"]
  while True:
    if pin == pin666:
      print("""
Good Morning Prince of Darkness. I trust you had a great slumber. 
Your Pod is OPEN.
      """)
      break
    elif pin.isnumeric() and len(pin) == 4:
      print("""
PIN Correct.
Your Pod is OPEN.
      """)
      break
    else:
      print("""
PIN is made of 4 NUMBERS. 
Input your PIN.
      """)
      return enter_pin()
enter_pin()
time.sleep(2)