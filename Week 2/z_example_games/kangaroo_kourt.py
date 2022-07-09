# all imports:
import sys,time
import sys
from datetime import date
from datetime import datetime



# all variables:
name = input
karma= 0
num = 4
space = "                                        "
space2 ="        "




#all lists:
list_choice = ["Roll eyes",
    "Cry"]
    
list_question1 = [
    "I only met him a week ago...",
    "I met him once a long time ago , just a short romance...  you know how it is...",
    "We just had a couple of pints at the pub together, that's all I remember...",
    "I have never seen him in my life, I swear!!!"]
list_question2 = [
    "I was at home watching youtube.",
    "I was in town center last night, just walking around.",
    "As I said.. I was drinking beer at the pub..and actually I don't remember anything."]

list_question3 = [
    "He's my sparring partner at the gym.",
    "I went on a few dates with him but nothing came of it, he was a little jumpy.",
    "I don't know him, I've never met him."
] 
list_question4 = [
    "Yeah, you could say we were on good terms.",
    "No, not really, he became slightly obsessive when I turned him down after a few dates.",
    "No, he was obsessed wih shadow boxing when he had a few drinks and got me a few times.",
    "OBJECTION!!" ] 
list_opinions=[
    "Aggressive",
    "Sympathetic",
    "Let him decide"] 
list_witness_stand= [
    "Get up",
    "Remain seated",
    ]
list_defendant_plead= ["I'm not guilty", "Guilty","This is a kangaroo court!!!"]


# main functions:
# scores of player

def lose_karma():
    global karma
    karma -= 5
def gain_karma():
    global karma
    karma += 5
# printing text one by one letter
def print_slow(txt):
        for letter in txt:
                sys.stdout.write(letter)
                sys.stdout.flush()
                time.sleep(0.05)
def print_banner(txt):
        for letter in txt:
                sys.stdout.write(letter)
                sys.stdout.flush()
                time.sleep(0.01)
#  printing list with index 
def list_serial(list):
    for index in range(len(list)):
        print(str(index + 1) + ". " + list[index])
    print("\n")
    return ""
#  current date
today = date.today()
current_date = today.strftime("%B %d, %Y")
#  current time
now = datetime.now()
current_time = now.strftime("%H:%M:%S")


def end():
    print_banner("""\033[1;32;40m
    .----------------.  .----------------.  .----------------.   .----------------.  .-----------------. .----------------.   
| .--------------. || .--------------. || .--------------. | | .--------------. || .--------------. || .--------------. |  
| |  _________   | || |  ____  ____  | || |  _________   | | | |  _________   | || | ____  _____  | || |  ________    | |  
| | |  _   _  |  | || | |_   ||   _| | || | |_   ___  |  | | | | |_   ___  |  | || ||_   \|_   _| | || | |_   ___ `.  | |  
| | |_/ | | \_|  | || |   | |__| |   | || |   | |_  \_|  | | | |   | |_  \_|  | || |  |   \ | |   | || |   | |   `. \ | |  
| |     | |      | || |   |  __  |   | || |   |  _|  _   | | | |   |  _|  _   | || |  | |\ \| |   | || |   | |    | | | |  
| |    _| |_     | || |  _| |  | |_  | || |  _| |___/ |  | | | |  _| |___/ |  | || | _| |_\   |_  | || |  _| |___.' / | |  
| |   |_____|    | || | |____||____| | || | |_________|  | | | | |_________|  | || ||_____|\____| | || | |________.'  | |  
| |              | || |              | || |              | | | |              | || |              | || |              | |  
| '--------------' || '--------------' || '--------------' | | '--------------' || '--------------' || '--------------' |  
'----------------'  '----------------'  '----------------'   '----------------'  '----------------'  '----------------'   

""")
    quit()



