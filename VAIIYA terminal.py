
import time
import os
from prompt_toolkit.shortcuts import ProgressBar
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit import prompt
from prompt_toolkit.shortcuts import message_dialog
from prompt_toolkit.shortcuts import yes_no_dialog
from prompt_toolkit.shortcuts import input_dialog
import time
import bcrypt
from datetime import datetime
from prompt_toolkit import print_formatted_text, HTML
import random
import tkinter.messagebox 
import sys
#changes the size of the Command prompt so it is easier to read (and that the ASCII doesnt soft wrap)
#from ctypes import wintypes
#from ctypes import windll, byref
#from ctypes.wintypes import SMALL_RECT    



#this idea was requested by Smashel on issue #30. 
#default value is 1-5650
#if it somehow gets that number the ascii will "corrupt" and use an alt
def startup_screen_ascii_roll():
    corrupted_ascii_roll = random.randint(1,5650)
    #normal value for this var is 3479
    if corrupted_ascii_roll == 3479:
        corrupted_ascii_startup_screen()

    else:
        norm_startup_screen_ASCII()

#if the number is rolled correctly, then this ASCII will play instead of the norm. 
def corrupted_ascii_startup_screen():
    with open("assets/text_lines/ASCII/startup_corrupted_ASCII_1.txt") as f: # The with keyword automatically closes the file when you are done
        print(f.read())
        f.close()



#NOTE: THERE MAY BE MINOR LINE WRAP IN THE ASCII

# Loading screen with VAIIYA SECURITY ASCII Art
def norm_startup_screen_ASCII():
    with open("assets/text_lines/ASCII/startup_ASCII_1.txt") as f: # The with keyword automatically closes the file when you are done
        print(f.read())
        f.close()


#title stuff for new loading screen 
#BEHAVIOR NOTE: THE PROMPT TK LOADINGBARS CANNOT GO OVER .01 FLOAT FOR SOME REASON! (thanks smashel for the idea, but was unable to make it happen)
def loading_bars_intro_1():

    title = HTML('Connecting to the VAIIYA Defender framework....')
    label = HTML('')

    # loading screen system with prompTK
    with ProgressBar(title=title) as pb:
        for i in pb(range(300), label=label):
            time.sleep(.01)
    time.sleep(.01)
    
    print("connection: approved")
    time.sleep(0.3)

def loading_bars_intro_2():

    title = HTML('Checking root for verification codes....')
    label = HTML('')

    # loading screen system with prompTK
    with ProgressBar(title=title) as pb:
        for i in pb(range(215), label=label):
            time.sleep(.01)
    time.sleep(1)
    #generates a 5 digit number from 0-9
    securecodestartup1 = random.randint(0,9)
    securecodestartup2 = random.randint(0,9)
    securecodestartup3 = random.randint(0,9)
    securecodestartup4 = random.randint(0,9) 
    securecodestartup5 = random.randint(0,9)

    print('Codes found! code is:')
    time.sleep(1.5)
    #prints that generated number
    print(securecodestartup1,securecodestartup2,securecodestartup3,securecodestartup4,securecodestartup5)
    print("checking.... system expected code is:")
    time.sleep(1.5)
    print(securecodestartup1,securecodestartup2,securecodestartup3,securecodestartup4,securecodestartup5)
    time.sleep(2)
    print("code approved! moving on...")
    #a cool lil thing for a secure startup! 
    

def loading_bars_intro_3():

    title = HTML('Sending system logs and debug info for system approval')
    label = HTML('')

    # loading screen system with prompTK
    with ProgressBar(title=title) as pb:
        for i in pb(range(175), label=label):
            time.sleep(.01)
    time.sleep(1)
    
    print("sending logs.... approved! sending debug... approved! ")
    time.sleep(0.3)
    
    
    print("All connections approved! opening VAIIYA terminal....")
    time.sleep(0.7)

# Display main menu
def main_menu():
   with open("assets/text_lines/ASCII/startup_ASCII_2login.txt") as f: # The with keyword automatically closes the file when you are done
        print(f.read())
        f.close()

