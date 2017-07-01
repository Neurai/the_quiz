#neurai
import random
#_._______________________________________________________________________
#                               Random/ tweaks

mega_points = [000] #the number of mega points the player has.

def ui_tweak(ui_element):
    #Args:
        #ui_element: the element of the ui output will appear
    #Behavior:
        #used to print out mega_points in style!
    #returns:
        #the string "Total Mega Points! :" and the amount of points the player has.
    if ui_element == "MegaPoints999": #adjust the ui to fit 999, len(23)
        if mega_points[0] < 10:
            return "Total Mega Points! :" + "00" + str(mega_points[0])
        if mega_points[0] < 100:
            return "Total Mega Points! :" + "0" + str(mega_points[0])
        if mega_points[0] > 999:
            return "Total Mega Points! :" + "999"
        return "Total Mega Points! :" +  str(mega_points[0])

def random_ui_words(style):
    #Args:
        #style: this selects what type of message to return.
    #Behavior:
        #returns a random phrase/string from one of the contained lists.
            #used to give character to tha game.
    #returns:
        #a random string for printing.
    greetings = ["Hello sunshine!", "Howdy partner!", "What's kickin' little chicken?", "Ahoy matey!", "Hiya!",
                "At least we meet for the first time for the last time!", "I like your face.", "Whats cookin good lookin'?",
                "Aloha", "Hola!", "Bonjour!", "Hallo!!", "Konnichiwa!", "I'm Batman!", "Here's Johnny!", "Ello govnuh!",
                "Top o the mornin to ya!", "GOOOOOD MORNING VIETNAM!", "Why hello there!", "Look who it is!",
                "Look what the cat dragged in!", "greets!", "what's cooking?", "What's cracking?", "Yello!",
                "A-Yo!", "G'day!", "Good to see you!", "Nice to see you!", "Long time no see!",
                "It's been a while!", "How have you been?", "G'day", "How do you do?", "G'day",
                "It's nice to meet you!", "Pleased to meet you!", "Good day!", "Yo!",
                "Are you OK?", "You alright?", "Alright mate?", "Howdy!","Sup?", "Whazzup?", "G'day mate!"]
    winner   = ["Groovy!","Righteous!", 'Nifty!', 'Copasetic!', 'Future Pulitzer Prize winner!', 'Future rock star!',
                'Future CEO!', 'You shine as brightly as the sun!', 'Success comes to those who work their ass off.', 'Felicitations',
                'Herzlichen Gluckwunsch', 'I am overjoyed with your success. Shine on!', "You've made us all so proud. I am very happy for you.",
                'Good work. Your hard work has truly paid off.', "You've got the right mix of dedication and enthusiasm. Keep it up!",
                'Congratulations for achieving so much on your own steam.', "It's the time for recognition! Well done my dear friend.",
                'Congratulations for making it big.', 'You have earned all the praises you are now receiving.',
                'Congrats. Am in awe of you for the rest of my life', 'May this moment last forever. Congratulations.',
                'You are our shining star. Well done.', "Congratulations for scaling new heights and setting new standards.",
                "May this moment last forever. Congratulations.","There was never a doubt in our hearts", "you were destined for success. Congratulations on your achievement!",
                "Many, many congratulations on your impressive performance.", "You have truly set a new record!",
                "Your will to push and never give up has brought you this far, you deserve this and more. Congratulations for a marvelous achievement!",
                "We are taught that the sky should always be the limit", " you have showed us that truly we should think beyond the sky.",
                "Some are destined to fit in, but you were born to stand out! You have made me proud","Congratulations on a brilliant victory!",
                "Life being a journey, Success has brought you many miles ahead of many people. Congratulations",
                "Cheers to never giving up!", "Enjoy the fruits of you labor and may you always succeed in whatever you do", "Congratulations my friend!",
                "Dreams for success rarely materialize without dedication, perseverance, passion and hard work combined to make it a reality.",
                "Well done!", "Congratulations and thank you!", "It is inspirational to witness hard work finally give birth to success. Congratulations!",
                "you worked hard, you deserve it, you have got it!", "Please accept my congratulations on this wonderful demonstra of your merits",
                "First they ignore you... Then they laugh and fight against you... Then you win!",
                "Congratulations for your fabulous victory! You deserve it every bit! Aim for the stars!",
                "Congratulations on your success! You have made us all proud. Keep up the good work!",
                "If Oscars were given for a job well done, I'd nominate you!", "Congratulations for your fantastic achievement!",
                "You, why you little, Champion!", "C-C-C-Combo", "Your hard work and effort have paid off! A success well deserved, an occasion worth celebrating! Congratulations!",
                "Your achievements speaks itself about your capabilities.", "Slow and steady makes it to the top!", "Good job!"]
    if style == "greetings":
        return random.choice(greetings)
    if style == "winner":
        return random.choice(winner)
