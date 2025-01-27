import time # basic tool imports here used a lot
import os
import sys
import random
import prompt_toolkit
from prompt_toolkit.shortcuts import ProgressBar
from prompt_toolkit.formatted_text import HTML # really good for colored text
from prompt_toolkit import prompt #general CMD prompts (NOT THE POPUPS)
from prompt_toolkit.shortcuts import message_dialog
from prompt_toolkit.shortcuts import yes_no_dialog
from prompt_toolkit.shortcuts import input_dialog
import bcrypt # bcrypt is used for the password thingys 
from datetime import datetime
from prompt_toolkit import print_formatted_text, HTML
import tkinter.messagebox # the windows popup controller
from alive_progress import alive_bar #replacement loading bars that look wayyyyy better :> 
from alive_progress.styles import showtime, Show


def headstart():
# ATTENTION!! READ THIS BEFORE YOU DO SOME SHI 
# the headstart def is the MAIN STARTUP DEF AND IS USED TO MAKE THE MAIN STARTUP ILLUSION!!

    # start of the startup
    time.sleep(0.20)
    startup_func.bar_interpreter_prep()
    time.sleep(0.6)
    print("program open and ready for run, please wait")
    time.sleep(0.20)
    startup_func.bar_1()
    time.sleep(.1)
    print("loading system modules...")
    time.sleep(0.45)
    # MODULE RANDOR LISTER
    startup_func.module_randor()
    time.sleep(0.30)
    startup_func.bar_2()
    time.sleep(0.30)
    startup_func.bar_3()
    time.sleep(0.39)
    startup_func.bar_4()
    time.sleep(0.37)
    startup_func.bar_5()
    time.sleep(0.30)
    print("access approved")




    


class startup_func():
# NOTE  
# the `alive_bar` is a replacement for the `ProgressBar` from the `prompt_toolkit.shortcuts` module. < that was the github AI thingy did that hahaha 
# the `alive_bar` is a lot better and has a lot more features than the `ProgressBar` from the `prompt_toolkit.shortcuts` module.
# 
# 
# 

    def bar_1():
        with alive_bar(title="prepping to load system assets...",monitor=False ,stats=False,elapsed='Time elapsed: {elapsed}',elapsed_end='Task was done in {elapsed}',stats_end=False) as bar:
                    for i in range(rangerandom1):
                        time.sleep(.005)
                        bar()

    def bar_2():
        with alive_bar( rangerandom2,title="Compiling assets...",stats='ETA: {eta}', monitor=False,elapsed='Time elapsed: {elapsed}',elapsed_end='Task was done in {elapsed}',stats_end=False) as bar:
                    for i in range(rangerandom2):
                        time.sleep(.005)
                        bar()       
    
    def bar_interpreter_prep():
        with alive_bar(rangerandom3, title="pre-loading and prepping the interpreter", monitor=False, stats='ETA: {eta}',elapsed='Time elapsed: {elapsed}',elapsed_end='Task was done in {elapsed}',stats_end=False) as bar:
                    for i in range(rangerandom3):
                        time.sleep(.005)
                        bar() 

    def bar_3():
        with alive_bar(rangerandom4, title="prepping to send package for VAIIYA system(s) connections...", monitor=False ,stats='ETA: {eta}',elapsed='Time elapsed: {elapsed}',elapsed_end='Task was done in {elapsed}',stats_end=False) as bar: #NOTE bar shi is broken asf, cant get that unknown to work, and cant change the style without it going left to right. not back and forth like i want.
                    for i in range(rangerandom4):
                        time.sleep(.005)
                        bar() 

    def bar_4():
        with alive_bar(rangerandom5, title="sending, please wait...", monitor=False, stats='ETA: {eta}',elapsed='Time elapsed: {elapsed}',elapsed_end='Task was done in {elapsed}',stats_end=False) as bar:
                    for i in range(rangerandom5):
                        time.sleep(.005)
                        bar() 
# this bar will play the back and forth animation
    def bar_5():
        with alive_bar(title="requesting system access...", monitor=False, stats=False,elapsed='Time elapsed: {elapsed}',elapsed_end='Task was done in {elapsed}',stats_end=False) as bar:
                    for i in range(rangerandom6):
                        time.sleep(.005)
                        bar() 

    def module_randor():
        #this part randomizes the order of all the "modules"
        seen_list = []
        random.seed()
        module_randpickees = ["module: compute module A7c version 2.3.11",
                                "module: V.A.N. NETWORK DRIVER A7B9 version 0.3.11 ",
                                "module: printfile system custom A4c version 1.2.19 ",
                                "module: time and server sync systems X93B version 7.0.9",
                                "module: interruption resolver and re-connector V43Z version 2.20.2"]
        
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