#intro
print("\033[0;1;35;40m")
print("kang          kang")
print("kang         kang")
print("kang        kang")
print("kang       kang")
print("kang      kang")
print("kang     kang")
print("kang    kang")
print("kang   kang")
print("kang  kang")
print("kang kang")
print("kang  kang")
print("kang   kang")
print("kang    kang")
print("kang     kang            aroo aroo       kang kang      kang    aroo aroo aroo       kang kang")
print("kang      kang          aroo   aroo      kang  kang     kang   aroo                 kang   kang")
print("kang       kang        aroo     aroo     kang   kang    kang  aroo                 kang     kang")
print("kang        kang      aroo  aro  aroo    kang    kang   kang  aroo   aroo aroo    kang  kan  kang")
print("kang         kang    aroo         aroo   kang     kang  kang   aroo       aroo   kang         kang")
print("kang          kang  aroo           aroo  kang      kang kang    aroo aroo aroo  kang           kang")
print("\033[0;31;40m")
print("-----------------------------------------------------------------------------------------------------")
print("\033[1;32;40m")
print("                            aroo aro aroo    kang kan kan    aro ar aroo")
print("                            aroo      aroo  kang      kang  aroo     aroo")
print("                            aroo aro aroo   kang kan  kang  aroo aro aroo")
print("                            aroo  aroo      kang   ka kang  aroo  ar aroo")
print("                            aroo   aroo     kang      kang  aroo     aroo")
print("                            aroo    aroo     kang kan kan    aro ar aroo")
print("\033[0;31;40m")
print("-----------------------------------------------------------------------------------------------------")
print("\033[1;33;40m")
print("kang         kang"                                                                                                                                                                               )
print("kang        kang")
print("kang       kang")
print("kang      kang")
print("kang     kang")
print("kang    kang")
print("kang   kang")
print("kang  kang")
print("kang kang")
print("kang  kang")
print("kang   kang")
print("kang    kang")
print("kang     kang       aro ar aroo   kang          kang  aroo aro aroo   kang kang kang")
print("kang      kang     aroo     aroo  kang          kang  aroo      aroo       kang")
print("kang       kang    aroo aro aroo  kang          kang  aroo aro aroo        kang")
print("kang        kang   aroo  ar aroo  kang          kang  aroo    aroo         kang")
print("kang         kang  aroo     aroo  kang          kang  aroo     aroo        kang")
print("kang          kang  aro ar aroo    kang kan ka kang   aroo      aroo       kang")
print("--------------------------------------------------------------------------------------------")
time.sleep(4)
def intro():
    print_slow("\033[1;34;40mBAILIFF: All rise!")
    print("\n\n")
    print_slow("\033[0;37;40mAround you, the entire court sprouts to their feet. You follow suit - noticeably slower.")
    print("\n\n")
    print_slow(f"\033[1;34;40mBAILIFF: Hear ye, hear ye. {current_date} at {current_time}")
    print("\n\n")
    print_slow("\033[0;37;40mThe JUDGE enters the room. Slowly, he walks up to his podium, towering over the court and planting himself down.")
    print("\n\n")
    print_slow("\033[1;34;40mBAILIFF: All persons having business before the San Diego Zoo's Court of California. Draw near and ye shall be heard. ")
    print("\n")
    print_slow("JUDGE SOLOMON SCOFFMAN presiding.")
    print("\n\n")
    print_slow("\033[0;37;40mThe JUDGE fusses around in his seat before proceeding.")
    print("\n\n")
    print_slow("\033[1;32;40mJUDGE: Be seated.")
    print("\n\n")
    print_slow("\033[0;37;40mIn unison, everyone except you sits, leaving you awkwardly standing. You hesitantly sit back down hoping no one noticed.")
    print("\n\n")
    print_slow("\033[1;32;40mJUDGE: Transcriber, please call the case.")
    print("\n\n")
    print_slow("\033[1;35;40mTRANSCRIBER: 40 SD 130. San Diego Zoo Court V... hmm. That's strange. There's no name.")
    print("\n\n")
    print_slow("\033[1;32;40mJUDGE: Will the defendant please rise and state their name for the KangaKourt.")
    print("\n\n\033[0;37;40m")
    global name
    name = input()
    print("\n")
    print_slow(f"\033[1;32;40mJUDGE: {name}, well then, please take your seat.")
    print("\n\n")       
    print_slow("\033[0;37;40mYou plonk back down in your seat.")
    print("\n\n")
    print_slow("\033[1;32;40mJUDGE: Are the people ready to make their opening arguments?")
    print("\n\n")
    print_slow("\033[1;31;40mPROSECUTOR: We are, your honour.")
    print("\n\n")