#_._______________________________________________________________________
#                             quiz select UI


quiz_select = {
    'AnswerVariants': { #these are the answers available for each option"
            'easy':     "    easy Easy 1",
            'medium':   "    medium Medium 2",
            'hard':     "    hard Hard 3",
            'insane':   "    insane Insane 4",
            'quit':     "    q Q quit QUIT exit EXIT Quit"
        },
    'quiz_select_ui':   """
        ________________|_______________________|__________________
        |------------=>>>!! Welcome to the quiz !!<<<=------------|
        |-               -------------------------               -|
        |-   -Please write out the difficulty you can handle!-   -|
        |-              ___________________________              -|
        |-             |  {}  |             -|
        |-                                                       -|
        |-   1. Easy:    {}      -|
        |-   2. Medium:  {}      -|
        |-   3. Hard:    {}      -|
        |-   4. Insane:  {}      -|
        |----------------------------|----------------------------|
        |- >>>>>>>>>> Type in "Quit" or "q" to exit <<<<<<<<<<<< -|
        |__________-=|=-_____________|___________-=|=-____________|
        """#this is the main UI, player selects a difficulty to play or quits
    }
#_._______________________________________________________________________
#                             Easy quiz data

quiz_easy_data = {
    'QuizFeature': {
            'CurrentLvl': 1,        #this is the current level of quiz the player is up to.
            'attempts': 0,          #global numbor of current players invalid attempts.
                                        #cannot reset attempts, once it == MaxAttempts that difficulty is "locked".
            'MaxAttempts': 10,      #these are the maximum amount of attempts the player can have.
            'CompletePoints': 5,    #the number of points awarded after completing a quiz.
                                        #points are multiplied by the current level inside quiz_feature_update().
            'difficulty': "easy"    #not used yet.
        },
    1: { #quiz easy level 1.
            'quiz': """
             ________________________________________________________________________________
            |------------------------>}>? Animal Names: Young ?<)<---------------------------|
            |-                         - If a dog has a puppy -                             -|
            |-                          ----------------------                              -|
            |-                            A cat has a __1___                                -|
            |-                            A chicken a __2__                                 -|
            |-                         A rabbit has a __3__                                 -|
            |-                          A sheep has a __4_                                  -|
            |--------------------------------------------------------------------------------|
            |________________________________________________________________________________|
            """, #The UI of the quiz displaying the questions with masked answers matching [ReplaceKey].
            'answers':    ["kitten", "chick", "bunny", "lamb"], #the answers.
            'ReplaceKey': ["__1___", "__2__", "__3__", "__4_"]  #these should match the blanks inside the UI so replacements work.
        },                                                          #replacements should match answers in length so UI doesn't break
    2: { #quiz easy level 2.
            'quiz': """
             ________________________________________________________________________________
            |----------------------->}>?  Animal Names: Female ?<)<--------------------------|
            |-              - What are the female names 0f these animals? -                 -|
            |-                          -----------------------                             -|
            |-            Cat = _1_    ||   Chicken = _4_     ||   Dog = _7___              -|
            |-           Deer = _2_    ||     Horse = _5__    ||   Fox = _8___              -|
            |-          Sheep = _3_    ||    Rabbit = _6_     ||  Wolf = _9___              -|
            |-                                                                              -|
            |--------------------------------------------------------------------------------|
            |                         > All names are capitalised <                          |
            |________________________________________________________________________________|
            """,
            'answers':    ["Tom", "Doe", "Ewe", "Hen", "Mare", "Doe", "Bitch", "Vixen", "Bitch" ],
            "ReplaceKey": ["_1_", "_2_", "_3_","_4_", "_5__", "_6_","_7___", "_8___", "_9___"]
        }
    }
#_._______________________________________________________________________
#                             Medium quiz data

