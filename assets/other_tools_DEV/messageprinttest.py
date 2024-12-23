with open("assets/text_lines/ASCII/startup_ASCII_1.txt") as f: # The with keyword automatically closes the file when you are done
    print(f.read())
    f.close()