intro()
def opening_statements():
    print_slow("\033[0;37;40mThe PROSECUTOR jumps to her feet, striding to the centre of the courtroom. Turning to her right, she looks at the jury. ")
    print("\n")
    print_slow("They all stare in anticipation." )
    print("\n\n")
    print_slow("\033[1;31;40mPROSECUTOR: Ladies and gentlemen, thank you for all coming in today. As you know, a horrific crime has occurred.")
    print("\n\n")
    print_slow("\033[0;37;40mShe looks down in shame.")
    print("\n\n")
    print_slow("\033[1;31;40mPROSECUTOR: Our most beloved Joey was kidnapped.")
    print("\n\n")
    print_slow("\033[0;37;40mThe Jury gasp!")
    print("\n\n")
    print_slow("\033[1;31;40mPROSECUTOR: And we believe they are to blame!")
    print("\n\n")
    print_slow("\033[0;37;40mShe points at YOU!")
    print("\n\n")
    print_slow("\033[1;31;40mPROSECUTOR: For this the crime of kidnapping of a marsupial, we call for the ultimate punishment...")
    print("\n")
    print_slow("\033[1;31;40mPROSECUTOR: EXECUTION!")
    print("\n\n")
    print_slow("\033[0;37;40mAs she returns to her seat, you feel a prod to your left side, to which you see a smirking balding man with gigantic circular glasses. ")
    print("\n")
    print_slow("He is dressed in an ill-fitting, heavily worn, brown suit with a bright yellow and purple polka dot tie.")
    print("\n\n")
    print_slow(f"\033[1;33;40mLAWYER: Hey {name}, don't worry, we've got this case. Now listen up, it's going to be tough but I've done my research. ")
    print("\n")
    print_slow("See, I've got this kangaroo theory and am well versed in kangaroo law.")
    print("\n")
    def choices():
        def choice1():
            print("\033[0;37;40m")
            print_slow("\033[0;37;40mYour eyes almost roll out of your head.")
        def choice2():
            print_slow("\033[0;37;40mYou sob uncontrollably.")
        print("\033[0;37;40m" )
        print_slow(list_serial(list_choice))
        choice = input()
        if choice == "1":
            choice1()
        elif choice == "2":
            choice2()
        else:
            print("\n\n")
            print_slow("\033[0;37;40mPlease pick from either 1 or 2.")
            print("\n\n")
            choices()
    choices()
    print("\n\n")
    print_slow("\033[1;33;40mLAWYER: Anyway, what kind of approach do you want to take for your opening statement?")
    print("\n\n")
    def defence_strategy():
        print_slow("\033[0;37;40mYou are presented with three options: ")
        print("\n\n")
        print_slow("\033[0;37;40m1. Aggressive\n")
        print_slow("\033[0;37;40m2. Sympathetic\n")
        print_slow("\033[0;37;40m3. Let him decide\n")
        print("\n\n")
        def choice1():
            print_slow("\033[0;37;40mYOU: Show them who's boss!")
            print("\n\n")
            print_slow("\033[1;33;40mLAWYER: Gotcha buddy! Don't worry, I'm a pro!")
            print("\n\n")
            print_slow("\033[0;37;40mThe LAWYER skips over towards the jury.")
            print("\n\n")
            print_slow("\n\033[1;33;40mLAWYER: Joey was beloved by all. My client was a good friend of his. To even dare think they are involved in Joey’s kidnapping is an insult!")
            print_slow("\n\033[0;37;40mThe LAWYER raises his arms in a dramatic effect.")
            print_slow("\n\033[1;33;40mLAWYER: Do you know who this is? They are a war hero! A Nobel prize winner at the age of 9 and an Academy award at 10! This trial is nonsense and should be acquitted immediately.")
            print_slow("\n\n\033[0;37;40mHe turns to you and winks at you with confidence.\n")
            print("                                                                           ")
            print_slow("\033[0;37;40mThe jury think he is absolutely insane.\n")
        def choice2():
            print("\n")
            print_slow("\033[0;37;40mKeep on crying.")
            print("\n\n")
            print_slow("\033[1;33;40mLAWYER: Gotcha buddy! Don't worry, I'm a pro!")
            print("\n\n")
            print_slow("\033[0;37;40mThe LAWYER skips over towards the jury.")
            print("\n\n")
            print_slow(f"\033[1;33;40mLAWYER: Joey was the best of us. His bounce was that of legend. We all loved him, especially my client, {name}.")
            print("\n")
            print_slow(f"The prosecution is trying to make them a scapegoat. We must acquit {name} so that we can find the true kidnapper!")
            print("\n\n")
            print_slow("\033[0;37;40mThe jury is all leaning in, completely captivated by your defences eloquent words.")
            print("\n")
        def choice3():
            print("\n\n")
            print_slow("\033[0;37;40mYOU: Good luck.")
            print("\n\n")
            print_slow("\033[1;33;40mLAWYER: Gotcha buddy! Don't worry, I'm a pro!")
            print("\n\n")
            print_slow("\033[0;37;40mThe LAWYER skips over towards the jury.")
            print("\n\n")
            print_slow("\033[1;33;40mLAWYER: What animal jumps when it walks and sits when it stands?")
            print("\n\n")
            print_slow("\033[0;37;40mThe court is silent.")
            print("\n\n")
            print_slow("\033[0;37;40mYOU:Kanga-")
            print("\n\n")
            print_slow("\033[1;33;40mLAWYER: That’s right! A Kangaroo!")
            print("\n\n")
            print_slow("\033[0;37;40mHe bakes in the non-existent laughter.")
            print("\n\n")
            print_slow("\033[1;33;40mLAWYER: Now that we are all having a good time. My client didn’t do it.")
            print("\n\n")
            print_slow("\033[0;37;40mThe jury is thoroughly confused but doesn’t seem to be swayed either way.")
            print("\n\n")
        choice = input()
        if choice == "1":
            lose_karma()
            choice1()
        elif choice == "2":
            gain_karma()
            choice2()
        elif choice == "3":
            choice3()
        else:
            print("\n")
            print("\033[0;37;40mPlease pick 1, 2 or 3.")
            print("\n")
            defence_strategy()
    defence_strategy()
    print_slow("\033[0;37;40mThe LAWYER returns to his seat with his thumbs up and a smirk.")
    print("\n")
    print_slow("\033[0;37;40mWith a loud cough, the PROSECUTOR stands up.")
    print("\n\n")
    print_slow(f"\033[1;31;40mPROSECUTOR: Your honour, the prosecution requests to call {name} to the stand.")
    print("\n\n")
    print_slow("\033[0;37;40mThe JUDGE nods firmly.")
    print("\n\n")
    def approach_stand():
        print("\033[0;37;40mDo you approach the stand?(Yes/No)")
        print("\n\n")
        yes = ["Y", "y", "yes","Yes","YES"]
        no = ["N", "n", "no","No","NO"]
        answer=input()
        # answer= answer.lower()
        # if answer == "y" or answer == "yes":
        if answer in yes:
            print("\n")
            print_slow("\033[0;37;40mRising out of your seat, you waddle to the witness stand, feeling as if you have forgotten how to walk.")
            print("\n")
        elif answer in no:
            lose_karma()
            print("\n")
            print_slow("\033[0;37;40mYou remain seated.")
            print("\n\n")
            print_slow(f"\033[1;32;40mJUDGE: BAILIFF, could you please help {name} out of their seat?")
            print("\n\n")
            print_slow("\033[0;37;40mDrawing their baton, the BAILIFF storms over to you.")
            print("\n\n")
            print_slow("\033[1;34;40mBAILIFF: The honourable JUDGE SCOFFMAN called you to the stand.")
            print("\n\n")
            print("\033[0;37;40m")
            def witness_stand():
                print_slow(list_serial(list_witness_stand))
                choice = input()
                print("                                                                                   \n")
                if choice == "1":
                    print("\n")
                    print_slow("Rising out of your seat you waddle to the seat next to the JUDGE, feeling as if you have forgotten how to walk.")
                    print("\n")
                    print_slow("The Jury stare as you walk past.")
                    print("\n")
                elif choice == "2":
                    print_slow("With a whack, you are smacked with the baton.")
                    print("\n")
                    print_slow("Everything goes black…")
                    print("\n")
                    print_slow("You wake up to find yourself tied up. ")
                    print("\n")
                    print_slow("Rolling on your side you see that you’re on a rail track. You can feel them vibrating.\n\nIn the not-so-far distance,") 
                    print_slow("there are huge puffs of steam.\n\nYou think to yourself “I should have just gotten up”\n\nYou are dead.")
                    def final_straw():
                        print("\n\n")
                        print_slow("Do you want to retry?(Yes/No)")
                        print("\n\n")
                        retry=input()
                        print("\n\n")
                        if retry in yes:
                            approach_stand()
                        elif retry in no:
                            end()
                        else:
                            print("\n\n")
                            print("\033[0;37;40mPlease say yes or no.")
                            final_straw()
                    final_straw()
                else:
                    print("\033[0;37;40mPlease pick from either 1 or 2.")
                    print("\n\n")
                    witness_stand()
            witness_stand()
            
        else:
            print("\n")
            print_slow("\033[1;32;40mJUDGE: They are speaking in tongues! Restrain the defendant.")
            print("\n\n")
            print_slow("\033[1;34;40mBALLIF: I ask you again, approach the stand!")
            print("\n\n")
            approach_stand()
        
            
    approach_stand()