quiz_medium_data = {
    'QuizFeature': {
            'CurrentLvl': 1,
            'attempts': 0,
            'MaxAttempts': 10,
            'CompletePoints': 30,
            'difficulty': "medium"
        },
    1: { #level 1
            'quiz': """

            _______________________________________________________________________________________________________
            |------------------------------>]>? Know these Albert Einstein-Quotes ?<\<----------------------------|
            |-                                                                                                   -|
            |-                        "Imagination is more __1______ than knowledge"                             -|
            |-    "The __1______ thing is not to __3_ questioning. Curiosity _2_ its own reason for existing."   -|
            |-              "Anyone who _2_ never made a mistake _2_ never tried anything _4_."                  -|
            |-                                                                                                   -|
            |-----------------------------------------------------------------------------------------------------|
            |                           >>>>>>>>> Please type non capitalized <<<<<<<<<                           |
            |_____________________________________________________________________________________________________|
            """,
            'answers':    ["important", "has", "stop", "new"],
            'ReplaceKey': ["__1______", "_2_", "__3_", "_4_"]

        },
    2: { #level 2
            'quiz': """
            ______________________________________________________________________________________
            |---------------------->}>? Know these Albert Einstein-Quotes ?<)<--------------------|
            |-                - Complete these not so famous sayings from Albert -               -|
            |-                              -----------------------                              -|
            |-                                                                                   -|
            |- Education _4 what remains after one has __1______ what one has learned in school. -|
            |-              Before _2_ we are all __3____ wise - and __3____ foolish.            -|
            |-                     The only source of knowledge _4 __5_______.                   -|
            |-       If you can't explain it __6___, you don't __7_______ it well enough.        -|
            |-                    When the __8_____ _4 simple, _2_ _4 answering.                 -|
            |-                                                                                   -|
            |-------------------------------------------------------------------------------------|
            |                             > All names are capitalized <                           |
            |_____________________________________________________________________________________|
            """,
            'answers':    ["forgotten", "God", "equally", "is", "experience", "simply", "understand", "solution" ],
            "ReplaceKey": ["__1______", "_2_", "__3____","_4", "__5_______", "__6___","__7_______", "__8_____"]
        }
    }
#_._______________________________________________________________________
#                              Hard quiz data

quiz_hard_data = {
    'QuizFeature': {
            'CurrentLvl': 1,
            'attempts': 0,
            'MaxAttempts': 7,
            'CompletePoints': 95,
            'difficulty': "hard"
        },
    1: { #level 1
            'quiz': """
            _______________________________________________________________________________________________________
            |----------------------------->!>? Know who said these Star Wars-Quotes ?<|<--------------------------|
            |-                                                                                                   -|
            |-                        "Do. Or do not. there is no try." - __1_                                   -|
            |-                           "Great, kid. Don't get cocky." - __2_____                               -|
            |-         "Aren't you a little short for a storm trooper?" - __3__________                          -|
            |-          "These aren't the droids you're looking for..." - __4___________                         -|
            |-                  "I find your lack of faith disturbing." - __5________                            -|
            |-                                     "Bleep, Bleep Bloop" - __6__   **-** has hyphen               -|
            |-                                                                                                   -|
            |-----------------------------------------------------------------------------------------------------|
            |   >>>>>>>>> Please type names capitalized, e.g: "Jar Jar Binks" NOT: "jar jar binks" <<<<<<<<<      |
            |_____________________________________________________________________________________________________|
            """,
            'answers':    ["Yoda", "Han Solo", "Princess Leia", "Obi Wan Kenobi", "Darth Vader", "R2-D2"],
            'ReplaceKey': ["__1_", "__2_____", "__3__________", "__4___________", "__5________", "__6__"]

        },
    2: { #level 2
            'quiz': """
            ______________________________________________________________________________________
            |--------------------->!>? Know who said these Star Wars-Quotes ?<|<------------------|
            |-                              - Who said these lines?? -                           -|
            |-                                ______________________                             -|
            |-  Help me, Obi-Wan Kenobi. You're my only hope.  -----------   = _____1_____       -|
            |-  The Force will be with you. Always.  ---------------------   = ______2_______    -|
            |-  Never tell me the odds!   --------------------------------   = ___3____          -|
            |-  Just for once, let me look on you with my own eyes. ------   = _______4________  -|
            |-  I'm just a simple man trying to make my way in the universe. = __5_______        -|
            |-------------------------------------------------------------------------------------|
            |                all names are capitalized <--> no hyphens, use space                 |
            |_____________________________________________________________________________________|
            """,
            'answers':    ["Leia Organa", "Obi Wan Kenobi", "Han Solo", "Anakin Skywalker", "Jango Fett"],
            "ReplaceKey": ["___1_______", "______2_______", "___3____","_______4________", "__5_______"]
        }
    }
