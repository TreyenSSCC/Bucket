# Version 0.0.7 - 3/14/2023 5:00 PM

syntax = ["and", "or", "if", "else", "print", "var", "while", "func", "end of list"]
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
        while(x<8): # Detects if the user entered any syntax. #Use len() command to grab the length of the list like x<len(syntax)-1
            if(user_code==syntax[x]):
                print(syntax[x])
            x+=1

Bucket()