opening_statements()
print_slow("The prosecutor stands, still staring at her notes.")
print("\n")
print_slow("Relaxing her shoulders she decides she's ready.")
print("\n")
print_slow("Striding to the stand she stares into your eyes.")
print("\n")
print_slow("It’s impossible to escape her gaze.")
def no_questions():
    print("\n\n")
    print_slow("\033[1;31;40mPROSECUTOR: No further questions your honour.")
    print("\n\n")
    print_slow("\033[0;37;40mThe PROSECUTOR returns to her seat, very pleased with herself.")

#Q1
def witness_stand():
    def question1():
        # \033[0;37;40m white
        # \033[1;31;40m red
        global karma
        print("\n\n")
        print_slow(f"\033[1;31;40mPROSECUTOR: When was the last time you saw Joey the Kangaroo, {name}? ")
        print("\n\n")
        print("\033[0;37;40m")
        # time.sleep(1)
        print_slow(list_serial(list_question1))
        anwser1 = input()
        if anwser1 == "1":
            print("\n")
            print_slow("\033[0;37;40mThe PROSECUTOR looks at you smugly. She whips out a picture and smacks it on the stand.")
            print("\n\n")
            print_slow ("\033[1;31;40mPROSECUTOR: I find it hard to believe as we have photo evidence of you two meeting two weeks ago! ")
            print("\n\n")
            print_slow("\033[0;37;40mWith a gasp the jury stare at you in shock.")
            lose_karma()   
        elif anwser1 == "2":
            print("\n\n")
            print("\033[1;31;40mPROSECUTOR: Second question...")
            print("\n\n")
            print_slow("\033[0;37;40mThe PROSECUTOR looks at you smugly.")
            print("\n\n")
            print_slow ("\033[1;31;40mPROSECUTOR: We have the transcripts from you couples counselling sessions! ")
            print("\n\n")
            print_slow("\033[0;37;40mThe jury gasps! ")
            print("\n\n")
            print_slow ("\033[1;31;40mPROSECUTOR: If they are willing to lie about when was the last time they saw them, maybe they are lying about something else…like Kidnapping? ")
            print("\n\n")
            print_slow("\033[0;37;40mThe jury seems hesitant to trust you.")
            lose_karma()
        elif anwser1 == "3":
            print("\n\n")
            print_slow ("\033[1;31;40mPROSECUTOR: Hmm… interesting. That does check out..")
            print("\n\n")
            print_slow("\033[0;37;40mThe jury looks at you sympathetically.")
            gain_karma()
        elif anwser1 == "4":
            print("\n\n")
            print_slow("\033[0;37;40mThe PROSECUTOR looks at you smugly. She whips out a picture and smacks it on the stand.")
            print("\n\n")
            print_slow ("\033[1;31;40mPROSECUTOR: I find it hard to believe as we have photo evidence of you two meeting two weeks ago! ")
            print("\n\n")
            print_slow("\033[0;37;40mWith a gasp the jury stare at you in shock.")
            lose_karma()
        else:
            print("\n\n")
            print_slow("\033[1;32;40mJUDGE: Please answer the question.")
            question1()
        
    question1()
    print("\n\n")
    print_slow("\033[1;32;40mJUDGE: Next question please. ")   
    # Q2
    def question2():
        global karma
        print("\n\n") 
        print_slow("\033[1;31;40mPROSECUTOR: Second question...")
        print("\n")
        print_slow(f"\033[1;31;40mWhere were you, {name}, at the time he went missing?")
        print("\n\n")
        print("\033[0;37;40m")
    # time.sleep(1)
        print_slow(list_serial(list_question2))
        anwser2= input()
        if anwser2 == "1" :
            print("\n\n")
            print_slow ("\033[1;31;40mPROSECUTOR: We have your browsing history, there's no record of that!")
            print("\n\n")
            print_slow("\033[0;37;40mWith a gasp the jury stare at you in shock.")
            lose_karma()  
        elif anwser2 == "2":
            print("\n\n")
            print_slow ("\033[1;31;40mPROSECUTOR: And there’s no one who can confirm that you did! Very suspicious! ")
            print("\n\n")
            print_slow("\033[0;37;40mThe jury look at you undecided.\n")
        elif anwser2 == "3":
            print("\n\n")
            print_slow ("\033[1;31;40mPROSECUTOR: You seem to have your story straight. That does check out with the timeline. ")
            print("\n\n")
            print_slow("\033[0;37;40mThe jury looks at you sympathetically.")
            gain_karma()
        else:
            print("\n\n")
            print_slow("\033[1;32;40mJUDGE: Please answer the question.")
            question2()
    
    
    question2()
    #Q3
    def question3():
        global karma
        print("\n\n")
        print_slow("\033[1;31;40mCould you please describe the dynamic of your relationship with the kangaroo? ")
        print("\n\n")
        print("\033[0;37;40m")
        print_slow(list_serial(list_question3))
        answer3 = input()
        if answer3 == "1":
            print("\n\n")
            print_slow ("\033[1;31;40mPROSECUTOR: That might be the case, but we know that your relationship was romantic in nature.")
            print("\n\n")
            print_slow("\033[0;37;40mThe PROSECUTOR slams down polaroids of you and Joey on holiday in Hawaii. ")
            print("\n\n")
            print_slow("\033[0;37;40mWith a gasp the jury stare at you in shock.")
            lose_karma()
        elif answer3 == "2":
            print("\n\n")
            print_slow ("\033[1;31;40mPROSECUTOR: Darn. Thought you were gonna incriminate yourself.")
            print("\n\n")
            print_slow("\033[0;37;40mThe jury looks at you sympathetically.")
            gain_karma()
        elif answer3 == "3":
            print("\n\n")
            print_slow ("\033[1;31;40mPROSECUTOR: That’s a lie! We have a locket with your face on it! ")
            print("\n\n")
            print_slow("\033[0;37;40mWIth a gasp the jury stare at you in shock.")
            lose_karma()
        else:
            print("\n\n")
            print_slow("\033[1;34;40mBAILIFF: Respect the Judge! Answer the question!!!")
            question3()



    question3()
    #Q4
    def question4():
        global karma
        print("\n\n")
        print("\033[1;31;40mPROSECUTOR: Final question!")
        print("\n")
        print_slow("\033[1;31;40mWere you on good terms with the Kangaroo? ")
        print("\n\n")
        print("\033[0;37;40m")
        print_slow(list_serial(list_question4))
        answer4 = input()
        if answer4 == "1":
            print("\n\n")
            print_slow ("\033[1;31;40mPROSECUTOR: Hmm… interesting. That does annoyingly check out.")
            print("\n\n")
            print_slow("\033[0;37;40mThe PROSECTUOR coughs awkwardly, a little embarrassed. The jury looks at you sympathetically.")
            gain_karma()
        elif answer4 == "2":
            print("\n\n")
            print_slow ("\033[1;31;40mPROSECUTOR: If that is true, then perhaps you kidnapped him to stop him?")
            print("\n\n")
            print_slow("\033[0;37;40mWIth a gasp the jury stare at you in shock.")
            lose_karma()
        elif answer4 == "3":
            print("\n\n")
            print_slow ("\033[1;31;40mPROSECUTOR: We will not take defamation and slander of our beautiful boy, Joey!")
            print("\n\n")
            print_slow("\033[0;37;40mThe jury looks at you with disgust.")
            lose_karma()
        elif answer4 == "4":
            print("\n\n")
            print("""░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░
▄▀▀▀▄░█░░░░█░▄▄▄░░░░▄█▄░█░░░░░░░░░█
█░░░█░█▄▄▄░▄░█▄█░▄▀▀░█░░▄░░▄░░░░░░█
█░░░█░█░░█░█░█░░░█░░░█░░█░█░█░█▄▄░█
█░░░█░█▄▄█░█░█▄░░▀▄▄░█░░█░▀▄▀░█░█░█
▀█▄█▀░░░░▄▄█░░░░░░░░░░░░░░░░░░▀░█░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░▄▄▄▄░░░░░░░░░░░░░░░░░░░░░░░░░
░░▀██████▀▀▀░░░░░░░░░░░░░░░░░░▄▄▄▄▄
░░░░▀██░░░▀░░░░░░░░░░░░░▄▄▀▀▀▀░▄▄▄▀
░░░░░░░░░▄▄░░░░░░░░░░▄▄██▀░░▀░█░░░░
░░░░░░░░▄▄▄▄██▄▄▄▄███████▄▄▀▀▀░░░░░
░▄▄███░▄████████████████▀▀▀░░░░░░░░
█████▄██████████████▀▀░░░░░░░░░░░░░
████████████████▀░░░░░░░░░░░░░░░░░░
██████████████▀░░░░░░░░░░░░░░░░░░░░
██████████████░░░░░░░░░░░░░░░░░░░░░""")
            print("\n\n")
            print_slow("\033[1;32;40mJUDGE: Please answer the question.")
            question4()
        else:
            print("\n\n")
            print_slow("\033[1;34;40mBAILIFF: Give some respect for the Judge! Answer the question!!!")

            question4()
        
        
    question4()
    no_questions()
