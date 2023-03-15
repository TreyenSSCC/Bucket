# Version 0.0.9 - 3/15/2023 4:36 PM
3
syntax = ["and", "or", "if", "else", "print", "var", "while", "input", "func", "add", "end of list"]
#Spill is a print, fill is an input
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
        while(x<len(syntax)-1): # Detects if the user entered any syntax.
            if(user_code==syntax[x]):
                print(syntax[x])
            elif(user_code[0]+user_code[1]+user_code[2]==syntax[9][0]+syntax[9][1]+syntax[9][2]): #This looks for the add syntax
                num1 = 0; num2 = 0; tempNum=3; temNum2 = 0;
               ## while(user_code[tempNum]!=" "): #Something is wrong in this loop code. It doesn't set num1 to tempNum 
                ##    num1[temNum2] = num(user_code[tempNum]) #It is supposed to grab a number that the user enters "add 42 "
                ##    tempNum+=1
                try:
                    if(user_code[3]==" "):
                        while(user_code[tempNum!=" "]):
                            tempNum+=1
                            num1[temNum] = num(user_code[tempNum])
                    print(num1, tempNum)
                    #tempNum=4
                except IndexError:
                    pass
            x+=1

Bucket()

                #num1 = 0; num2 = 0; tempNum=3;
              #  while(user_code[tempNum]!=" "): #Something is wrong in this loop code. It doesn't set num1 to tempNum 
               #     num1 = num(user_code[tempNum]) #It is supposed to grab a number that the user enters "add 42 "
               #     tempNum+=1
              #  print(num1, tempNum)
              #  tempNum=3
