#-1
#000
#1111
#22222
#333333
#_._______________________________________________________________________
#                               Random/ tweaks
import random

mega_points = [0]
def ui_tweak(ui_element):
    if ui_element == "MegaPoints999": #adjust the ui to fit up to 999, len(23)
        if mega_points[0] < 10:
            return "Total Mega Points! :" + "00" + str(mega_points[0])
        if mega_points[0] < 100:
            return  "Total Mega Points! :" + "0" + str(mega_points[0])
        if mega_points[0] > 999:
            return "Total Mega Points! :" + "999"
        return "Total Mega Points! :" +  str(mega_points[0])

def random_ui_words(style):
    greeings = ["Hello sunshine!", "Howdy partner!", "What's kickin' little chicken?", "Ahoy matey!", "Hiya!",
                "At least we meet for the first time for the last time!", "I like your face.", "Whats cookin good lookin'?",
                "Aloha", "Hola!", "Bonjour!", "Hallo!!", "Konnichiwa!", "I'm Batman!", "Here's Johnny!", "Ello govnuh!",
                "Top o the mornin to ya!", "GOOOOOD MORNING VIETNAM!", "Why hello there!", "Look who it is!",
                "Look what the cat dragged in!", "greets!", "what's cooking?", "what's cracking?", "yello!",
                "a-yo!", "G'day!", "Good to see you!", "Nice to see you!", "Long time no see!",
                "It's been a while!", "How have you been?", "G'day", "How do you do?", "G'day",
                "It's nice to meet you!", "Pleased to meet you!", "Good day!", "Yo!",
                "Are you OK?", "You alright?", "Alright mate?", "Howdy!","Sup?", "Whazzup?", "G'day mate!"]
    winner   = ["Groovy!","Righteous!", 'Nifty!', 'Copasetic!', 'Future Pulitzer Prize winner!', 'Future rock star!',
                'Future CEO!', 'You shine as brightly as the sun!', 'Success comes to those who work their ass off.', 'Felicitations',
                'Herzlichen Gluckwunsch', 'I am overjoyed with your success. Shine on!', "You've made us all so proud. I am very happy for you.",
                'Good work. Your hard work has truly paid off.', "You've got the right mix of dedication and enthusiasm. Keep it up!",
                'Congratulations for achieving so much on your own steam.', "It's the time for recognition! Well done my dear friend.",
                'Congratulations for making it big. You have earned all the praises you are now receiving.',
                'Congrats. Am in awe of you for the rest of my life', 'May this moment last forever. Congratulations.',
                'You are our shining star. Well done.', "Congratulations for scaling new heights and setting new standards.",
                "May this moment last forever. Congratulations.","There was never a doubt in our hearts that you were destined for success. Congratulations on your achievement!",
                "Many, many congratulations on your impressive performance, you have truly set a new record!",
                "Your will to push and never give up has brought you this far, you deserve this and more. Congratulations for a marvelous achievement!",
                "We are taught that the sky should always be the limit, but you have showed us that truly we should think beyond the sky.",
                "Some are destined to fit in, but you were born to stand out! You have made me proud","Congratulations on a brilliant victory!",
                "Life being a journey, Success has brought you many miles ahead of many people. Congratulations",
                "Cheers to never giving up! Enjoy the fruits of you labor and may you always succeed in whatever you do. Congratulations my friend!",
                "Dreams for success rarely materialize without dedication, perseverance, passion and hard work combined to make it a reality.",
                "Well done!", "Congratulations and thank you!", "It is inspirational to witness hard work finally give birth to success. Congratulations!",
                "you worked hard, you deserve it, you have got it! Please accept my congratulations on this wonderful recognition of your merits",
                "First they ignore you... Then they laugh and fight against you... Then you win!",
                "Congratulations for your fabulous victory! You deserve it every bit! Aim for the stars!",
                "Congratulations on your success! You have made us all proud. Keep up the good work!",
                "If Oscars were given for a job well done, I'd nominate you! Congratulations for your fantastic achievement!",
                "You, why you little, Champion!", "C-C-C-Combo", "Your hard work and effort have paid off! A success well deserved, an occasion worth celebrating! Congratulations!",
                "Your achievements speaks itself about your capabilities. Slow and steady makes it to the top! Good job!"]
    if style == "greetings":
        return random.choice(greeings)
    if style == "winner":
        return random.choice(winner)