witness_stand()
def closing_statement():
    def defendant_plead():
        global karma
        print_slow("\033[0;37;40m You return to your seat. The court is silent - waiting excitedly for the JUDGE.")
        print("\n\n")
        print_slow("\033[1;32;40mJUDGE: Before the jury decides, how does the defendant plead?  ")
        print("\033[0;37;40m")
        print("\033[0;37;40m")
        print_slow(list_serial(list_defendant_plead))
        choice = input()
        choice = choice.lower()
        if choice == "1":
            gain_karma()
        elif choice == "2":
            print_slow("")
        elif choice == "3":
            lose_karma()
            print_slow("\033[0;37;40mYou stand up enraged\n\n THIS IS A KANGAROO COURT!")
        else:
            print("\n\n")
            print_slow("\033[1;34;40mBAILLIFF: Respect the judge you WEASEL!!! ")
            defendant_plead()
    defendant_plead()
closing_statement()


#verdict

def countdown():
    global num
    global space
    global space2
    while num > 1:
            num-=1
            time.sleep(1) 
            if num == 3:
                print(f"\033[1;34;40m")
            elif num == 2:        
                print(f"\033[1;32;40m")
            elif num == 1:
                print(f"\033[1;31;40m")
            print(f"{space} -----------------")
            print(f"{space}|{space2}{space2} |")
            print(f"{space}|{space2}{num}{space2}| ")
            print(f"{space}| {space2}{space2}|")
            print(f"{space} _________________ ")
    time.sleep(1)