# randomized the print delay in the listing for the modules.
rand_moduledelay = random.uniform(0.2, 0.10)

# this randomizes the length of all the bars 
rangerandom1 = random.randint(300, 800)
rangerandom2 = random.randint(300, 800)
rangerandom3 = random.randint(300, 800)
rangerandom4 = random.randint(300, 800)
rangerandom5 = random.randint(300, 800)
rangerandom6 = random.randint(300, 800)
         







# Display main menu
def main_menu():
    game.printfile("assets/text_lines/ASCII/startup_ASCII_2login.txt")


def timefetch():
#time fetch for login
    curtime = datetime.now().strftime('%H:%M:%S') 
    curdate = datetime.now().strftime('%Y-%m-%d')
    print("|")
    print("""|""")
    print('Welcome VAIIYA trustee! the time is: ',curtime)
    print('and the date is: ',curdate)
    print("have a wonderful CHRISTMAS day at VAIIYA Technologies LLC!")
    print("""|""")

#this is here so that this doesnt dupe every time the commandline reprints. it now only happens once.
def terminal_start_message():
    print(" for a list of commands, please type 'commands' ")
    print("""|""")
 
    
#TERMINAL BEHAVIOR NOTES! make sure to use `elif` instead of `if`. this will prevent the error string from printing if we return from the EEs or logins.
#ANOTHER NOTE: exit() AND quit() COUNT AS DEBUGGING, SO A TRACKBACK WILL CALL. USE `raise SystemExit` FROM NOW ON!
#
#notes here^^^

#Starts the TERMINAL and its commands
def open_terminal():

    while True:
        
        text = prompt('awaiting command(s)>>> ')
#put all the usercommands under here please! 
        #this is the FIRST `if`, replace and all new should be `elif`.
        if text == 'T342':
            print('hey thanks for saying something!')
            continue
#this is BELOW the first command. put `elif` on all new commands.

        #the credits for the game! 
        elif text == 'credits':
            game.printfile("assets/text_lines/commands_lines/line_credits.txt")

        elif text == 'version':
            print("|")
            print("VAIIYA Terminal Engine version 24.39-overhaul_8")
            print("detected operating device: IBM 5150 VAIIYA secure system fitted.")
            print("OS system detected: MuCoDOS V27.592 private")
            print("VAIIYA Terminal release V11")
            print("|")
            #the link given will NEVER EXPIRE
        elif text == 'discord':
            print("""|""")
            print(" the invite link to The VAIIYA Hub and VAIIYA Terminal news!: https://discord.gg/Qt5Je9sFE5 ")
            print("""|""")
            


        elif text == 'CNS':
            print("CNS_VAIIYA_BYPASS_V4.567.EXE EXECUTING....")
            time.sleep(2)
            CNS_EE_HAKED()
        
        
        #walkers login, requires password. this will print the following, stop for 3 secs and then runs the `walker_login()`.
        elif text == 'walker':
            print("Welcome walker to your login! Please wait while your coffee brews.......")
            time.sleep(3)
            walker_login()

        #the `no-command bug has been resolved.` 
        # FROST EE WIP!! 
        elif text == 'frostbyte':
            print("Welcome frostbyte to your login! Please wait while I startup the supercomputer and freeze these bytes!....")
            time.sleep(3)
            #enters the frostbyte EE
            frostbyte_login()


#below are all the non-user commands, DO NOT REMOVE!



        #BELOW IS THE DEBUG COMMANDLINE, DO NOT LEAVE ON FOR RELEASE!     
        elif text == 'DEBUG':
            DEBUG_COMMANDLINE()


            #the COMMANDS directory, DO NOT REMOVE!
        elif text == 'commands':
            game.printfile("assets/text_lines/commands_lines/line_commands.txt")


        #this solves the space command issue. leave blank    
        elif text == '':
            continue

            #the EXIT command, DO NOT REMOVE!! 
        elif text == 'exit':
            print('exiting the terminal... have a nice day!')
            time.sleep(0.5)
            raise SystemExit 
        
        #error response
        else:
            game_errs.Vengine_nocmd_found()

# PLEASE PUT ALL 2ND DEF(S) BELOW THIS NOTE! 