#_._______________________________________________________________________
#                               Insane data

quiz_insane_data = {
    'QuizFeature': {
            'CurrentLvl': 1,
            'attempts': 0,
            'MaxAttempts': 4,
            'CompletePoints': 140,
            'difficulty': "insane"
        },
    1: { #level 1
            'quiz': """
            _________________________________________________________________________________
            |------------------------>^>? Complete the series ?<&<---------------------------|
            |-                                                                              -|
            |-                              9 = 4      21 = 9                               -|
            |-                             22 = 9      24 = 10                              -|
            |-                              8 = 5       7 = 5                               -|
            |-                             99 = 10    100 = 7                               -|
            |-                             16 = _a_?   17 = _b_?                            -|
            |-                                                                              -|
            |--------------------------------------------------------------------------------|
            |________________________________________________________________________________|
            """,
            'answers':    ["7   ", "9   "],
            'ReplaceKey': ["_a_?", "_b_?"]

        },
    2: { #level 2
            'quiz': """
            _______________________________________________________________________________________
            |------------------------------>!>! Impossibro !<|<------------------------------------|
            |-                          - Find the missing letter -                               -|
            |-                            -----------------------                                 -|
            |-                                                                                    -|
            |-       A = 5   |   E = 9   |   I = 13  |   M = 17  |   Q = 21  |   U = 25  |        -|
            |-       Y = 29  |   F = 10  |   J = 14  |   N = 18  |   R = 22  |   V = 26  |        -|
            |-       Z = 30  |   C = 7   |   G = 11  |   K = 15  |   O = 19  |   S = 23  |        -|
            |-       W = 27  |   D = 8   |   H = 12  |   L = 16  |   P = 20  |   T = 24  |        -|
            |-                                 |   X = 28  |                                      -|
            |-                                                                                    -|
            |-                               _____       _____                                    -|
            |-                              |     |     |     |                                   -|
            |-         Find this letter --> |  ?  |     |  G  |                                   -|
            |-                              |_____|_____|_____|                                   -|
            |-                                    |     |                                         -|
            |-                                    |  B  |                                         -|
            |-                               _____|_____|_____                                    -|
            |-                              |     |     |     |                                   -|
            |-                              |  S  |     |  p  |                                   -|
            |-                              |_____|     |_____|                                   -|
            |-                                                                                    -|
            |--------------------------------------------------------------------------------------|
            |                            Write letter capitalized!                                 |
            |______________________________________________________________________________________|

            """,
            'answers':    ["J"],
            "ReplaceKey": ["?"]
        }
    }
#_._______________________________________________________________________
#                              Quiz functions

def quiz_printer():
    #Behavior:
        #prints an updated UI for player to select a difficulty from
    #returns:
        #prints quiz_select_ui with.format changes
    game_intro_proxy =  quiz_select['quiz_select_ui']
    easy_ui_entry = "-       <<<  ROUND " + str(quiz_easy_data['QuizFeature']['CurrentLvl']) + "  >>>        -"
    medium_ui_entry = "-       <<<  ROUND " + str(quiz_medium_data['QuizFeature']['CurrentLvl']) + "  >>>        -"
    hard_ui_entry = "-       <<<  ROUND " + str(quiz_hard_data['QuizFeature']['CurrentLvl']) + "  >>>        -"
    insane_ui_entry = "-       <<<  ROUND " + str(quiz_insane_data['QuizFeature']['CurrentLvl']) + "  >>>        -"

    if quiz_easy_data['QuizFeature']['CurrentLvl'] == len(quiz_easy_data):
            easy_ui_entry = "-       <<<<<<<FIN>>>>>>>        -"
    if quiz_medium_data['QuizFeature']['CurrentLvl'] == len(quiz_medium_data):
            medium_ui_entry = "-       <<<<<<<FIN>>>>>>>        -"
    if quiz_hard_data['QuizFeature']['CurrentLvl'] == len(quiz_hard_data):
            hard_ui_entry = "-       <<<<<<<FIN>>>>>>>        -"
    if quiz_insane_data['QuizFeature']['CurrentLvl'] == len(quiz_insane_data):
            insane_ui_entry = "-       <<<<<<<FIN>>>>>>>        -"
    print game_intro_proxy.format(ui_tweak("MegaPoints999"), easy_ui_entry, medium_ui_entry, hard_ui_entry, insane_ui_entry)

