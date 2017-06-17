#_._______________________________________________________________________
#                                 Easy quiz
#For Ui keep key (__1__) the same length as answer. e.g. for improve: use __1____
#I use find (Ctrl + f) to change multiple items. Find "_new" and replace the name of the quiz
#1, 2 and 3 are placeholders to test.

key__1__new =             "1" #"kitten"
key__2__new =             "2" #"chick"
key__3__new =             "3" #"bunny"
key_chain_new =           [key__1__new, key__2__new, key__3__new]
quiz_questions_new  =     ["__1_", "__2_", "__3_"]

quiz_difficulty_new = """
_________________________________________________________________________________
|------------------------>}>? Quiz title:          <)<---------------------------|
|-                         -     Quiz heading     -                             -|
|-                          ----------------------                              -|
|-                            question a __1_                                   -|
|-                            question b __2_                                   -|
|-                            question c __3_                                   -|
|--------------------------------------------------------------------------------|
|________________________________________________________________________________|
"""
#_._______________________________________________________________________

def quiz_new():
    quiz_question = 0
    attempts = 0
    quiz_difficulty_new_proxy = quiz_difficulty_new
    input_holder = "new"
    print quiz_difficulty_new
    while quiz_question < len(quiz_questions_new):
        if attempts < 5:
            input_holder = raw_input("Please fill in " + quiz_questions_new[quiz_question] + " ")
            if input_holder == key_chain_new[quiz_question]:
                quiz_question += 1
                attempts = 0
                quiz_difficulty_new_proxy = quiz_difficulty_new_proxy.replace(quiz_questions_new[quiz_question-1],key_chain_new[quiz_question-1])
                print quiz_difficulty_new_proxy
                print random_ui_words("winner")
            else:
                attempts += 1
                print "Are you even human?.. You have",5 - attempts, "attempts left"
        if attempts >= 5:
            return "You lose"
    mega_points[0] += 5
    quiz_compleate_status_new[0] = 1
    return the_quiz()