#MAKE SURE THIS IS DISABLED BEFORE RELEASE!!! 
def DEBUG_COMMANDLINE():
    if DEVsettings.DEBUG_ENABLE() == True:

        while True:
            text = prompt('DEBUG COMMANDLINE >>> ')        

            if text == 'VRRALSA':
                VRRALSA_startup()

            elif text == 'WALKER':
                walker_entered()

            elif text == 'FROST':
                frostbyte_entered()
            
            elif text == 'SHOWTIME':
                showtime()

            elif text == 'BAR': 
                with alive_bar(title="TESTING THE BARS!! noice") as bar:
                    for i in range(1000):
                        time.sleep(.005)
                        bar()
            
            elif text == 'SHOWTIMEBARS':
                 showtime(Show.BARS)

            elif text == 'SHOWTIMETHEMES':
                 showtime(Show.THEMES)

            elif text == 'TYPE':
                pass

            elif text == 'COMMANDS':
                print("commands:")
                print("VRRALSA")
                print("WALKER")
                print("FROST")
                print("EXIT")
                
            elif text == 'EXIT':
                break

            else:
                print("use COMMANDS if you forgot")
    if DEVsettings.DEBUG_ENABLE() == False:
        game_errs.debug_disabled()



#PUT ALL FUNC DEFS BELOW HERE! 
# the CNS EE below this message
def CNS_EE_HAKED():
    #below is the Y/N prompt for CNS, and the following `result` can be split into a bool and set as True or False
    result = yes_no_dialog(
    title='CNS.02.06.01',
    text='dO yOU wAnT ThE tRUTh?').run()
    #if the `result` has a bool of True, it will run this part of the code. 
    if result == True:
         message_dialog(
    title='CNS.02.06.01',
    text='very well then, we will see you soon enough').run()
         #then after it returns to the main menu and exits the program.
         print("VAIIYA DEFENDER ENGINE CRITICAL FAILURE!: THE VAIIYA DEFENDER ENGINE HAS FOUND A BREACH AND WILL NOW FORCE QUIT THE PROGRAM")
         print("""|""")
         print("THE PROGRAM WILL SHUTDOWN IN:")
         time.sleep(1)
         print("3")
         time.sleep(1)
         print("2")
         time.sleep(1)
         print("1")
         time.sleep(1)
         game.quit()
    #if the `result` has a bool of False, then it will run this part of code. and again will return to menu and exit the program. 
    if result == False:
         message_dialog(
    title='CNS.02.06.01',
    text='how disappointing, that you dont want tHe TrutH. we will see you soon enough').run()
         print("VAIIYA DEFENDER ENGINE CRITICAL FAILURE!: THE VAIIYA DEFENDER ENGINE HAS FOUND A BREACH AND WILL NOW FORCE QUIT THE PROGRAM")
         print("""|""")
         print("THE PROGRAM WILL SHUTDOWN IN:")
         time.sleep(1)
         print("3")
         time.sleep(1)
         print("2")
         time.sleep(1)
         print("1")
         time.sleep(1)
         game.quit()
#the idea above from smashel! 



#add passwords here for the logins and name the vars respectively.
# 
#the website for reference to the password system is https://www.geeksforgeeks.org/npm-bcrypt/   
#walkerpasswrd1
walkerhash = b'$2b$12$M7LXCClyfsnN9SjibtnEmuLEOlR68H2ovjCBA0zcAIBs2RHBzOnFy'
#frostEEpswrd1
frosthash = b'$2b$12$AUur7AKX1aGQurOlmM46Pu0OX9HXqx6UHH9SHiEvrCJM56JvUjYfu'


#walker login here
def walker_login():
    #when exiting the prompt with the `<cancel>`, the program will force-quit for some reason. 

    #password prompt; 
    userpassword = text = input_dialog(
    title='Walker password input',
    text='walker password:',
    password=True,
    ).run()
    #encodes the given password for compare
    userpassword = userpassword.encode('utf-8')

    #compare password hashes, if identical then "result" == True, then it will move onto walker_entered
    result = bcrypt.checkpw(userpassword, walkerhash)
    if result:
          walker_entered()
#end of walker password verify 


def walker_entered():
    
    print("|")
    print("|")
    print("use 'commands' for available commands")
    while True:
        text = prompt("system$walker>>> ")

        if text == 'commands':
            print("commands for sys$walker")
            print("command; VRRALSA")

        elif text == 'VRRALSA':
            VRRALSA_startup()
        
        elif text == 'exit':
            return
        
        else:
            print("that isnt a command. use 'commands'")

    



# FROST EE STUFF OVER HERE!
def frostbyte_login():
    userpassword = input_dialog(
    title='frostbyte password input',
    text='frostbyte password:',
    password=True,
    ).run()
    
    userpassword = userpassword.encode('utf-8')
               
    #compare password hashes
    result = bcrypt.checkpw(userpassword, frosthash)
    if result:
          frostbyte_entered()