#_._______________________________________________________________________
#                               Intro screen
game_intro = """
________________|_______________________|__________________
|-----------=>>>!! Welcome to the quiz !!<<<=-------------|
|-              -------------------------                -|
|-   -Please write out the difficulty  you can handle-   -|
|-              ___________________________              -|
|-             |  {}  |             -|
|-                                                       -|
|-   1. Easy:    {}      -|
|-   2. Medium:  {}      -|
|-   3. Hard:    {}    -|
|-   4. Insane:  {}    -|
|----------------------------|----------------------------|
|- >>>>>>>>>> Type in "Quit" or "q" to exit <<<<<<<<<<<< -|
|__________-=|=-_____________|___________-=|=-____________|
"""

#_._______________________________________________________________________
#                                 Easy quiz

key__1___e =            "1" #"kitten"
key__2__e =             "2" #"chick"
key__3__e =             "3" #"bunny"
key_chain_e =           [key__1___e, key__2__e, key__3__e]
quiz_questions_e  =     ["__1___", "__2__", "__3__"]

quiz_difficulty_e = """
_________________________________________________________________________________
|------------------------>}>? Animal Names: Young ?<)<---------------------------|
|-                         - If a dog has a puppy -                             -|
|-                          ----------------------                              -|
|-                            A cat has a __1___                                -|
|-                            A chicken a __2__                                 -|
|-                           A rabbit has a __3__                               -|
|--------------------------------------------------------------------------------|
|________________________________________________________________________________|
"""
#_._______________________________________________________________________
#                                 Easy bonus quiz
#For Ui keep key (__1__) the same length as answer. e.g. for improve: use __1____
#I use find (Ctrl + f) to change multiple items. Find "_e_bonus" and replace the name of the quiz
#1, 2 and 3 are placeholders to test.

key__1__e_bonus =             "1"#"Tom"
key__2__e_bonus =             "2"#"Doe"
key__3__e_bonus =             "3"#"Ewe"
key__4__e_bonus =             "4"#"Hen"
key__5__e_bonus =             "5"#"Mare"
key__6__e_bonus =             "6"#"Doe"
key__7__e_bonus =             "7"#"Bitch"
key__8__e_bonus =             "8"#"Vixen"
key__9__e_bonus =             "9"#"Bitch"
key_chain_e_bonus =           [key__1__e_bonus, key__2__e_bonus, key__3__e_bonus, key__4__e_bonus, key__5__e_bonus, key__6__e_bonus, key__7__e_bonus, key__8__e_bonus, key__9__e_bonus, ]
quiz_questions_e_bonus  =     ["_1_", "_2_", "_3_","_4_", "_5__", "_6_","__7__", "__8__", "__9__"]

quiz_difficulty_e_bonus = """
_________________________________________________________________________________
|----------------------->}>? Animal Names: Female  ?<)<--------------------------|
|-              - What are the female names 0f these animals? -                 -|
|-                          -----------------------                             -|
|-            Cat = _1_    ||   Chicken = _4_     ||   Dog = __7__              -|
|-           Deer = _2_    ||     Horse = _5__    ||   Fox = __8__              -|
|-          Sheep = _3_    ||    Rabbit = _6_     ||  Wolf = __9__              -|
|-                                                                              -|
|--------------------------------------------------------------------------------|
|                         > All names are capitalised <                          |
|________________________________________________________________________________|
"""
#_._______________________________________________________________________
#                                Medium quiz

key____1____m =         "1"#"important"
key_2_m =               "2"#"has"
key__3_m =              "3"#"stop"
key_4_m =               "4"#"new"
key_chain_m =           [key____1____m, key_2_m, key__3_m, key_4_m]
quiz_questions_m  =     ["____1____", "_2_", "__3_", "_4_"]

quiz_difficulty_m = """
_______________________________________________________________________________________________________
|------------------------------>]>? Know these Albert Einstein-Quotes ?<\<----------------------------|
|-                                                                                                   -|
|-                        "Imagination is more ____1____ than knowledge"                             -|
|-    "The ____1____ thing is not to __3_ questioning. Curiosity _2_ its own reason for existing."   -|
|-              "Anyone who _2_ never made a mistake _2_ never tried anything _4_."                  -|
|-                                                                                                   -|
|-----------------------------------------------------------------------------------------------------|
|                           >>>>>>>>> Please type non capitalised <<<<<<<<<                           |
|_____________________________________________________________________________________________________|
"""
#_._______________________________________________________________________
#                               Hard quiz

