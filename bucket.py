# Version 0.2.4a - 4/15/2023 11:52 AM
# Copyright (c) 2023 Treyen Wilson

syntax = ["and", "or", "if", "else", "pour", "var", "while", "fill", "func", "add", "sub", "mul", "div", "loop", "equal", "end of list"]
variables = [] #This stores the variables for the user
user_data = [0] # This stores what the user has typed.
user_functions = [] # This stores the user created functions.

#Spill/pour is a print, fill is an input
# The syntax list will contain all of the syntax for Bucket.

def Bucket(code_line):# This is the main function of the program. This is where Bucket will perform most of it's tasks.
    #code_line = 0
    while True:
        x=0
        code_line+=1
        user_data[0] = code_line-1
        print(code_line, ": ", sep="", end="")
        user_code = input("").lower()
        if (user_code==("quit") or user_code=="exit"):
            break
        elif(user_code=="save"):
            f = open("file.bkt", "w")
            f.write("{}".format(user_data[0:len(user_data)]))
            #print(user_data)
            f.close()
            #print(user_data) #Debug
        elif(user_code=="open"): #Input : '[5, 'add 4 5', 'sub 7 4', 'mul 985 4', 'div 4837 3', "pour 'hi'", 'add 4 5']'
            f = open("file.bkt", "r") #Open syntax
            test = [0]
            test = eval(f.read())
            #user_data = user_data[1:len(user_data)-1]
            #c = 0 #This is to loop through user_data
            code_line=int(test[0])
            x = 1
            while(x<test[0]):
                #equal(test[x])
                if(test[x].split(" ")[0]=="equal"):
                    equal(test[x])
                elif(test[x].split(" ")[0]=="add"):
                    add(test[x])
                elif(test[x].split(" ")[0]=="sub"):
                    sub(test[x])
                elif(test[x].split(" ")[0]=="mul"):
                    mul(test[x])
                elif(test[x].split(" ")[0]=="div"):
                    div(test[x])
                elif(test[x].split(" ")[0]=="pour"):
                    pour(test[x])
                elif(test[x].split(" ")[0]=="var"):
                    var(test[x])
                elif(test[x].split(" ")[0]=="loop"):
                    loop(test[x])
                elif(test[x].split(" ")[0]=="if"):
                    if_syntax(test[x])
                x+=1
            f.close()
            #user_data = test
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
        elif(user_code.split(" ")[0]==syntax[5]): # Var Syntax
            var(user_code)
        elif(user_code.split(" ")[0]==syntax[14]): # Equal syntax
            equal(user_code)
        elif(user_code.split(" ")[0]==syntax[13]): # Loop syntax - 
        #loop 10 {pour 'hello world'} - This is the loop syntax.
            loop(user_code)
        elif(user_code.split(" ")[0]==syntax[2]): #If code
            if_syntax(user_code)
        user_data.insert(code_line, user_code) #This saves the user code in a list for later use.
        #print(user_data) #Debug
        #else:
            #print("Invalid syntax given.")
            
#Syntax code
def equal(user_code):
    try:
        if(user_code.split(" ")[1]==user_code.split(" ")[2]):
            print("true")
            return("true")
        else:
            print("false")
            return("false")
    except:
        print("Nothing to equal.")

def sequal(user_code): #This is a special version of equal just for the if syntax.
    try:
        if(user_code.split(" ")[1]==user_code.split(" ")[2]):
            #print("true")
            return("true")
        else:
            #print("false")
            return("false")
    except:
        print("Nothing to equal.")

