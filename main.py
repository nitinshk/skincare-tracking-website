
from time import sleep 
from flask import Flask
app = Flask(__name__)
@app.route("/")


def welcome_statement():

    """Displays print welcome statements for user"""

    print("\n**************** Welcome To SkinReg ****************") 
    sleep(1)
    print("\nSkin is the largest organ of the human body...")
    sleep(4)
    print("\nAs we age, it is essential to keep our skin healthy and youthful.")
    sleep(4)
    print("\nHaving a step by step skincare routine is a great way to start.")
    sleep(4)
    print("\nLets create your personalized skincare regimen.")
    sleep(2)
#welcome_statement()


def ask_for_name():

    """Asks user for name to start the game"""

    name = input("\nWhat is your name? > ")
    name = name.title()
    sleep(2)
    print(f"\nHello {name}, you're on the right path to better skin health!")
    sleep(2)
#ask_for_name()


def skin_type_statement():

    """Asks user to select their skin texture type"""
    print("\nNow, we need to learn more about your skin texture and type...")
    sleep(4)
    print("\nSelect one of the following that best describes your skin:")
    sleep(2)
    print("[A] Normal \n[B] Oily \n[C] Dry \n[D] Sensitive \n[E] Combination")
#skin_type_statement()


def skin_type():
    """Asks user to type a specific letter"""
    sleep(1)
    type_of_skin = input("(Pick A, B, C, D, or E) > ")
    type_of_skin = type_of_skin.lower()
 
    if type_of_skin == "a":
        skin1 = "normal"
        sleep(2)
        print(f"\nGreat, we have your skin type as {skin1}")
        
    elif type_of_skin == "b":
        skin2 = "oily"
        sleep(2)
        print(f"\nGreat, we have your skin type as {skin2}") 

    elif type_of_skin == "c":
        skin3 = "dry" 
        sleep(2)
        print(f"\nGreat, we have your skin type as {skin3}")  

    elif type_of_skin == "d":
        skin4 = "sensitive"
        sleep(2)
        print(f"\nGreat, we have your skin type as {skin4}")

    elif type_of_skin == "e":
        skin5 = "combination"
        sleep(2)
        print(f"\nGreat, we have your skin type as {skin5}")  
    
    else:
        print("\n**Please type A, B, C, D or E only**")
        sleep(1)
        skin_type()
#skin_type()


def continue_reg():

    """Asks user if they want to continue playing"""
    sleep(3)
    print("\nNext, we'll list the appropiate way to layer your skincare products.")
    sleep(3)
    continue_game = input("\nWould you like to continue to the first step of the routine? (Type Y or N)> ")
    sleep(3)
    continue_game = continue_game.upper()
    if continue_game == "Y":
        print("\nAwesome! Let's start with Step 1: The Cleanser")
        sleep(2)
    elif continue_game == "N":
        print("\nNo worries! We'll be here once you're ready to start your healthy skincare regimen :) ")
        sleep(2)
    else:
        print("\n**Please type Y (for Yes) or N (for No)**")
        sleep(1)
        continue_reg()
#continue_reg()


def day_or_night():

    """Asks user for input on time of day"""
    sleep(2)
    time_of_day = input("\nIs it Daytime or Nighttime? > ")
    time_of_day = time_of_day.lower()
    sleep(2)
    if time_of_day == "daytime" or time_of_day == "day time":
        print("\nRise and shine...Early bird gets the worm!")
        sleep(2)
    elif time_of_day == "nighttime" or time_of_day == "night time":
        print("\nWhat a day! It's time to unwind for bed.")
        sleep(2)
    else:
        print("\n**Please type Daytime or Nighttime only**")
        sleep(1)
        day_or_night()
#day_or_night()


def first_step_cleanser():

    """Displays first step of the skin care regimen"""
    
    print("\nRight after you've washed your hands and set your water to a lukewarm temperature, we're on to our first step.")
    sleep(6)
    print("\nAlways remember how important it is to use the proper cleaning technique for your skin.")
    sleep(6)
    print("\nSelect the cleanser that best fits your skin type:")
    sleep(2)
    print("[A] Normal Cleanser - Normal \n[B] Oily Cleanser - Foaming \n[C] Dry Cleanser - Hydrating \n[D] Sensitive Cleanser - Hypoallergenic \n[E] Combination Cleanser - Balancing")
#first_step_cleanser()


def cleanser_choice():

    """Asks user to select cleanser based on skin type"""
    sleep(2)
    select_cleanser = input("(Pick A, B, C, D, or E) > ")
    select_cleanser = select_cleanser.lower()
    sleep(3)
    if select_cleanser == "a":
        print("\nNormal cleanser it is! Squeeze a dime size amount, lather on face for 60 secs, rinse off product with warm water, and pat dry face with a clean towel.")
        sleep(4)
    elif select_cleanser == "b":
        print("\nFoaming cleanser it is! Squeeze a dime size amount, lather on face for 60 secs, rinse off product with warm water, and pat dry face with a clean towel.")
        sleep(4)
    elif select_cleanser == "c":
        print("\nHydrating cleanser it is! Squeeze a dime size amount, lather on face for 60 secs, rinse off product with warm water, and pat dry face with a clean towel.")
        sleep(4)
    elif select_cleanser == "d":
        print("\nSensitive cleanser it is! Squeeze a dime size amount, lather on face for 60 secs, rinse off product with warm water, and pat dry face with a clean towel.")
        sleep(4)
    elif select_cleanser == "b":
        print("\nBalancing cleanser it is! Squeeze a dime size amount, lather on face for 60 secs, rinse off product with warm water, and pat dry face with a clean towel.")
        sleep(4)
    else:
        print("** Please type A, B, C, D or E only **")
        sleep(1)
        cleanser_choice()