# 2nd part to the FROST EE                     
def frostbyte_entered():
    
    #the following prompts from promptTK are for frost taking about UwU more and more ¯\_(ツ)_/¯
    message_dialog(
    title='VAIIYA Warning systems',
    text='VAIIYA TERMINAL WARNING AWAITING ATTENTION!').run()
    
    message_dialog(
    title='VAIIYA Warning systems',
    text='VAIIYA employee T342 has marked you as "requires careful observation and mental medical attention." thankyou for your cooperation.').run()

    message_dialog(
    title='VAIIYA Warning systems',
    text='thank you for your attention. you may continue your tasks and have a safe day!').run()
    
    print("|")
    print("|")
    print("use 'commands' for available") 
    
    while True:
        text = prompt('system$frostbyte>>> ')

        if text == 'commands':
            print("commands for sys$frostbyte ")
            print("command; VRRALSA")

        elif text == 'VRRALSA':
            VRRALSA_startup()
        
        elif text == 'exit':
            return

        else:
            print("that isnt a command. use 'commands'")
#END OF FROST EE CODE, 


#USER TEMPLATE HERE
            #print("|")
            #print("V.R.R.A.L.S.A. FINDING INQUIRY....")
            #time.sleep(1)
            #print("searching database... ")
            #time.sleep(1)
            #print("Record found!")
            #print("|")
            #print("citizen record; (name) ")
            #print("username=(DC username)")
            #print("user_traits= (any) ")
            #print("health_record_status=(True/false) current_records=## record_severity=(low/med/high) highest_alert=(any)")
            #print("end of file.")
            #print("|")














#RENAMED VRCL TO VAIIYA RESTRICTED RECORDS AND LOGS SYSTEM AUTOMATED. OR V.R.R.A.L.S.A.
#THE VRCL startup with the welcome message. this is so the welcome message clone does not happen again. 
def VRRALSA_startup():
    VRRALSA_welcome_message()
    VRRALSA_COMMAND_PANEL()

def VRRALSA_welcome_message():
    with open("assets/text_lines/VRRALSA_lines/VRRALSA_welcome.txt") as f: # The with keyword automatically closes the file when you are done
        print(f.read())
        f.close()

def VRRALSA_COMMAND_PANEL():
    
    while True:
        print("|") 
        VRRALSA_TEXT = prompt('V.R.R.A.L.S.A. awaiting command(s)>>>> ')

        if  VRRALSA_TEXT == 'test':
            print("VRRALSA has received the ping.")
        
        elif VRRALSA_TEXT == 'logs':
            with open("assets/text_lines/VRRALSA_lines/VRRALSA_commands/VRRALSA_logslist.txt") as f: # The with keyword automatically closes the file when you are done
                print(f.read())
                f.close()

        elif VRRALSA_TEXT == 'records':
            print("|")
            print("record; walker")
            print("record; frostbyte")
            print("record; violet ")
        #only the logs and records commands here! 


        elif VRRALSA_TEXT == 'violet':
            print("|")
            print("V.R.R.A.L.S.A. FINDING INQUIRY....")
            time.sleep(1)
            print("searching database... ")
            time.sleep(1)
            print("Record found!")
            print("|")
            with open("assets/text_lines/VRRALSA_lines/VRRALSA_records/VRRALSA_record_violet.txt") as f: # The with keyword automatically closes the file when you are done
                print(f.read())
                f.close()

        elif VRRALSA_TEXT == 'frostbyte':
            print("|")
            print("V.R.R.A.L.S.A. FINDING INQUIRY....")
            time.sleep(1)
            print("searching database... ")
            time.sleep(1)
            print("Record found!")
            print("|")
            with open("assets/text_lines/VRRALSA_lines/VRRALSA_records/VRRALSA_record_frostbyte.txt") as f: # The with keyword automatically closes the file when you are done
                print(f.read())
                f.close()            

        elif VRRALSA_TEXT == 'walker':
            print("|")
            print("V.R.R.A.L.S.A. FINDING INQUIRY....")
            time.sleep(1)
            print("searching database... ")
            time.sleep(1)
            print("Record found!")
            print("|")
            with open("assets/text_lines/VRRALSA_lines/VRRALSA_records/VRRALSA_record_walker.txt") as f: # The with keyword automatically closes the file when you are done
                print(f.read())
                f.close() 
        #please put all records above here
        #put all logs below here! 
        elif VRRALSA_TEXT == 'LOG_10079':
            print("|")
            print("V.R.R.A.L.S.A. FINDING INQUIRY....")
            time.sleep(1)
            print("searching database... ")
            time.sleep(1)
            print("Log Found!")
            print("|")
            with open("assets/text_lines/VRRALSA_lines/VRRALSA_logs/VRRALSA_log_10079.txt") as f: # The with keyword automatically closes the file when you are done
                print(f.read())
                f.close()

            print_formatted_text(HTML('<red>ERROR! LOG ENDED WITH CODE #570-A. ESTIMATED LOSS: 39% OF FILE LEFT.</red>'))
            print("End of log.")
        
        elif VRRALSA_TEXT == 'LOG_342': 
            print("|")
            print("V.R.R.A.L.S.A. FINDING INQUIRY....")
            time.sleep(1)
            print("searching database... ")
            time.sleep(1)
            print("Log Found!")
            print("|")
            with open("assets/text_lines/VRRALSA_lines/VRRALSA_logs/VRRALSA_log_342.txt") as f: # The with keyword automatically closes the file when you are done
                print(f.read())
                f.close()

        elif VRRALSA_TEXT == 'exit':
            return
        
        else: 
            print("|")
            print("V.R.C.L. ERROR; KEYWORD DOES NOT LINK TO RECORD OR LOG. CHECK SPELLING, CAPS, OR OTHER.")