def add(user_code):
    try:
        # add [000] 2 or add 1 [000]
        if(user_code.split(" ")[1][0]=="["):
            tempVar1 = ""; num1 = 1; transferData1 = ""
            transferData1 = user_code.split("["); transferData1 = transferData1[1].split("]")
            num1 = int(transferData1[0])
            if(user_code.split(" ")[2][0]=="["):# This adds two vars together,
                tempVar2 = ""; num2 = 1; transferData2 = ""
                transferData2 = user_code.split("["); transferData2 = transferData2[2].split("]") #This needs to be 2 instead of 1. Found out several days after.
                num2 = int(transferData2[0]); #print (transferData1, transferData2) That was for debugging. 
                print(int(variables[num1])+int(variables[num2]))
                return(int(variables[num1])+int(variables[num2]))
            else: 
                #This only adds a var in front and a normal number on back together
                print(int(variables[num1])+int(user_code.split(" ")[2]))
                return(int(variables[num1])+int(user_code.split(" ")[2]))
        elif(user_code.split(" ")[2][0]=="["): # This adds two vars together,
            tempVar2 = ""; num2 = 1; transferData2 = ""
            transferData2 = user_code.split("["); transferData2 = transferData2[1].split("]")
            num2 = int(transferData2[0])
            print(int(user_code.split(" ")[1])+int(variables[num2]))
            return(int(user_code.split(" ")[1])+int(variables[num2]))

        else:
            print(int(user_code.split(" ")[1])+int(user_code.split(" ")[2])) #This prints the result
            return(int(user_code.split(" ")[1])+int(user_code.split(" ")[2])) #This allows for var to save the result
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
                transferData2 = user_code.split("["); transferData2 = transferData2[2].split("]")
                num2 = int(transferData2[0])
                print(int(variables[num1])-int(variables[num2]))
                return(int(variables[num1])-int(variables[num2]))
            else: #This only adds a var in front and a normal number on bacl together
                print(int(variables[num1])-int(user_code.split(" ")[2]))
                return(int(variables[num1])-int(user_code.split(" ")[2]))
        elif(user_code.split(" ")[2][0]=="["): # This adds two vars together,
            tempVar2 = ""; num2 = 1; transferData2 = ""
            transferData2 = user_code.split("["); transferData2 = transferData2[1].split("]")
            num2 = int(transferData2[0])
            print(int(user_code.split(" ")[1])-int(variables[num2]))
            return(int(user_code.split(" ")[1])-int(variables[num2]))
        else:
            print(int(user_code.split(" ")[1])-int(user_code.split(" ")[2]))
            return(int(user_code.split(" ")[1])-int(user_code.split(" ")[2]))
    except:
        print("Invalid ", syntax[10], " syntax. Double check your input.", sep="")

def mul(user_code):
    try:
        # mul [000] 2 or mul 1 [000]
        if(user_code.split(" ")[1][0]=="["):
            tempVar1 = ""; num1 = 1; transferData1 = ""
            transferData1 = user_code.split("["); transferData1 = transferData1[1].split("]")
            num1 = int(transferData1[0])
            if(user_code.split(" ")[2][0]=="["):# This multiplies two vars together,
                tempVar2 = ""; num2 = 1; transferData2 = ""
                transferData2 = user_code.split("["); transferData2 = transferData2[2].split("]") #This needs to be 2 instead of 1.
                num2 = int(transferData2[0]);
                print(int(variables[num1])*int(variables[num2]))
                return(int(variables[num1])*int(variables[num2]))
            else: 
                #This only multiples a var in front and a normal number on back together
                print(int(variables[num1])*int(user_code.split(" ")[2]))
                return(int(variables[num1])*int(user_code.split(" ")[2]))
        elif(user_code.split(" ")[2][0]=="["): # This multiples two vars together,
            tempVar2 = ""; num2 = 1; transferData2 = ""
            transferData2 = user_code.split("["); transferData2 = transferData2[1].split("]")
            num2 = int(transferData2[0])
            print(int(user_code.split(" ")[1])*int(variables[num2]))
            return(int(user_code.split(" ")[1])*int(variables[num2]))
        else:
            print(int(user_code.split(" ")[1])*int(user_code.split(" ")[2]))
            return(int(user_code.split(" ")[1])*int(user_code.split(" ")[2]))
    except:
        print("Invalid ", syntax[11], " syntax. Double check your input.", sep="")