#cleanser_choice()


def add_cleanser_to_list():

    """Asks user if they want to add cleanser to list""" 
    sleep(4)
    print("\nWoohoo! your skin is so happy, clean, and ready for the next step")
    sleep(4)
    print("\nBefore we move on...would you like to add the cleanser to your personalized SkinReg list? (Type Y or N)")
    add_cleanser = input("> ")
    add_cleanser = add_cleanser.lower()
    sleep(3)

    if add_cleanser == "y":
        skin_care_steps = []
        skin_care_steps.append("The Cleanser")
        for step in skin_care_steps:
            print(f"Here's your personal regimen, so far: {step}")
        sleep(4)
    elif add_cleanser == "n":
        print("\nNo problem! We'll hold onto your cleanser until you're ready") 
        sleep(2)
    print("\nNow it's time to move onto Step 2: The Toner")
    sleep(3)
#add_cleanser_to_list()


def second_step_toner():

    """Displays statements about toner benefits"""
    sleep(2)
    print("\nAfter you've cleansed your skin, it's important to restore your ph balance, with an alcohol free toner")
    sleep(5)
    print("\nA toner is used to complete the cleansing of the skin, effectively removing impurities that remain after washing your face")
    sleep(5)
    print("\nBased on your skin type, select the toner that best fits:")
    sleep(2)
    print("[A] Normal Skin Toner - Hyaluronic Acid \n[B] Oily Skin Toner  - Witch Hazel \n[C] Dry Skin Toner - Glycerin \n[D] Sensitive Skin Toner - Aloe Vera \n[E] Combination Skin Toner - Lactic Acid")
#second_step_toner()   


def toner_choice():

    """Asks user to select a toner based on skin type"""
    sleep(1)
    select_toner = input("(Pick A, B, C, D, or E) > ")
    select_toner = select_toner.lower()
    sleep(4)
    if select_toner == "a":
        print("\nNice, a toner with hyaluronic acid! This will replenish moisture, giving your skin a hydrated, softer look, and feel. \nGrab a cotton pad, saturate it with your toner, then gently apply to your face.")
        sleep(4)

    elif select_toner == "b":
        print("\nNice, a toner containing witch hazel! This will control shine and purify the skin, which is cruical for congested pores.\nGrab a cotton pad, saturate it with your toner, then gently apply to your face.")
        sleep(4)

    elif select_toner == "c":
        print("\nNice, a toner containing glycerin! When you have dry skin...stay away from toners that contain alcohol in them, as it dries you out. .\nGrab a cotton pad, saturate it with your toner, then gently apply to your face.")
        sleep(4)

    elif select_toner == "d":
        print("\nNice, a toner containing aloe vera! This will work to detoxify and remove impurites that can irritate the skin.\nGrab a cotton pad, saturate it with your toner, then gently apply to your face.")
        sleep(4)

    elif select_toner == "e":
        print("\nNice, a toner containing lactic acid! This hydrates dry skin, but does so gently which works for sensative skin also.\nGrab a cotton pad, saturate it with your toner, then gently apply to your face.")
        sleep(4)

    else:
        print("** Please type A, B, C, D or E only **")
        sleep(1)
#toner_choice()


def add_toner_to_list():

    """Asks user if they want to add toner to list""" 
    sleep(6)
    print("\nSoooo refreshing! I bet your skin feels like you just left the spa.")
    sleep(4)
    print("\nBefore we move on...would you like to add the toner to your personalized SkinReg list? (Type Y or N)")
    add_toner = input("> ")
    add_toner = add_toner.lower()
    sleep(3)

    if add_toner == "y":
        skin_care_steps = []
        skin_care_steps.append("The Cleanser")
        skin_care_steps.append("The Toner")
        sleep(2)
        print("Here's your personal regimen, so far:")
        for step in skin_care_steps:
            print(step)
        sleep(2)

    elif add_toner == "n":
        sleep(2)
        print("\nNo problem! We'll hold onto your toner until you're ready") 
    sleep(2)
    print("\nNow it's time to move onto Step 3: The Serum")
    sleep(2)
#add_toner_to_list()


def keep_playing():

    """Ask user if they want to keep playing"""
    sleep(2)
    print("\nIn order to move forward...you have to purchase the app.")
    sleep(3)
    keep_playing = input("\nWould you like to know the next important step in your skin care routine? (Type Y or N) > ")
    keep_playing = keep_playing.upper()
    sleep(2)
 #how to start this part over if user enters wrong letter?
    if keep_playing == "Y":
        sleep(2)
        print("\nThat's the spirit...You'll now be taking to our payment station to continue your regimen")
    elif keep_playing == "N":
        sleep(2)
        print("\nThank you for stopping by! We'll be here once you're ready to finalize your healthy SkinReg routine :) ")
    else:
        sleep(1)
        print("**Please type Y (for Yes) or N (for No)**")
        keep_playing()
#keep_playing()


def run_skin_reg():

    """Runs the entire skin care routine game"""

    welcome_statement()
    ask_for_name()
    skin_type_statement()
    skin_type()
    continue_reg()
    day_or_night()
    first_step_cleanser()
    cleanser_choice()
    add_cleanser_to_list()
    second_step_toner()
    toner_choice()
    add_toner_to_list()
    keep_playing()

if __name__=='__main__':
 app.run(debug = True)