key__1_h =             "1" #"Yoda"
key__2_____h =         "2" #"Han Solo"
key__3__________h =    "3" #"Princess Leia"
key__4___________h =   "4" #"Obi Wan Kenobi"
key__5________h =      "5" #"Darth Vader"
key__6__h =            "6" #"R2-D2"
key_chain_h =           [key__1_h, key__2_____h, key__3__________h, key__4___________h, key__5________h, key__6__h]
quiz_questions_h  =     ["__1_", "__2_____", "__3__________", "__4___________", "__5________", "__6__"]

quiz_difficulty_h = """
_______________________________________________________________________________________________________
|----------------------------->!>? Know who said these Star Wars-Quotes ?<|<--------------------------|
|-                                                                                                   -|
|-                        "Do. Or do not. there is no try." - __1_                                   -|
|-                           "Great, kid. Don't get cocky." - __2_____                               -|
|-         "Aren't you a little short for a storm trooper?" - __3__________                          -|
|-          "These aren't the droids you're looking for..." - __4___________                         -|
|-                  "I find your lack of faith disturbing." - __5________                            -|
|-                                     "Bleep, Bleep Bloop" - __6__                                  -|
|-                                                                                                   -|
|-----------------------------------------------------------------------------------------------------|
|   >>>>>>>>> Please type names capitalised, e.g: "Jar Jar Binks"   NOT:  "jar jar binks" <<<<<<<<<   |
|_____________________________________________________________________________________________________|
"""
#_._______________________________________________________________________
#                                insane quiz

key_a_i =            "1" #"7"
key_b_i =            "2" #"9"
key_chain_i =           [key_a_i, key_b_i]
quiz_questions_i  =     ["_a_", "_b_"]

quiz_difficulty_i = """
_________________________________________________________________________________
|------------------------>>>? Complete the series ?<<<---------------------------|
|-                                                                              -|
|-                              9 = 4      21 = 9                               -|
|-                             22 = 9      24 = 10                              -|
|-                              8 = 5       7 = 5                               -|
|-                             99 = 10    100 = 7                               -|
|-                             16 = _a_?   17 = _b_?                            -|
|-                                                                              -|
|--------------------------------------------------------------------------------|
|________________________________________________________________________________|
"""
#_._______________________________________________________________________
#                             Global Var

difficulty_answers_list = ["   easy Easy 1", "    medium Medium 2", "    hard Hard 3",#The possible user input options available for each difficulty\/. i use the .find method to scan this list against the users input, allowing for more than one option when typing.
                            "     insane Insane 4","     q Q quit QUIT exit EXIT Quit "]
#def quiz_status(n): \/
quiz_compleate_status_e = [0]
quiz_compleate_status_m = [0]
quiz_compleate_status_h = [0]
quiz_compleate_status_i = [0]

#_._______________________________________________________________________
#                              Extra features

#would like a hint system
#yet to impliment method of resetting all states to new. #quiz_reset = [quiz_compleate_status_e[0], quiz_compleate_status_m[0],quiz_compleate_status_h[0], quiz_compleate_status_i[0]]
you_win = random_ui_words("winner") * mega_points[0]
difficulties_l = ["easy", "medium", "hard", "insane" ]
#_._______________________________________________________________________
#                      Quiz per difficulty. Functions:
def quiz_e():
    quiz_question = 0
    attempts = 0
    quiz_difficulty_e_proxy = quiz_difficulty_e
    input_holder = "e"
    print quiz_difficulty_e
    while quiz_question < len(quiz_questions_e):
        if attempts < 5:
            input_holder = raw_input("Please fill in " + quiz_questions_e[quiz_question] + " ")
            if input_holder == key_chain_e[quiz_question]:
                quiz_question += 1
                attempts = 0
                quiz_difficulty_e_proxy = quiz_difficulty_e_proxy.replace(quiz_questions_e[quiz_question-1],key_chain_e[quiz_question-1])
                print quiz_difficulty_e_proxy
                print random_ui_words("winner")
            else:
                attempts += 1
                print "Are you even human?.. You have",5 - attempts, "attempts left"
        if attempts >= 5:
            return "You lose"
    mega_points[0] += 5
    quiz_compleate_status_e[0] = 1
    return the_quiz()

