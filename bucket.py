# Version 0.2.1a - 4/13/2023 4:35 PM

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

            f = open("demofile3.txt", "w")
            f.write(user_code)
            f.close()
            print (user_code)
        elif(user_code=="open"):
            f = open("demofile3.txt", "r")
            print(f.read())
            f.close()
        #while(x<len(syntax)-1): # Detects if the user entered any syntax. - OBSOLETE
        elif(user_code.split(" ")[0]==syntax[9]): #Add syntax
            add(user_code)
            save(user_code, code_line)
        elif(user_code.split(" ")[0]==syntax[10]): # Subtraction  syntax
            sub(user_code) # Calls the sub function
        elif(user_code.split(" ")[0]==syntax[11]): # Multiplication Syntax
            mul(user_code)
        elif(user_code.split(" ")[0]==syntax[12]): # Division Syntax
            div(user_code)
        elif(user_code.split(" ")[0]==syntax[4]): # Pour syntax
            pour(user_code)
        elif(user_code.split(" ")[0]==syntax[5]):
            var(user_code)
        elif(user_code.split(" ")[0]==syntax[14]): # Equal syntax
            equal(user_code)
        elif(user_code.split(" ")[0]==syntax[13]): # loop 10 {pour 'hello world'} - This is the loop syntax.
            try:
                tempCode = user_code.split("{")
                tempCode = tempCode[1].split("}")
                tempCode = tempCode[0]
                y = 0
                user_number = int(user_code.split(" ")[1])
                x=0;
                while(x!=user_number):
                    if(tempCode.split(" ")[0]=="pour"):
                        pour(tempCode) #The pour function - Not working, it prints out invalid syntax when there is valid syntax.
                    elif(tempCode.split(" ")[0]=="add"):
                        add(tempCode)
                    elif(tempCode.split(" ")[0]=="sub"):
                        sub(tempCode)
                    elif(tempCode.split(" ")[0]=="div"):
                        div(tempCode)
                    elif(tempCode.split(" ")[0]=="mul"):
                        mul(tempCode)
                    elif(tempCode.split(" ")[0]=="equal"):
                        equal(tempCode)
                    x+=1
            except:
                print("Check your syntax.")
            
        #else:
            #print("Invalid syntax given.")
            
#Modular Test - Failed. Keeping in code for when the loop or if syntax needs it.
def equal(user_code):
    if(user_code.split(" ")[1]==user_code.split(" ")[2]):
        print("true")
    else:
        print("false")  

def add(user_code):
    try: # add [000] 2 or add 1 [000]
        if(user_code.split(" ")[1][0]=="["):
            tempVar1 = ""; num1 = 1; transferData1 = ""
            transferData1 = user_code.split("["); transferData1 = transferData1[1].split("]")
            num1 = int(transferData1[0])
            if(user_code.split(" ")[2][0]=="["): # This adds two vars together,
                tempVar2 = ""; num2 = 1; transferData2 = ""
                transferData2 = user_code.split("["); transferData2 = transferData2[1].split("]")
                num2 = int(transferData2[0])
                print(int(variables[num1])+int(variables[num2])) # This is for some reason adding var1 to itself instead of var2.
            else: #This only adds a var in front and a normal number on bacl together
                print(int(variables[num1])+int(user_code.split(" ")[2]))
        elif(user_code.split(" ")[2][0]=="["): # This adds two vars together,
            tempVar2 = ""; num2 = 1; transferData2 = ""
            transferData2 = user_code.split("["); transferData2 = transferData2[1].split("]")
            num2 = int(transferData2[0])
            print(int(user_code.split(" ")[1])+int(variables[num2]))
        else:
            print(int(user_code.split(" ")[1])+int(user_code.split(" ")[2]))
    except:
        print("Invalid ", syntax[9], " syntax. Double check your input.", sep="")

def sub(user_code): 
    try: # add [000] 2 or add 1 [000]
        if(user_code.split(" ")[1][0]=="["):
            tempVar1 = ""; num1 = 1; transferData1 = ""
            transferData1 = user_code.split("["); transferData1 = transferData1[1].split("]")
            num1 = int(transferData1[0])
            if(user_code.split(" ")[2][0]=="["): # This adds two vars together,
                tempVar2 = ""; num2 = 1; transferData2 = ""
                transferData2 = user_code.split("["); transferData2 = transferData2[1].split("]")
                num2 = int(transferData2[0])
                print(int(variables[num1])-int(variables[num2]))
            else: #This only adds a var in front and a normal number on bacl together
                print(int(variables[num1])-int(user_code.split(" ")[2]))
        elif(user_code.split(" ")[2][0]=="["): # This adds two vars together,
            tempVar2 = ""; num2 = 1; transferData2 = ""
            transferData2 = user_code.split("["); transferData2 = transferData2[1].split("]")
            num2 = int(transferData2[0])
            print(int(user_code.split(" ")[1])-int(variables[num2]))
        else:
            print(int(user_code.split(" ")[1])-int(user_code.split(" ")[2]))
    except:
        print("Invalid ", syntax[10], " syntax. Double check your input.", sep="")

def mul(user_code):
    if(user_code.split(" ")[0]==syntax[11]): # Multiplication Syntax
        try:
            print(int(user_code.split(" ")[1])*int(user_code.split(" ")[2]))
        except:
            print("Invalid ", syntax[11], " syntax. Double check your input.", sep="")

def div(user_code):
    try:
        print(int(user_code.split(" ")[1])/int(user_code.split(" ")[2]))
    except:
        print("Invalid ", syntax[12], " syntax. Double check your input.", sep="")

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
                #print(user_code.split("'")[1]) 
                    if(user_code.split("'")[2]==""):
                        if(user_code[x]!="'"):
                            print(user_code[x], sep="", end="")
                        elif(user_code[x]=="'"):
                            print("")
                            break
                        x+=1    
        except:
            print("Double check your pour syntax.") # When given "pour 'hi", it prints the hi but gives an error.    

def var(user_code):
    try:                # var [000] = 'Hello'
        if("=" in user_code):
            tempVar = ""; num = 1; transferData = "" #These three lines grab the number
            transferData = user_code.split("["); transferData = transferData[1].split("]")
            num = int(transferData[0])
            tempVar=user_code.split("'")[1]                    
            variables.insert(num, tempVar)
            try:
                variables.pop(num+1) #This deletes an extra string that will appear.
                print(variables)
            except:
                print(variables)

        elif("=" not in user_code):
            tempVar = ""; num = 1; transferData = ""
            transferData = user_code.split("["); transferData = transferData[1].split("]")
            num = int(transferData[0])
            print(variables[num])                
    except:
        print("Something is wrong with your var syntax. Double check it.")

def save(user_code, code_line):
    user_data.insert(0, code_line)
    user_data.insert(code_line, user_code)

Bucket(0)