def quiz_feature_update(diff,state):
    #Args:
        #diff: difficulty of the recently played quiz.
        #state: what state the quiz was when it finished (win, TryAgain).
    #Behavior:
        #preforms all updates for each quiz depending on the status of its completion,
        #if, all answers in the quiz are correct it updates the score and increases the current LVL of the quiz +1, else: prints "Try again!"*9001
    #returns:
        #the_quiz with a valid string "win", "TryAgain" to print appropriate returning message.
    if state == "win":
        if diff == "easy":
            mega_points[0] =  mega_points[0] + (quiz_easy_data["QuizFeature"]["CompletePoints"]*quiz_easy_data['QuizFeature']['CurrentLvl'])
            quiz_easy_data['QuizFeature']['CurrentLvl'] = quiz_easy_data['QuizFeature']['CurrentLvl'] + 1;
        if diff == "medium":
            mega_points[0] =  mega_points[0] + (quiz_medium_data["QuizFeature"]["CompletePoints"]*quiz_medium_data['QuizFeature']['CurrentLvl'])
            quiz_medium_data['QuizFeature']['CurrentLvl'] = quiz_medium_data['QuizFeature']['CurrentLvl'] + 1;
        if diff == "hard":
            mega_points[0] =  mega_points[0] + (quiz_hard_data["QuizFeature"]["CompletePoints"]*quiz_hard_data['QuizFeature']['CurrentLvl'])
            quiz_hard_data['QuizFeature']['CurrentLvl'] = quiz_hard_data['QuizFeature']['CurrentLvl'] + 1;
        if diff == "insane":
            mega_points[0] =  mega_points[0] + (quiz_insane_data["QuizFeature"]["CompletePoints"]*quiz_insane_data['QuizFeature']['CurrentLvl'])
            quiz_insane_data['QuizFeature']['CurrentLvl'] = quiz_insane_data['QuizFeature']['CurrentLvl'] + 1;
        return the_quiz('win')
    if state == "TryAgain":
        print "Try again!"*9001 #Hinders player from scrolling up in the terminal to check answers. And looks fun
        return the_quiz('TryAgain')

def quiz_e():
    #Behavior:
        #Runs the easy quiz using the current level value in quiz_easy_data['QuizFeature']['CurrentLvl']
    #returns:
        #provides quiz_feature_update() with two arguments.
            #difficulty:what the quiz difficulty is
            #state: if player "won" the quiz then state == "won" if attempts == MaxAttempts then state == TryAgain
    quiz_question = 0
    current_lvl = quiz_easy_data['QuizFeature']['CurrentLvl']
    ui_proxy = quiz_easy_data[current_lvl]['quiz']
    print ui_proxy
    for answers in quiz_easy_data[current_lvl]['answers']:
        while (1 + 1) == 2:
            if quiz_easy_data['QuizFeature']['attempts'] < quiz_easy_data['QuizFeature']['MaxAttempts']:
                input_holder = raw_input("Please fill in " + quiz_easy_data[current_lvl]["ReplaceKey"][quiz_question] + " ")
                if input_holder == answers:
                    quiz_question += 1
                    ui_proxy = ui_proxy.replace(quiz_easy_data[current_lvl]["ReplaceKey"][quiz_question-1],answers)
                    print ui_proxy
                    print random_ui_words("winner") #18
                    break
                quiz_easy_data['QuizFeature']['attempts'] = quiz_easy_data['QuizFeature']['attempts'] +1;
                print "Are you even human?.. You have",5 - quiz_easy_data['QuizFeature']['attempts'], "attempts left"
            else:
                return  quiz_feature_update("easy","TryAgain")
    return quiz_feature_update("easy","win")

    #Behavior:
        #Runs the medium quiz using the current level value in quiz_medium_data['QuizFeature']['CurrentLvl']
    #returns:
        #provides quiz_feature_update() with two arguments.
            #difficulty: tells quiz_feature_update() what the quiz difficulty was
            #state: if player "won" the quiz then state == "won" if attempts == MaxAttempts then state == TryAgain
    quiz_question = 0
    current_lvl = quiz_medium_data['QuizFeature']['CurrentLvl']
    ui_proxy = quiz_medium_data[current_lvl]['quiz']
    print ui_proxy
    for answers in quiz_medium_data[current_lvl]['answers']:
        while (1 + 1) == 2:
            if quiz_medium_data['QuizFeature']['attempts'] < quiz_medium_data['QuizFeature']['MaxAttempts']:
                input_holder = raw_input("Please fill in " + quiz_medium_data[current_lvl]["ReplaceKey"][quiz_question] + " ")
                if input_holder == answers:
                    quiz_question += 1
                    ui_proxy = ui_proxy.replace(quiz_medium_data[current_lvl]["ReplaceKey"][quiz_question-1],answers)
                    print ui_proxy
                    print random_ui_words("winner") #18
                    break
                quiz_medium_data['QuizFeature']['attempts'] = quiz_medium_data['QuizFeature']['attempts'] +1;
                print "Are you even human?.. You have",5 - quiz_medium_data['QuizFeature']['attempts'], "attempts left"
            else:
                return  quiz_feature_update("medium","TryAgain")
    return quiz_feature_update("medium","win")