def quiz_e_bonus():
    quiz_question = 0
    attempts = 0
    quiz_difficulty_e_bonus_proxy = quiz_difficulty_e_bonus
    input_holder = "new"
    print quiz_difficulty_e_bonus
    while quiz_question < len(quiz_questions_e_bonus):
        if attempts < 5:
            input_holder = raw_input("Please fill in " + quiz_questions_e_bonus[quiz_question] + " ")
            if input_holder == key_chain_e_bonus[quiz_question]:
                quiz_question += 1
                attempts = 0
                quiz_difficulty_e_bonus_proxy = quiz_difficulty_e_bonus_proxy.replace(quiz_questions_e_bonus[quiz_question-1],key_chain_e_bonus[quiz_question-1])
                print quiz_difficulty_e_bonus_proxy
                print random_ui_words("winner")
            else:
                attempts += 1
                print "Are you even human?.. You have",5 - attempts, "attempts left"
        if attempts >= 5:
            return "You lose"
    mega_points[0] += 45
    quiz_compleate_status_e[0] += 1
    return the_quiz()

def quiz_m():
    quiz_question = 0
    attempts = 0
    quiz_difficulty_m_proxy = quiz_difficulty_m
    input_holder = "m"
    print quiz_difficulty_m
    while quiz_question < len(quiz_questions_m):
        if attempts < 5:
            input_holder = raw_input("Please fill in " + quiz_questions_m[quiz_question] + " ")
            if input_holder == key_chain_m[quiz_question]:
                quiz_question += 1
                attempts = 0
                quiz_difficulty_m_proxy = quiz_difficulty_m_proxy.replace(quiz_questions_m[quiz_question-1],key_chain_m[quiz_question-1])
                print quiz_difficulty_m_proxy
                print random_ui_words("winner")
            else:
                attempts += 1
                print "Are you even human?.. You have",5 - attempts, "attempts left"
        if attempts >= 5:
            return "You lose"
    mega_points[0]  += 15
    quiz_compleate_status_m[0] += 1
    return the_quiz()

def quiz_h():
    quiz_question = 0
    attempts = 0
    quiz_difficulty_h_proxy = quiz_difficulty_h
    print quiz_difficulty_h
    while quiz_question < len(quiz_questions_h):
        input_holder = raw_input("Please fill in " + quiz_questions_h[quiz_question] + " ")
        if attempts < 5:
            if input_holder == key_chain_h[quiz_question]:
                quiz_question += 1
                attempts = 0
                quiz_difficulty_h_proxy = quiz_difficulty_h_proxy.replace(quiz_questions_h[quiz_question-1],key_chain_h[quiz_question-1])
                print quiz_difficulty_h_proxy
                print random_ui_words("winner")
            else:
                attempts += 1
                print "Are you even human?.. You have",5 - attempts, "attempts left"
        if attempts >= 5:
            return "You lose"
    mega_points[0] += 30
    quiz_compleate_status_h[0] += 1
    return the_quiz()

def quiz_i():
    quiz_question = 0
    attempts = 0
    quiz_difficulty_i_proxy = quiz_difficulty_i
    print quiz_difficulty_i
    while quiz_question < len(quiz_questions_i):
        if attempts < 5:
            if raw_input("Please fill in " + quiz_questions_i[quiz_question] + " ") == key_chain_i[quiz_question]:
                quiz_question += 1
                attempts = 0
                quiz_difficulty_i_proxy = quiz_difficulty_i_proxy.replace(quiz_questions_i[quiz_question-1],key_chain_i[quiz_question-1])
                print quiz_difficulty_i_proxy
                print random_ui_words("winner")
            else:
                attempts += 1
                print "Are you even human?.. You have",5 - attempts, "attempts left"
        if attempts >= 5:
            return "You lose"
    mega_points[0] += 50
    quiz_compleate_status_i[0] = True
    return the_quiz()

#_._______________________________________________________________________
#                                  Game

def quiz_printer():#this prints game_intro string with .format
    game_intro_proxy = game_intro
    easy_bonus = "What do we call young animals?    "
    medium_bonus = "Know these Albert Einstein-Quotes?"
    hard_bonus = "Know who said these Star Wars lines?"
    insane_bonus = "Complete the series.                "
    if quiz_compleate_status_e[0] == 1:
            easy_bonus = "-       <<<BONUS ROUND>>>        -"
    if quiz_compleate_status_m[0] == 1:
            medium_bonus = "-     <<<BONUS ROUND>>>          -"
    if quiz_compleate_status_h[0] == 1:
            hard_bonus = "-     <<<BONUS ROUND>>>            -"
    if quiz_compleate_status_i[0] == 1:
            insane_bonus = "-     <<<BONUS ROUND>>>            -"

    if quiz_compleate_status_e[0] == 2:
            easy_bonus = "-     <<<<<<<FIN>>>>>>>          -"
    if quiz_compleate_status_m[0] == 2:
            medium_bonus = "-     <<<<<<<FIN>>>>>>>          -"
    if quiz_compleate_status_h[0] == 2:
            hard_bonus = "-     <<<<<<<FIN>>>>>>>            -"
    if quiz_compleate_status_i[0] == 2:
            insane_bonus = "-     <<<<<<<FIN>>>>>>>            -"
    print game_intro_proxy.format(ui_tweak("MegaPoints999"), easy_bonus, medium_bonus, hard_bonus, insane_bonus)