def div(user_code):
    try:
        # div [000] 2 or div 1 [000]
        if(user_code.split(" ")[1][0]=="["):
            tempVar1 = ""; num1 = 1; transferData1 = ""
            transferData1 = user_code.split("["); transferData1 = transferData1[1].split("]")
            num1 = int(transferData1[0])
            if(user_code.split(" ")[2][0]=="["):# This divides two vars together,
                tempVar2 = ""; num2 = 1; transferData2 = ""
                transferData2 = user_code.split("["); transferData2 = transferData2[2].split("]") #This needs to be 2 instead of 1.
                num2 = int(transferData2[0]);
                print(int(variables[num1])/int(variables[num2]))
                return(int(variables[num1])/int(variables[num2]))
            else: 
                #This only divides a var in front and a normal number on back together
                print(int(variables[num1])/int(user_code.split(" ")[2]))
                return(int(variables[num1])/int(user_code.split(" ")[2]))
        elif(user_code.split(" ")[2][0]=="["): # This divides two vars together,
            tempVar2 = ""; num2 = 1; transferData2 = ""
            transferData2 = user_code.split("["); transferData2 = transferData2[1].split("]")
            num2 = int(transferData2[0])
            print(int(user_code.split(" ")[1])/int(variables[num2]))
            return(int(user_code.split(" ")[1])/int(variables[num2]))
        else:
            print(int(user_code.split(" ")[1])/int(user_code.split(" ")[2]))
            return(int(user_code.split(" ")[1])/int(user_code.split(" ")[2]))
    except:
        print("Invalid ", syntax[12], " syntax. Double check your input.", sep="")

def pour(user_code):
    if(user_code.split(" ")[0]==syntax[4]):
        try:
            if(user_code.split(" ")[1]=="var"): # pour var [000] - This no longer works, kept for reference
                tempVar = ""; num = 1; transferData = ""
                transferData = user_code.split("["); transferData = transferData[1].split("]")
                num = int(transferData[0])
                print(variables[num])
            elif(user_code.split(" ")[1][0]=="["): # pour [000]
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
            try: #This checks to see the user is giving syntax after the '='.
                tempVar = user_code.split("("); tempVar=tempVar[1].split(")") #tempVar ends up a list
                #print(tempVar)
                if(tempVar[0].split(" ")[0]=="add"):
                    tempVar = add(tempVar[0]) #Only the first list item has the user's code. var [000] = (add 1 2)
                elif(tempVar[0].split(" ")[0]=="sub"):
                    tempVar = sub(tempVar[0])
                elif(tempVar[0].split(" ")[0]=="mul"):
                    tempVar = mul(tempVar[0])
                elif(tempVar[0].split(" ")[0]=="div"):
                    tempVar = div(tempVar[0])
                elif(tempVar[0].split(" ")[0]=="equal"):
                    tempVar = equal(tempVar[0])
                variables.insert(num, tempVar)
                try:
                    variables.pop(num+1) #This deletes an extra list item that will appear.
                    #print(variables)
                except:
                    print("", sep="", end="") #Just some empy code to fill the indentation
            except:
                tempVar=user_code.split("'")[1]                    
                variables.insert(num, tempVar)
                try:
                    variables.pop(num+1) #This deletes an extra list item that will appear.
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