def before_verdict():
    print("\n\n")
    print_slow("\033[1;32;40mJUDGE: It is time for the Jury to decide.")
    print("\n")
    print_slow("\n\033[0;37;40mYou can hear the haste whispers of the jury conversing. Suddenly, it ceases.")
    print("\n\n")
    print_slow("\033[1;36;40mJURY: We have come to a decision.")
    print("\n\n")
    print_slow("\033[1;32;40mJUDGE: What have you decided?")
    print("\n\n")
    print_slow("\033[1;36;40mJURY: We have decided....")
    countdown()
def arrested():

    print("\033[1;31;40m                                                                                                                                ")
    print("                                                                                                                                 ")
    print("                      ##        ##                                                                                                     ")
    print("                       ##     ##                       ##                                                                              ")
    print("                        ##  ##     #####    ##    ##  ## ##  ###   ######                                                              ")
    print("                          ##    ##     ##  ##    ##  ## ## ##    ##     ##                                                             ")
    print("                         ##    ##     ##  ##    ##     ##       ########                                                               ")
    print("                        ##    ##     ##  ##    ##     ##       ##                                                                      ")
    print("                       ##      #####     ######      ##        #######                                                                 ")
    print("                                                                                                                                 ")
    print("                                             ##   ##    ##                                                                             ")
    print("                                                 ##    #####                                                                           ")
    print("                        #####     ##    ##  ##  ##    ##    ##    ##                                                                   ")
    print("                     ##      ##  ##    ##  ##  ##    ##    ##    ##                                                                    ")
    print("                    ##      ##  ##    ##  ##  ##    ##    ##    ##                                                                     ")
    print("                   ##      ##  ##    ##  ##  ##    ##    ##    ##                                                                      ")
    print("                    #######    #####    ##   ####  #####  #####                                                                        ")
    print("                        ##                                 ##                                                                          ")
    print("                       ##                                 ##                                                                           ")
    print("                   ####                               ####                                                                             ")
    print("                                                                                                                                       ")
