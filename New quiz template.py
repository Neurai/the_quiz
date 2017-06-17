#_._______________________________________________________________________
#                                 Easy bonus quiz
#For Ui keep key (__1__) the same length as answer. e.g. for improve: use __1____
#I use find (Ctrl + f) to change multiple items. Find "_e_bonus" and replace the name of the quiz
#1, 2 and 3 are placeholders to test.

key__1__e_bonus =             "1"#"Tom"
key__2__e_bonus =             "1"#"Doe"
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
