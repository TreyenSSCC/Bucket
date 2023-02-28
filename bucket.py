# Version 0.0.4 - 2/28/2023 5:48 PM

syntax = ["AND", "OR", "IF", "ELSE", "PRINT", "VAR", "WHILE"]
# The syntax list will contain all of the syntax for Bucket.


def Bucket():# This is the main function of the program. This is where Bucket will perform most of it's tasks.
    code_line = 0
    while True:
        code_line+=1
        print(code_line, ": ", sep="", end="")
        user_code = input("")

Bucket()