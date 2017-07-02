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