def message_of_the_day(): #or per boot 
    print("|")
    print("The message of the day is: ")
    print("|") 
    #picks a random number, each value (depending on how many messages) will have a number. 
    MOTD = random.randint(1,6)

    if MOTD == 1: 
        with open("assets/text_lines/MOTD/MOTD_1.txt") as f: # The with keyword automatically closes the file when you are done
            print(f.read())
            f.close()
    
    elif MOTD == 2: 
        with open("assets/text_lines/MOTD/MOTD_2.txt") as f: # The with keyword automatically closes the file when you are done
            print(f.read())
            f.close()

    elif MOTD == 3:
        with open("assets/text_lines/MOTD/MOTD_3.txt") as f: # The with keyword automatically closes the file when you are done
            print(f.read())
            f.close()

    elif MOTD == 4:
        with open("assets/text_lines/MOTD/MOTD_4.txt") as f: # The with keyword automatically closes the file when you are done
            print(f.read())
            f.close()

    elif MOTD == 5:
        with open("assets/text_lines/MOTD/MOTD_5.txt") as f: # The with keyword automatically closes the file when you are done
            print(f.read())
            f.close()

    #remove this MOTD on the next update PAST christmas, maybe new years or when the snow melts. 
    elif MOTD == 6:
        with open("assets/text_lines/MOTD/MOTD_xmas.txt") as f: # The with keyword automatically closes the file when you are done
            print(f.read())
            f.close()

    elif MOTD == 7:
        with open("assets/text_lines/MOTD/MOTD_6.txt") as f: # The with keyword automatically closes the file when you are done
            print(f.read())
            f.close()

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
            with open("assets/text_lines/commands_lines/line_credits.txt") as f: # The with keyword automatically closes the file when you are done
                print(f.read())
                f.close()

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
            with open("assets/text_lines/commands_lines/line_commands.txt") as f: # The with keyword automatically closes the file when you are done
                print(f.read())
                f.close()            


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
            print("VAIIYA Engine did not detect that as a valid command.")
            print("please check spelling, spaces, or other. or use 'commands'")

# PLEASE PUT ALL 2ND DEF(S) BELOW THIS NOTE! 

#MAKE SURE THIS IS DISABLED BEFORE RELEASE!!! 
def DEBUG_COMMANDLINE():
    if DEBUG_ENABLE() == True:

        while True:
            text = prompt('DEBUG COMMANDLINE >>> ')        

            if text == 'VRRALSA':
                VRRALSA_startup()

            elif text == 'WALKER':
                walker_entered()

            elif text == 'FROST':
                frostbyte_entered()

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
    if DEBUG_ENABLE() == False:
        print("hahaha good try (￣y▽,￣)╭ ")



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
         raise SystemExit
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
         raise SystemExit
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

#BELOW IS THE DEBUG COMMANDLINE ENABLE, SET TO TRUE FOR IT TO WORK.  FALSE FOR RELEASE
def DEBUG_ENABLE():
    return True

def DEBUG_STARTUP_DISABLE():
    return True

def STARTUP_DEBUG_CHECK():
    if DEBUG_STARTUP_DISABLE() == False:
        startup_screen_ascii_roll()
        loading_bars_combined_startup()
    
    if DEBUG_STARTUP_DISABLE() == True:
        pass


def terminal_startup_combined():
    main_menu()
    message_of_the_day()
    timefetch()
    terminal_start_message()
    open_terminal()

def loading_bars_combined_startup():
    loading_bars_intro_1()
    loading_bars_intro_2()
    loading_bars_intro_3()

# Main system loop
def game_loop():
    STARTUP_DEBUG_CHECK()
    terminal_startup_combined()
    
    while True:
        #there is no code to run right before startup so there is a `pass` here. 
            pass

# Start the game
game_loop()

#this func is not required for the operation of the program, so it is disabled.
#if __name__ == "__main__":
#        main()




#VRRALSA notes 
# employee#4972 or herbert does not like greg. (⊙_⊙)？
