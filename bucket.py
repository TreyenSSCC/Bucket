# Version 0.0.6 - 3/13/2023 4:45 PM

syntax = ["and", "or", "if", "else", "print", "var", "while", "end of list"]
# The syntax list will contain all of the syntax for Bucket.


def Bucket():# This is the main function of the program. This is where Bucket will perform most of it's tasks.
    code_line = 0
    while True:
        x=0
        code_line+=1
        print(code_line, ": ", sep="", end="")
        user_code = input("").lower()
        if (user_code==("quit") or user_code=="exit"):
            break
        while(x<7): # Detects if the user entered any syntax.
            if(user_code==syntax[x]):
                print(syntax[x])
            x+=1

Bucket()
