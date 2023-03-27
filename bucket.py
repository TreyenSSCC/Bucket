# Version 0.1.3a - 3/21/2023 4:31 PM
3
syntax = ["and", "or", "if", "else", "pour", "var", "while", "fill", "func", "add", "sub", "mul", "div", "loop", "end of list"]
#Spill/pour is a print, fill is an input
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
        #while(x<len(syntax)-1): # Detects if the user entered any syntax. - OBSOLETE
        if(user_code.split(" ")[0]==syntax[9]): #Add syntax
            try:
                print(int(user_code.split(" ")[1])+int(user_code.split(" ")[2]))
            except:
                print("Invalid ", syntax[9], " syntax. Double check your input.", sep="")
        elif(user_code.split(" ")[0]==syntax[10]): # Subtraction  syntax
            try:
                print(int(user_code.split(" ")[1])-int(user_code.split(" ")[2]))
            except:
                print("Invalid ", syntax[10], " syntax. Double check your input.", sep="")
        elif(user_code.split(" ")[0]==syntax[11]): # Multiplication Syntax
            try:
                print(int(user_code.split(" ")[1])*int(user_code.split(" ")[2]))
            except:
                print("Invalid ", syntax[11], " syntax. Double check your input.", sep="")
        elif(user_code.split(" ")[0]==syntax[12]): # Division Syntax
            try:
                print(int(user_code.split(" ")[1])/int(user_code.split(" ")[2]))
            except:
                print("Invalid ", syntax[12], " syntax. Double check your input.", sep="")
        elif(user_code.split(" ")[0]==syntax[4]):
            try:
                x = 6
                while True:
                    if(user_code[x]!="'"):
                        print(user_code[x], sep="", end="")
                    elif(user_code[x]=="'"):
                        print("")
                        break
                    x+=1
            except:
                print("Double check your pour syntax.") # When given "pour 'hi", it prints the hi but gives an error.
        elif(user_code.split(" ")[0]==syntax[5]): #Something is wrong.
            try: # list.insert(0, "stuff")
                var = []
                x = 13
                tempVar = ""
                number = 111; number[0]=user_code.split(" ")[1][0]; number[1]=user_code.split(" ")[1][1]
                number[2]=user_code.split(" ")[1][2]
                y=0
                while True:
                    if(user_code[x]!="'"):
                        tempVar[y]=user_code[x]
                    else:
                        var.insert(number, tempVar)
                        print(var[number])
                        break
                #var [001] = 'variable'
            except:
                print("Error")

        elif(user_code.split(" ")[0]==syntax[x]):
            print(syntax[x])
        else:
            print("Invalid syntax given.")
            
        

Bucket()