def freedom():
    print("\033[1;32;40m                                                                                                                                                    ")
    print("                                                                                                                                                                 ")
    print("                          ##        ##                                                                                                                           ")
    print("                           ##     ##                       ##                                                                                                    ")
    print("                            ##  ##     #####    ##    ##  ## ##  ###    ######                                                                                   ")
    print("                              ##    ##     ##  ##    ##  ## ## ##    ##     ##                                                                                   ")
    print("                             ##    ##     ##  ##    ##     ##       ########                                                                                     ")
    print("                            ##    ##     ##  ##    ##     ##       ##                                                                                            ")
    print("                           ##      #####     ######      ##        ######                                                                                        ")
    print("                                                                                                                                                                 ")
    print("                                 ##                                       ##  ##    ##                                                                           ")
    print("                                ####                                         ##    ####                                                                          ")
    print("          ##  ####    #####    ##                   ######    ##    ##  ##  ##    ##    ##    ##                                                                 ")
    print("         ##     ##  ##    ##  ##                 ##      ##  ##    ##  ##  ##    ##    ##    ##                                                                  ")
    print("        ##     ##  ##    ##  ##                 ##      ##  ##    ##  ##  ##    ##    ##    ##                                                                   ")
    print("       ##     ##  ##    ##  ##                 ##      ##  ##    ##  ##  ##    ##    ##    ##                                                                    ")
    print("      ##     ##    #####    ####                #######    #####    ##   ####  #####  #####                                                                      ")
    print("                                                    ##                                 ##                                                                        ")
    print("                                                   ##                                 ##                                                                         ")
    print("                                               ####                               ####                                                                           ")
    print("                                                                                                                                                                 ")
