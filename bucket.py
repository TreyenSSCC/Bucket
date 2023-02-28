# Version 0.0.5 - 2/28/2023 6:13 PM

syntax = ["and", "or", "if", "else", "print", "var", "while"]
# The syntax list will contain all of the syntax for Bucket.


def Bucket():# This is the main function of the program. This is where Bucket will perform most of it's tasks.
    code_line = 0
    while True:
        code_line+=1
        print(code_line, ": ", sep="", end="")
        user_code = input("").lower()
        if (user_code==("quit") or user_code=="exit"):
            break

Bucket()