def quiz_status(status_check): # status: 0 = none finished, 1 = bonus round available, 2 = completed both normal and bonus quiz
    if status_check == "AllDoneChek":
        if quiz_compleate_status_e[0] and quiz_compleate_status_m[0] and quiz_compleate_status_h[0] and quiz_compleate_status_i[0] == 2:
            return False
        return True
    if status_check == "easy":
        return quiz_compleate_status_e[0]
    if status_check == "medium":
        return quiz_compleate_status_m[0]
    if status_check == "hard":
        return quiz_compleate_status_h[0]
    if status_check == "insane":
        return quiz_compleate_status_i[0]

def quiz_runner(diff):#Takes string input from quiz_select, and runs appropriate quiz and checks if bonus1 or first0.
    if diff == "easy":
        if quiz_status("easy") == 0:
            return quiz_e()
        if quiz_status("easy") == 1:
            return quiz_e_bonus()
        return the_quiz()
    if diff == "medium":
        if quiz_status("medium") == 0:
            return quiz_m()
        if quiz_status("medium") == 1:
            return "quiz_m_bonus()"
        return the_quiz()
    if diff == "hard":
        if quiz_status("hard") == 0:
            return quiz_h()
        if quiz_status("hard") == 1:
            return "quiz_h_bonus()"
        return the_quiz()
    if diff == "insane":
        if quiz_status("insane") == 0:
            return quiz_i()
        if quiz_status("insane") == 1:
            return "quiz_i_bonus()"
        return the_quiz()

def quiz_select(user_input): #uses the user input from the_quiz to run the apropriate quiz, also allows for variants in answers as defined globaly by difficulty_answers_list
    if difficulty_answers_list[0].find(user_input) >= 2: #Easy
        return quiz_runner("easy")
    if difficulty_answers_list[1].find(user_input) >= 2: #Medium
        if user_input != "i": #this allows the use of "i" for insane difficulty.
            return quiz_runner("medium")
    if difficulty_answers_list[2].find(user_input) >= 2: #Hard
        return quiz_runner("hard")
    if difficulty_answers_list[3].find(user_input) >= 2: #Insane
        return quiz_runner("insane")
    return "false"

def input_check(user_input):#used to check if inputs are correct answers without running quiz, # 1 =east 2=medium 3=hard 4=insane ,# added this after quiz select to allow for inccorect answers.
    if difficulty_answers_list[0].find(user_input) >= 2: #Easy
        return 1
    if difficulty_answers_list[1].find(user_input) >= 2: #Medium
        if user_input != "i": #this allows the use of "i" for insane difficulty.
            return 2
    if difficulty_answers_list[2].find(user_input) >= 2: #Hard
        return 3
    if difficulty_answers_list[3].find(user_input) >= 2: #Insane
        return 4
    return False

def the_quiz():#the_quiz
    quiz_printer()
    print random_ui_words("greetings")
    input_holder = "0"
    if input_holder != "0":
        quiz_printer()
        print """ "Can you get all the points? Probably not... Type 1 for easy. <<" """
    if quiz_status("AllDoneChek") == False:
        print you_win
    input_holder = raw_input("Please type in a difficulty: ")
    if input_check(input_holder) == 1 or 2 or 3 or 4:
        quiz_select(input_holder)
    if input_check(input_holder) == False:
        if difficulty_answers_list[4].find(input_holder) >= 2:#checks if the input was user wanting to quit,  if not assumes a mistake is made in input and returns quiz again for another go.
            ui_tweak("MegaPoints999")
            print "Thanks for Quitting, I knew you couldn't finish! HAHAHAHA!!!"
            return
            input_holder = quiz_select(input_holder)
        the_quiz()
the_quiz()