def guilty():
    global name
    arrested()
    print_slow(f"\033[1;36;40mJURY: We find {name}... ")
    print("\n")
    print_slow("Guilty! ")
    print("\n\n")
    print_slow("\033[0;37;40mA boom of cheers echos the courtroom from the loud spectators.")
    print("\n\n")
    print_slow("\033[1;32;40mJUDGE: Excellent! ")
    print("\n\n")
    print_slow("\033[0;37;40mThe JUDGE rubs his hands excitingly. ")
    print("\n\n")
    print_slow("\033[1;32;40mJUDGE: I sentence you to being imprisoned within the zoo for life!  ")
    print("\n\n")
    print_slow("\033[0;37;40mThe crowd are loving this.")
    print("\n\n")
    print_slow("\033[1;32;40mJUDGE: You’ll wear an costume and be our new kangaroo!  ")
    print("\n\n")
    print_slow("\033[0;37;40mOh no. What have you done?\n")
    print("\n\n")
    print_slow("You live your days out in a stuffy kangaroo suit with children laughing and pointing at you inside of your enclosure all day,")
    print("\n") 
    print_slow("every day.")
    
def not_guilty():
    global name
    freedom()
    print("\n\n")
    print_slow(f"\033[1;36;40mJURY: We find {name}...not guilty!")
    print("\n\n")
    print_slow("\033[0;37;40mAbruptly, you hear loud booing of the the court towards the jury.")
    print("\n\n")
    print_slow("\033[1;32;40mJUDGE: You sure? ")
    print("\n\n")
    print_slow("\033[1;36;40mJURY: We are.")
    print("\n\n")
    print_slow(f"\033[1;32;40mJUDGE:  Well then, {name} you are free to go! I hope we never see you in San Deigo every again!")
    print("\n\n")
    print_slow("\033[0;37;40mYou are free! The BAILIFF helps escort you out of the the court, protecting you from the outraged spectators. ")
    print("\n")
    print_slow("You return home with an evil smile on your face.")
    print("\n")
    print_slow("In your living room all tied up...") 
    print("\n"*5)
    print_slow("...is JOEY!?")

def really_guilty():
    global name
    arrested()
    print("\n\n")
    print_slow(f"\033[1;36;40mJURY: We find {name}... Guilty! On all accounts!")
    print("\n\n")
    print_slow("\033[0;37;40mThe court screams with joy! Chanting “Death” over and over.")
    print("\n\n")
    print_slow("\033[1;32;40mJUDGE: Marvelous!! ")
    print("\n\n")
    print_slow("\033[0;37;40mThe JUDGE rubs his hands excitingly with an evil grin.")
    print("\n\n")
    print_slow("\033[1;32;40mJUDGE: I sentence you to death by… ")
    print("\n\n")
    print_slow("\033[0;37;40mThe JUDGE strokes his chin thinking hard")
    print("\n\n")
    print_slow("\033[1;32;40mJUDGE: Being covered in gravy and then dropped into the lion enclosure")
    print("\n\n")
    print_slow("\033[0;37;40mThe crowd are loving this.")
    print("\n\n")
    print_slow("\033[1;32;40mJUDGE: She is awfully hungry!")
    print("\n\n")
    print_slow("\033[0;37;40mThe BALLIFF handcuffs and escorts you out through the cheering crowd")
    print("\n\n")
    print_slow("You are then smothered in gravy and then thrown to the Lion. She was indeed awfully hungry.")
    time.sleep(2) 
    print("\n" * 30)
    print_slow("The End?")
    time.sleep(4)
    print_slow("...")
    print("\n" * 20)
    print_slow("\033[0;37;40mThe court is empty. Except for one person. Still sitting in his chair. The JUDGE is smiling menancingly. ")
    print("\n\n")
    print_slow("\033[1;32;40mJUDGE: Everything went as planned!")
    print("\n\n")
    print_slow("\033[0;37;40mSuddenly he pulls his face off. It’s a mask! To reveal: \n\n… \n\nA kangaroo!")
    print("\n")
    print("\n")
    print_slow("\033[1;32;40mJOEY: I am now free, muhahaha!")
    print("\n")
    print("\n")

def final_karma():
    global karma
    if karma >= 10:
        not_guilty()
    elif karma  <10 and karma >=0:
        guilty()
    else:
        really_guilty()
        
before_verdict()
final_karma()
end()

# if karma > 10: this part is to change depend on how many point it take to be innocent