def quiz_h():
    #Behavior:
        #Runs the hard quiz using the current level value in quiz_hard_data['QuizFeature']['CurrentLvl']
    #returns:
        #provides quiz_feature_update() with two arguments.
            #difficulty: tells quiz_feature_update() what the quiz difficulty was
            #state: if player "won" the quiz then state == "won" if attempts == MaxAttempts then state == TryAgain
    quiz_question = 0
    current_lvl = quiz_hard_data['QuizFeature']['CurrentLvl']
    ui_proxy = quiz_hard_data[current_lvl]['quiz']
    print ui_proxy
    for answers in quiz_hard_data[current_lvl]['answers']:
        while (1 + 1) == 2:
            if quiz_hard_data['QuizFeature']['attempts'] < quiz_hard_data['QuizFeature']['MaxAttempts']:
                input_holder = raw_input("Please fill in " + quiz_hard_data[current_lvl]["ReplaceKey"][quiz_question] + " ")
                if input_holder == answers:
                    quiz_question += 1
                    ui_proxy = ui_proxy.replace(quiz_hard_data[current_lvl]["ReplaceKey"][quiz_question-1],answers)
                    print ui_proxy
                    print random_ui_words("winner") #18
                    break
                quiz_hard_data['QuizFeature']['attempts'] = quiz_hard_data['QuizFeature']['attempts'] +1;
                print "Are you even human?.. You have",5 - quiz_hard_data['QuizFeature']['attempts'], "attempts left"
            else:
                return  quiz_feature_update("hard","TryAgain")
    return quiz_feature_update("hard","win")

def quiz_i():
    #Behavior:
        #Runs the insane quiz using the current level value in quiz_insane_data['QuizFeature']['CurrentLvl']
    #returns:
        #provides quiz_feature_update() with two arguments.
            #difficulty: tells quiz_feature_update() what the quiz difficulty was
            #state: if player "won" the quiz then state == "won" if attempts == MaxAttempts then state == TryAgain
    quiz_question = 0
    current_lvl = quiz_insane_data['QuizFeature']['CurrentLvl']
    ui_proxy = quiz_insane_data[current_lvl]['quiz']
    print ui_proxy
    for answers in quiz_insane_data[current_lvl]['answers']: #these answers are less strict, need this because the answers in the insane quiz are short and ui breaks replacing blanks.
        while (1 + 1) == 2:
            if quiz_insane_data['QuizFeature']['attempts'] < quiz_insane_data['QuizFeature']['MaxAttempts']:
                input_holder = raw_input("Please fill in " + quiz_insane_data[current_lvl]["ReplaceKey"][quiz_question] + " ")
                if input_holder in answers:
                    quiz_question += 1
                    ui_proxy = ui_proxy.replace(quiz_insane_data[current_lvl]["ReplaceKey"][quiz_question-1],answers)
                    print ui_proxy
                    print random_ui_words("winner") #18
                    break
                quiz_insane_data['QuizFeature']['attempts'] = quiz_insane_data['QuizFeature']['attempts'] +1;
                print "Are you even human?.. You have",5 - quiz_insane_data['QuizFeature']['attempts'], "attempts left"
            else:
                return quiz_feature_update("insane","TryAgain")
    return quiz_feature_update("insane","win")