#END OF THE VRCL COMMAND SYSTEM
class game:
    #the game class is for very often used tasks (eg the file printer)

    #make sure that the filepath is an actual filepath with "" otherwise it WILL break 
    def printfile(txtfilepath = ""):
        try:
            with open(txtfilepath) as f: # The with keyword automatically closes the file when you are done
                    print(f.read())
        except:
            print_formatted_text(HTML('<red>ERR! FILEPRINT FAILURE</red>'))
            

    #the game.quit() event is to make the rase systemexit look a bit better :3
    def quit():
        raise SystemExit



    


# setting are ova here dude 
class DEVsettings:

#BELOW IS THE DEBUG COMMANDLINE ENABLE, SET TO TRUE FOR IT TO WORK.  FALSE FOR RELEASE
    def DEBUG_ENABLE():
        return True #set to TRUE to enable the debug commandline 

    def DEBUG_STARTUP_DISABLE():
        return False  #set to TRUE to disable the startup part of VT

    def STARTUP_DEBUG_CHECK():
        if DEVsettings.DEBUG_STARTUP_DISABLE() == False:
            headstart()
    
        if DEVsettings.DEBUG_STARTUP_DISABLE() == True:
            pass

        
class DEVtools:

    def debug_enabled_reminder():
# a simple reminders system that the debug system is turned on 
        if DEVsettings.DEBUG_ENABLE() == True:
            print_formatted_text(HTML('<red>DEBUG MODE IS ENABLED</red>'))
    
        if DEVsettings.DEBUG_ENABLE() == False:
            pass
    
        if DEVsettings.DEBUG_STARTUP_DISABLE() == False:
            pass

        if DEVsettings.DEBUG_STARTUP_DISABLE() == True:
            print_formatted_text(HTML('<red>THE STARTUP IS DISABLED!!</red>'))


class startup_shortcuts:
    def terminal_startup_combined():
        main_menu()
        timefetch()
        terminal_start_message()
        DEVtools.debug_enabled_reminder()
        open_terminal()

class game_errs:

    def Vengine_nocmd_found():
        print("VAIIYA Engine did not detect that as a valid command.")
        print("please check spelling, spaces, or other. or use 'commands'")

    def debug_disabled():
        print("VAIIYA Engine did not detect a VAIIYA granted systems card.")
        print("If you are a VAIIYA employee, please contact your district supervisor for more info.")




# BELOW THIS NOTE IS ONLY RAISE ERRORS!!! DO NOT REMOVE ANY OF THIS!!!!! 
class this_broke:
    pass
# this class is for errors outside of normal use, like the file printer not finding the file

# class fileprintfail(FileNotFoundError):
# # this error is used to be user friendly, and debug friendly. while also giving it a keen eye
#     def __init__(self, *args):
#         super().__init__(*args)
        
#         try:
#             raise fileprintfail
#         except fileprintfail as e:
#             print_formatted_text(HTML('<red>ERR! FILEPRINT FAILURE</red>', e.strerror ))

    


# Main system loop
def game_loop():
    DEVsettings.STARTUP_DEBUG_CHECK()
    startup_shortcuts.terminal_startup_combined()
    
    while True:
        #there is no code to run right before startup so there is a `pass` here. 
            pass

# Start the game
game_loop()

#this func is not required for the operation of the program, so it is disabled.
# if __name__ == "__main__":
#     game_loop()




#VRRALSA notes 
# employee#4972 or herbert does not like greg. (⊙_⊙)？
