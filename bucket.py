# Version 0.1.8a - 4/03/2023 5:57 PM

syntax = ["and", "or", "if", "else", "pour", "var", "while", "fill", "func", "add", "sub", "mul", "div", "loop", "equal", "end of list"]
variables = [] #This stores the variables for the user
user_data = [] # This stores what the user has typed.
user_functions = [] # This stores the user created functions.

#Spill/pour is a print, fill is an input
# The syntax list will contain all of the syntax for Bucket.

def Bucket(code_line):# This is the main function of the program. This is where Bucket will perform most of it's tasks.
    #code_line = 0
    while True:
        x=0
        code_line+=1
        print(code_line, ": ", sep="", end="")
        user_code = input("").lower()
        if (user_code==("quit") or user_code=="exit"):
            break
        elif(user_code=="save"):
            #save = open("demofile2.txt", "w")

            #print(user_data)

        user_data.insert(code_line-1, user_code)

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
            sub(user_code) # Calls the sub function
        elif(user_code.split(" ")[0]==syntax[11]): # Multiplication Syntax
            mul(user_code)
        elif(user_code.split(" ")[0]==syntax[12]): # Division Syntax
            try:
                print(int(user_code.split(" ")[1])/int(user_code.split(" ")[2]))
            except:
                print("Invalid ", syntax[12], " syntax. Double check your input.", sep="")
        elif(user_code.split(" ")[0]==syntax[4]): # Pour syntax
            pour(user_code)
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
        elif(user_code.split(" ")[0]==syntax[14]): # Equal syntax
            if(user_code.split(" ")[1]=="var" and user_code.split(" ")[3]=="var"):
                tempVar1 = ""; num1 = 1; transferData1 = "" #This makes the first variable store in num1
                transferData1 = user_code.split("["); transferData1 = transferData1[1].split("]")
                num1 = int(transferData1[0])
                #Second variable
                tempVar2 = ""; num2 = 1; transferData2 = ""
                transferData2 = user_code.split("["); transferData2 = transferData2[2].split("]")
                num2 = int(transferData2[0])
                if(variables[num1]==variables[num2]): #Can only compare a variable to a variable.
                    print("true")
                else:
                    print("false")
            # equal var [000] var [001] or equal 1 var [000] or equal var [000] 1
            elif(user_code.split(" ")[1]==user_code.split(" ")[2]):
                print("true")
            else:
                print("false")
        elif(user_code.split(" ")[0]==syntax[13]): # loop 10 {pour 'hello world'}
            try:
                tempCode = user_code.split("{")
                tempCode = tempCode[1].split("}")
                tempCode = tempCode[0]
                y = 0
                user_number = int(user_code.split(" ")[1])
                x=0;
                while(x!=user_number):
                    pour(tempCode) #The pour function
                    x+=1
            except:
                print("Check your syntax.")
            
        else:
            print("Invalid syntax given.")
            
#Modular Test - Failed. Keeping in code for when the loop or if syntax needs it.
def equal():
    if(user_code.split(" ")[0]==syntax[14]): # Equal syntax
        if(user_code.split(" ")[1]=="var" and user_code.split(" ")[3]=="var"):
            tempVar1 = ""; num1 = 1; transferData1 = "" #This makes the first variable store in num1
            transferData1 = user_code.split("["); transferData1 = transferData1[1].split("]")
            num1 = int(transferData1[0])
            #Second variable
            tempVar2 = ""; num2 = 1; transferData2 = ""
            transferData2 = user_code.split("["); transferData2 = transferData2[2].split("]")
            num2 = int(transferData2[0])
            if(variables[num1]==variables[num2]): #Can only compare a variable to a variable.
                print("true")
            else:
                print("false")      
    # equal var [000] var [001] or equal 1 var [000] or equal var [000] 1
    elif(user_code.split(" ")[1]==user_code.split(" ")[2]):
        print("true")
    else:
        print("false")  

def sub(user_code): 
    if(user_code.split(" ")[0]==syntax[10]): # Subtraction  syntax
        try:
            print(int(user_code.split(" ")[1])-int(user_code.split(" ")[2]))
        except:
            print("Invalid ", syntax[10], " syntax. Double check your input.", sep="")

def mul(user_code):
    if(user_code.split(" ")[0]==syntax[11]): # Multiplication Syntax
        try:
            print(int(user_code.split(" ")[1])*int(user_code.split(" ")[2]))
        except:
            print("Invalid ", syntax[11], " syntax. Double check your input.", sep="")

def pour(user_code):
    if(user_code.split(" ")[0]==syntax[4]):
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

Bucket(0)
