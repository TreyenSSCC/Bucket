# Version 0.1.6a - 4/01/2023 11:33 AM

syntax = ["and", "or", "if", "else", "pour", "var", "while", "fill", "func", "add", "sub", "mul", "div", "loop", "end of list"]
variables = [] #This stores the variables for the user
user_data = [] # This stores what the user has typed.

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
        elif(user_code=="save"):
            print(1)
        #while(x<len(syntax)-1): # Detects if the user entered any syntax. - OBSOLETE
        if(user_code.split(" ")[0]==syntax[9]): #Add syntax
            try: # add var [000] 2 or add 1 var [000]
                if(user_code.split(" ")[1]=="var" or user_code.split(" ")[2]=="var"):
                    tempVar = ""; num = 1; transferData = ""
                    transferData = user_code.split("["); transferData = transferData[1].split("]")
                    num = int(transferData[0])
                    if(user_code.split(" ")[1]=="var"):
                        print(int(variables[num])+user_code.split(" ")[3])
                    else:
                        print(user_code.split(" ")[1]+int(variables[num]))
                else:
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
                if(user_code.split(" ")[1]=="var"): # pour var [000]
                    tempVar = ""; num = 1; transferData = ""
                    transferData = user_code.split("["); transferData = transferData[1].split("]")
                    num = int(transferData[0])
                    print(variables[num])
                else:
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
        elif(user_code.split(" ")[0]==syntax[5]):
            try:                # var [000] = 'Hello'
                if("=" in user_code):
                    tempVar = ""; num = 1; transferData = "" #These three lines grab the number
                    transferData = user_code.split("["); transferData = transferData[1].split("]")
                    num = int(transferData[0])
                    tempVar=user_code.split("'")[1]
                    variables.insert(num, tempVar); print(variables)
                elif("=" not in user_code):
                    tempVar = ""; num = 1; transferData = ""
                    transferData = user_code.split("["); transferData = transferData[1].split("]")
                    num = int(transferData[0])
                    print(variables[num])

                
            except:
                print("Something is wrong with your var syntax. Double check it.")
        elif(user_code.split(" ")[0]==syntax[x]):
            print(syntax[x])
        else:
            print("Invalid syntax given.")
            
        

Bucket()
