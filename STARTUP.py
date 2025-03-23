import random
import time
#BARS STUFF BELOW
from alive_progress import alive_bar
# ASCIIMATICS STUFF BELOW
from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen

#NOTE: THIS FILE IS TO BE CALLED INTO VAIIYA_terminal.py. 
# only asciimatics and the other startup stuff IS TO BE CALLED!!!



# a settings translator that will define the type of ASCIIMATICS view. like a DEBUG ver or the normal one! 
def MAINCALL(runtype='default'):

    #use THIS runtype when publishing VAIIYA terminal. 
    if runtype == 'default':
        STARTUP_PATH.DEFAULT()

    if runtype == 'ASCIIMATICS_TESTING_1':
        STARTUP_PATH.ASCIIMATICS_TESTING_1()

    if runtype == 'BARS_ONLY':
        STARTUP_PATH.BARS_ONLY()


# this is a set of follow paths for the above settings system to use^^ 
class STARTUP_PATH():

    def DEFAULT():
        pass

    def ASCIIMATICS_TESTING_1():
        STARTUP_PARTS.ASCIIMATICS.ASCIIMATICS_1()
    
    def BARS_ONLY():
        STARTUP_PARTS.BAR.bar_interpreter_prep() # 1 in the list of bars
        time.sleep(.2)
        print("VAIIYAkernel loaded without issues. continuing...")
        time.sleep(.2)
        STARTUP_PARTS.BAR.bar_1() # 2 in the list of bars. 
        STARTUP_PARTS.BAR.bar_2() # 3 in the list of bars
        STARTUP_PARTS.BAR.bar_3()
        STARTUP_PARTS.BAR.bar_4()
        STARTUP_PARTS.BAR.bar_5()

# this is the RAW startup parts, later to be organized in the startup paths
class STARTUP_PARTS():
    
    # contains all the different BARs 
    class BAR():

        def bar_1():
            with alive_bar(title="loading binary assets...",monitor=False ,stats=False,elapsed=False,elapsed_end="Done!",stats_end=False, bar=None, spinner='classic') as bar:
                    for i in range(rangerandom1):
                        time.sleep(.005)
                        bar()

        def bar_2():
            with alive_bar( rangerandom2,title="Checking system(s) security integrity...",stats='ETA: {eta}', monitor=False,elapsed=False,elapsed_end='Done!',stats_end=False, bar=None, spinner='classic') as bar:
                    for i in range(rangerandom2):
                        time.sleep(.005)
                        bar()
    
        def bar_interpreter_prep():
            with alive_bar(title="VAIIYAkernel is warming up, please wait...", monitor=False, stats=False, elapsed=False,elapsed_end='Done!',stats_end=False, bar=None, spinner='classic') as bar:
                    for i in range(rangerandom3):
                        time.sleep(.005)
                        bar()
                        

        def bar_5():
            with alive_bar(rangerandom4, title="prepping to send package for VAIIYAlink connection...", monitor=False ,stats='ETA: {eta}',elapsed='Time elapsed: {elapsed}',elapsed_end='Task was done in {elapsed}',stats_end=False) as bar: #NOTE bar shi is broken asf, cant get that unknown to work, and cant change the style without it going left to right. not back and forth like i want.
                    for i in range(rangerandom4):
                        time.sleep(.005)
                        bar()
                        

        def bar_3():
            with alive_bar(title="sending, please wait...", monitor=False, stats=False, elapsed='Time elapsed: {elapsed}',elapsed_end='Task was done in {elapsed}',stats_end=False) as bar:
                    for i in range(rangerandom5):
                        time.sleep(.005)
                        bar()
        # this bar will play the back and forth animation
        def bar_4():
            with alive_bar(title="requesting a VAIIYAlink systems connection and security-check dump...", monitor=False, stats=False,elapsed='Time elapsed: {elapsed}',elapsed_end='Task was done in {elapsed}',stats_end=False, bar='checks') as bar:
                    for i in range(rangerandom6):
                        time.sleep(.005)
                        bar()


    class code_letterizor():

        # the code letterizor is a "startup module" that makes a set of 6, 2 digit codes with letters and numbers.
        # example: 1A--B2--C3--4D--E5--F6 but randomized.

        time.sleep(0.06)
        
        def coinflip_1(numberset_1):
            match numberset_1:
                #num-ltr
                case 1:
                    return rand_numb1A, rand_letter1A
                    #ltr-num 
                case 2:
                    return rand_letter1A, rand_numb1A
                    #ltr-ltr
                case 3:
                    return rand_letter1A, rand_letter1B
                #num-num
                case 4:
                    return rand_numb1B, rand_numb1A

        def coinflip_2(numberset_2):
            match numberset_2:
                case 1:
                    return rand_numb2A, rand_letter2A
                    #ltr-num 
                case 2:
                    return rand_letter2A, rand_numb2A
                    #ltr-ltr
                case 3:
                    return rand_letter2A, rand_letter2B
                #num-num
                case 4:
                    return rand_numb2B, rand_numb2A
        def coinflip_3(numberset_3):
            match numberset_3:
                case 1:
                    return rand_numb3A, rand_letter3A
                # ltr-num
                case 2:
                    return rand_letter3A, rand_numb3A
                # ltr-ltr
                case 3:
                    return rand_letter3A, rand_letter3B
                            # num-num
                case 4:
                    return rand_numb3B, rand_numb3A

        def coinflip_4(numberset_4):
            match numberset_4:
                case 1:
                    return rand_numb4A, rand_letter4A
                    #ltr-num 
                case 2:
                    return rand_letter4A, rand_numb4A
                    #ltr-ltr
                case 3:
                    return rand_letter4A, rand_letter4B
                #num-num
                case 4:
                    return rand_numb4B, rand_numb4A

        def coinflip_5(numberset_5):
            match numberset_5:
                case 1:
                    return rand_numb5A, rand_letter5A
                    #ltr-num 
                case 2:
                    return rand_letter5A, rand_numb5A
                    #ltr-ltr
                case 3:
                    return rand_letter5A, rand_letter5B
                #num-num
                case 4:
                    return rand_numb5B, rand_numb5A

        def coinflip_6(numberset_6):
            match numberset_6:
                case 1:
                    return rand_numb6A, rand_letter6A
                    #ltr-num 
                case 2:
                    return rand_letter6A, rand_numb6A
                    #ltr-ltr
                case 3:
                    return rand_letter6A, rand_letter6B
                #num-num
                case 4:
                    return rand_numb6B, rand_numb6A

        def _return_codesets():
            print(numberset_1,"-",numberset_2,"-",numberset_3,"-",numberset_4,"-",numberset_5,"-",numberset_6)

    def module_randomizer():
        #this part randomizes the order of all the "modules"
        seen_list = []
        random.seed()
        module_randpickees = ["SYSTEM: IBM CONFIRMED compute drivers A7c version 2.3.11",
                                "module: V.A.N. NETWORK DRIVER A7B9 version 0.3.11 ",
                                "module: printfile system custom A4c version 1.2.19 ",
                                "module: time and server sync systems X93B version 7.0.9",
                                "module: VAIIYAlink interruption resolver and re-connector V43Z version 2.20.2",
                                "tool: VAIIYAlink activity monitor Z28B version 3.21",
                                "application: VAIIYAtools user experience enhancer G10D version 1.4.1",
                                "SYSTEM: VAIIYAkernel runtime local V6.2.1",]
        
        while True:
            time.sleep(rand_moduledelay)
            
            if len(seen_list) == len(module_randpickees): 
                break

            n = random.randrange(len(module_randpickees))

            try:
                seen_list.index(n)
                continue

            except ValueError:
                    pass

            print(module_randpickees[n])
            seen_list.append(n)

