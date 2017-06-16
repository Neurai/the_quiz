#-1
#000
#1111
#22222
#333333
#_._______________________________________________________________________
#                               Quiz start
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
""" #this never updates after with the points.
#_._______________________________________________________________________
#                              Extra features
# status: 0 = none finished, 1 = bonus round available, 2 = finished all

#yet to impliment method of resetting all quiz states to new: 0 with a for loop? needs changing
#quiz_reset = [quiz_compleate_status_e[0], quiz_compleate_status_m[0],quiz_compleate_status_h[0], quiz_compleate_status_i[0]]
#
you_win = " !!YOU--WIN!! " * mega_points[0]
difficulties_l = ["easy", "medium", "hard", "insane" ]
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
key_b_i =            "2" #" 9"
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
#                             Global V

#def quiz_status(n):
quiz_compleate_status_e = [0]
quiz_compleate_status_m = [0]
quiz_compleate_status_h = [0]
quiz_compleate_status_i = [0]
#_._______________________________________________________________________
#                      Quiz per difficulty. Functions:
def quiz_e():
    quiz_question = 0
    attempts = 0
    quiz_difficulty_e_proxy = quiz_difficulty_e
    game_intro_proxy = game_intro
#Help^^^ Please tell me why i needed this? what is it called?
#without it i had errors further in the code tryng to call quiz_difficulty_e further in the function using .replace, saying it was called before being defined.
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
                print "Congratulations!! Next!"
            else:
                attempts += 1
                print "Are you even human?.. You have",5 - attempts, "attempts left"
        if attempts >= 5:
            return "You lose"
    game_intro_proxy = game_intro.replace("What do we call young animals?", "-    <<<<BONUS ROUND>>>      -")
    mega_points[0] += 5
    quiz_compleate_status_e[0] = 1
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
                print "Congratulations!! Next!"
            else:
                attempts += 1
                print "Are you even human?.. You have",5 - attempts, "attempts left"
        if attempts >= 5:
            return "You lose"
    mega_points[0]  += 15
    quiz_compleate_status_m[0] = 1
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
                print "Congratulations!! Next!"
            else:
                attempts += 1
                print "Are you even human?.. You have",5 - attempts, "attempts left"
        if attempts >= 5:
            return "You lose"
    mega_points[0] += 30
    quiz_compleate_status_h[0] = 1
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
                print "Congratulations!! Next!"
            else:
                attempts += 1
                print "Are you even human?.. You have",5 - attempts, "attempts left"
        if attempts >= 5:
            return "You lose"
    mega_points[0] += 50
    quiz_compleate_status_i[0] = True
    return "You got  >> 5 Mega points!! << for beating Hard" ,the_quiz()

#_._______________________________________________________________________
#                                  Game
quiz_key = (ui_tweak("MegaPoints999"),"What do we call young animals?", "Know these Albert Einstein-Quotes?", "Know who said these Star Wars lines?", "Complete the series.       " )

def quiz_printer():
    game_intro_proxy = game_intro
    easy_bonus = "What do we call young animals?    "
    medium_bonus = "Know these Albert Einstein-Quotes?"
    hard_bonus = "Know who said these Star Wars lines?"
    insane_bonus = "Complete the series.                "
    if quiz_compleate_status_e[0] == 1:
            easy_bonus = "-     <<<BONUS ROUND>>>          -"
    if quiz_compleate_status_m[0] == 1:
            medium_bonus = "-     <<<BONUS ROUND>>>          -"
    if quiz_compleate_status_h[0] == 1:
            hard_bonus = "-     <<<BONUS ROUND>>>            -"
    if quiz_compleate_status_i[0] == 1:
            insane_bonus = "-     <<<BONUS ROUND>>>            -"

    if quiz_compleate_status_e[0] == 2:
            easy_bonus = "-     <<<____FIN____>>>          -"
    if quiz_compleate_status_m[0] == 2:
            medium_bonus = "-     <<<____FIN____>>>          -"
    if quiz_compleate_status_h[0] == 2:
            hard_bonus = "-     <<<____FIN____>>>            -"
    if quiz_compleate_status_i[0] == 2:
            insane_bonus = "-     <<<____FIN____>>>            -"
    print game_intro_proxy.format(ui_tweak("MegaPoints999"), easy_bonus, medium_bonus, hard_bonus, insane_bonus)

def quiz_status(d): # status: 0 = none finished, 1 = bonus round available, 2 = finished all
    if d == "AllDoneChek":
        if quiz_compleate_status_e[0] and quiz_compleate_status_m[0] and quiz_compleate_status_h[0] and quiz_compleate_status_i[0] == 2:
            return False
        return True
    if d == "easy":
        return quiz_compleate_status_e[0]
    if d == "medium":
        return quiz_compleate_status_m[0]
    if d == "hard":
        return quiz_compleate_status_h[0]
    if d == "insane":
        return quiz_compleate_status_i[0]

def quiz_runner(diff):
    if diff == "easy":
        if quiz_status("easy") == 0:
            return quiz_e()
        return "quiz_e_bonus()"
    if diff == "medium":
        if quiz_status("medium") == 0:
            return quiz_m()
        return "quiz_m_bonus()"
    if diff == "hard":
        if quiz_status("hard") == 0:
            return quiz_h()
        return "quiz_h_bonus()"
    if diff == "insane":
        if quiz_status("insane") == 0:
            return quiz_i()
        return "quiz_i_bonus()"

def the_quiz():
    quiz_printer()
    print "Welcome!!"
    input_holder = "0"
    difficulty_answers_list = ["   easy Easy 1", "    medium Medium 2", "    hard Hard 3","     insane Insane 4","     q Q quit QUIT exit EXIT Quit "] # would have done this better with another attempt, I wanted to increase the amount of possible answers, this wouldnt work in many situations.
    while input_holder != -1:
        if input_holder != "0":
            quiz_printer()
            print """ "Can you get all the points? Probably not... Type 1 for easy. <<" """
        if quiz_status("AllDoneChek") == False:
            print you_win
            break
        input_holder = raw_input("Please type in a difficulty: ")
        #Easy
        if difficulty_answers_list[0].find(input_holder) >= 2:
            quiz_runner("easy")
            break
        #Medium
        if difficulty_answers_list[1].find(input_holder) >= 2: #i is meant for other difficuly
            if input_holder != "i":
                quiz_runner("medium")
                break
        #Hard
        if difficulty_answers_list[2].find(input_holder) >= 2:
            quiz_runner("hard")
            break
        #Insane
        if difficulty_answers_list[3].find(input_holder) >= 2:
            quiz_runner("insane")
            break
        #checking if user wants to quit
        if difficulty_answers_list[4].find(input_holder) >= 2:
            ui_tweak("MegaPoints999")
            print "Thanks for playing,"
            break


the_quiz()