def alldonecheck():
    #Behavior:
        #Checks if all content the has been complete
    #returns:
        #True or False
    if quiz_easy_data['QuizFeature']['CurrentLvl'] > len(quiz_easy_data):
        if quiz_medium_data['QuizFeature']['CurrentLvl'] > len(quiz_medium_data):
            if quiz_hard_data['QuizFeature']['CurrentLvl'] > len(quiz_hard_data):
                if quiz_insane_datadata['QuizFeature']['CurrentLvl'] > len(quiz_insane_data):
                    return True
    return False

def quiz_runner(diff):
    #Args:
        #1:The difficulty matching users input from the_quiz()
    #Behavior:
        #selects the quiz to run matching player input
    #returns:
        #runs the quiz matching target difficulty
    if diff == "easy" and quiz_easy_data['QuizFeature']['CurrentLvl'] < len(quiz_easy_data):
        return quiz_e()
    if diff == "medium"and quiz_easy_data['QuizFeature']['CurrentLvl'] < len(quiz_medium_data):
        return quiz_m()
    if diff == "hard"and quiz_hard_data['QuizFeature']['CurrentLvl'] < len(quiz_hard_data):
        return quiz_h()
    if diff == "insane"and quiz_insane_data['QuizFeature']['CurrentLvl'] < len(quiz_insane_data):
        return quiz_i()
    return the_quiz("win")

def input_check(player_input):
    #Args:
        #player_input:this is what the player typed attempting to quit/select a difficulty.
    #Behavior:
        #allows for variants in the users input.
            #eg quit can be players input in the string: "    q Q quit QUIT exit EXIT Quit"
    #returns:
        # returns the string representing a difficulty or quit attempt.
            #if players input doesn't match any answer_variants[] the string "InputError" gets returned.

    if quiz_select['AnswerVariants']['easy'].find(player_input) >= 2:
        return "easy"
    if quiz_select['AnswerVariants']['medium'].find(player_input) >= 2:
        if player_input != "i": #this allows the use of "i" for insane difficulty.
            return "medium"
    if quiz_select['AnswerVariants']['hard'].find(player_input) >= 2:
        return "hard"
    if quiz_select['AnswerVariants']['insane'].find(player_input) >= 2:
        return "insane"
    if quiz_select['AnswerVariants']['quit'].find(player_input) >= 2:
        return "quit"
    return "InputError"

def quiz_state_message(state):
    #Args:
        #state:is user:
            #starting brand new? "new"
            #has player failed something? "new"
            #has player won something? "winner"
    #Behavior:
        #used to deliver alternative/random messages based on-
            #the player's current progress
    #returns:
        # a string representing the player's last actions/progress
    if state == "new":
        return random_ui_words("greetings")
    if state == "TryAgain":
        return "__ -- Try Again!!-- __"
    if state == "win":
        return random_ui_words("winner")

def the_quiz(state):
    #Args: #########  quiz_select['AnswerVariants']['quiz_select_ui']
        #state:has user:
            #started new? "new"
            #failed something? "new"
            #won something? "winner"
    #Behavior:
        #displays the quiz_select_ui and asks player to,
            #type out a difficulty and select a quiz or quit
    #returns:
        #uses player's input to start the appropriate quiz difficulty with quiz_runner(correct_game_option) or quits
        #if the input was invalid returns the_quiz('TryAgain') for new input.
    quiz_printer()
    print quiz_state_message(state)
    correct_game_option = input_check(raw_input("Please type in a difficulty: ")) #asks for player input then checks if valid with input_check()
    if alldonecheck():
        print "You Win!!"*9001
        print " You got max ", mega_points[0], " Mega points!!"
        return
    if correct_game_option in quiz_select['AnswerVariants']:
        if correct_game_option == "quit": #checks if the input was player wanting to quit,  if not assumes a mistake is made in input and returns quiz again for another go.
            print "Thanks for quitting, I knew you couldn't finish! HAHAHAHA!!!"
            return ui_tweak("MegaPoints999")
        quiz_runner(correct_game_option)
    if correct_game_option == "InputError":
        the_quiz("TryAgain")
    the_quiz('new')

the_quiz('new')