# MOVE INTO `.\assets\ASCIIMATICS\ASCIIMATICS.py` mr future T3 \(￣︶￣*\))
    class ASCIIMATICS():
    
        def ASCIIMATICS_1(screen):
            while True:
                effects = [
                    Cycle(
                        screen,
                        FigletText("VAIIYA IS THE", font='big'),
                        int(screen.height / 2 - 8)),
                    Cycle(
                        screen,
                        FigletText("BEST!", font='standard'),
                        int(screen.height / 2 + 3)),
                    Stars(screen, 200)
                ]
                screen.play([Scene(effects, 500)])

        Screen.wrapper(ASCIIMATICS_1)


# VALUES

# number randomizer for the code letterizor
rand_numb1A = random.randint(0, 9)
rand_numb1B = random.randint(0, 9)
rand_numb2A = random.randint(0, 9)
rand_numb2B = random.randint(0, 9)
rand_numb3A = random.randint(0, 9)
rand_numb3B = random.randint(0, 9)
rand_numb4A = random.randint(0, 9)
rand_numb4B = random.randint(0, 9)
rand_numb5A = random.randint(0, 9)
rand_numb5B = random.randint(0, 9)
rand_numb6A = random.randint(0, 9)
rand_numb6B = random.randint(0, 9)

# letter randomizer for the code letterizor
rand_letter1A = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
rand_letter1B = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
rand_letter2A = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
rand_letter2B = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
rand_letter3A = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
rand_letter3B = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
rand_letter4A = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
rand_letter4B = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
rand_letter5A = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
rand_letter5B = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
rand_letter6A = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
rand_letter6B = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

# the coinflip modules for the randomizer
coinflip1 = random.randint(0, 3)
coinflip2 = random.randint(0, 3)
coinflip3 = random.randint(0, 3)
coinflip4 = random.randint(0, 3)
coinflip5 = random.randint(0, 3)
coinflip6 = random.randint(0, 3)

# randomized the print delay in the listing for the modules.
rand_moduledelay = random.uniform(0.14, 0.07)

# this randomizes the length of all the bars 
rangerandom1 = random.randint(300, 800)
rangerandom2 = random.randint(300, 800)
rangerandom3 = random.randint(300, 800)
rangerandom4 = random.randint(300, 800)
rangerandom5 = random.randint(300, 800)
rangerandom6 = random.randint(300, 800)
rangerandom_headstartbar = random.randint(200, 670)