def svar(user_code): #This var function is for special circumstances where the entire list of vars does not need to be seen.
    try:                # var [000] = 'Hello'
        if("=" in user_code):
            tempVar = ""; num = 1; transferData = "" #These three lines grab the number
            transferData = user_code.split("["); transferData = transferData[1].split("]")
            num = int(transferData[0])
            try: #This checks to see the user is giving syntax after the '='.
                tempVar = user_code.split("("); tempVar=tempVar[1].split(")") #tempVar ends up a list
                #print(tempVar) This was used to debug
                if(tempVar[0].split(" ")[0]=="add"):
                    tempVar = add(tempVar[0]) #Only the first list item has the user's code. var [000] = (add 1 2)
                elif(tempVar[0].split(" ")[0]=="sub"):
                    tempVar = sub(tempVar[0])
                elif(tempVar[0].split(" ")[0]=="mul"):
                    tempVar = mul(tempVar[0])
                elif(tempVar[0].split(" ")[0]=="div"):
                    tempVar = div(tempVar[0])
                elif(tempVar[0].split(" ")[0]=="equal"):
                    tempVar = equal(tempVar[0])
                variables.insert(num, tempVar)
                try:
                    variables.pop(num+1) #This deletes an extra list item that will appear.
                    #print(variables)
                except:
                    print("", sep="", end="") #Just some empy code to fill the indentation
            except:
                tempVar=user_code.split("'")[1]                    
                variables.insert(num, tempVar)
                try:
                    variables.pop(num+1) #This deletes an extra list item that will appear.
                    #print(variables)
                except:
                    print("", sep="", end="") #Empty code so that python does throw an error.

        elif("=" not in user_code):
            tempVar = ""; num = 1; transferData = ""
            transferData = user_code.split("["); transferData = transferData[1].split("]")
            num = int(transferData[0])
            print(variables[num])                
    except:
        print("Something is wrong with your var syntax. Double check it.")

def loop(user_code):
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
            elif(tempCode.split(" ")[0]=="var"):
                var(tempCode)
            x+=1
    except:
        print("Check your syntax.")

def if_syntax(user_code): # if equal 1 1: pour 'hello'; else: add 1 2;
    try:
        tempCheckCode = ""
        if(user_code.split(" ")[1]=="equal"):
            #This makes the comparison code able to be interpreted by Bucket.
            tempCheckCode = user_code.split(" ")[1]+" "+user_code.split(" ")[2]+" "+user_code.split(" ")[3][0:len(user_code.split(" ")[3])-1]
            if(sequal(tempCheckCode)=="true"):
                tempIfCode = user_code.split(":")[1].split(";")[0]
                tempIfCode=tempIfCode[1:len(tempIfCode)]
                #Below is checking for the syntax
                if(tempIfCode.split(" ")[0]=="equal"):
                    equal(tempIfCode)
                elif(tempIfCode.split(" ")[0]=="add"):
                    add(tempIfCode)
                elif(tempIfCode.split(" ")[0]=="sub"):
                    sub(tempIfCode)
                elif(tempIfCode.split(" ")[0]=="mul"):
                    mul(tempIfCode)
                elif(tempIfCode.split(" ")[0]=="div"):
                    div(tempIfCode)
                elif(tempIfCode.split(" ")[0]=="pour"):
                    pour(tempIfCode)
                elif(tempIfCode.split(" ")[0]=="var"):
                    var(tempIfCode)
                elif(tempIfCode.split(" ")[0]=="loop"):
                    loop(tempIfCode)
                elif(tempIfCode.split(" ")[0]=="if"):
                    if_syntax(tempIfCode)
            elif(sequal(tempCheckCode)=="false"):
                tempElseCode = user_code.split("else: ")[1].split(";")[0]
                if(tempElseCode.split(" ")[0]=="equal"):
                    equal(tempElseCode)
                elif(tempElseCode.split(" ")[0]=="add"):
                    add(tempElseCode)
                elif(tempElseCode.split(" ")[0]=="sub"):
                    sub(tempElseCode)
                elif(tempElseCode.split(" ")[0]=="mul"):
                    mul(tempElseCode)
                elif(tempElseCode.split(" ")[0]=="div"):
                    div(tempElseCode)
                elif(tempElseCode.split(" ")[0]=="pour"):
                    pour(tempElseCode)
                elif(tempElseCode.split(" ")[0]=="var"):
                    var(tempElseCode)
                elif(tempElseCode.split(" ")[0]=="loop"):
                    loop(tempElseCode)
                elif(tempElseCode.split(" ")[0]=="if"):
                    if_syntax(tempElseCode)
            #print(tempCheckCode)
    except:
        #print(tempCheckCode)
        print("Something is wrong with your if code.")
def save(user_code, code_line):
    #user_data.insert(0, code_line)
    #user_data.insert(code_line, user_code)
    print("",sep="",end="") #Empty code to make the function work

Bucket(0)
