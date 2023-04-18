# Version 0.2.9b - 4/18/2023 3:49 PM
# Copyright (c) 2023 Treyen Wilson
# This is the b version of Bucket.

syntax = ["and", "or", "if", "else", "pour", "var", "while", "fill", "func", "add", "sub", "mul", "div", "loop", "equal", "end of list"]
variables = [] #This stores the variables for the user
user_data = [0] # This stores what the user has typed.
user_functions = [0] # This stores the user created functions.
syntaxAdded = "no"
code_line = 1
#Spill/pour is a print, fill is an input
# The syntax list will contain all of the syntax for Bucket.

def Bucket(code_line):# This is the main function of the program. This is where Bucket will perform most of it's tasks.
    try:
        while True:
            x=0
            code_line+=1
            user_data[0] = code_line-1
            print(code_line, ": ", sep="", end="")
            user_code = input("").lower()
            if (user_code==("quit") or user_code=="exit"):
                break
            elif(user_code=="drop"):
                f = open("water.bkt", "r")
                storage = eval(f.read())
                exec(storage)
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
                while(x<test[0]+1):
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
                        #print(test[x])
                        loop(test[x])
                    elif(test[x].split(" ")[0]=="if"):
                        if_syntax(test[x])
                    elif(test[x].split(" ")[0]=="func"):
                        sfunc(test[x])
                    
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
                #loop(user_code)
                loop(user_code) #This is to test out new features for the loop
            elif(user_code.split(" ")[0]==syntax[2]): #If code
                if_syntax(user_code)
            elif(user_code.split(" ")[0]==syntax[8]): #This detects if a user is making a function.
                user_code = func(user_code)
            else:
                print("Invalid syntax given.")
            user_data.insert(code_line, user_code) #This saves the user code in a list for later use.
    except:
        print("Something went wrong.")       
#Syntax code
def equal(user_code):
    try:
        if(user_code.split(" ")[1][0]=="["):
            tempVar1 = ""; num1 = 1; transferData1 = ""
            transferData1 = user_code.split("["); transferData1 = transferData1[1].split("]")
            num1 = int(transferData1[0])
            if(user_code.split(" ")[2][0]=="["):# This compares two vars together,
                tempVar2 = ""; num2 = 1; transferData2 = ""
                transferData2 = user_code.split("["); transferData2 = transferData2[2].split("]") #This needs to be 2 instead of 1. Found out several days after.
                num2 = int(transferData2[0]); #print (transferData1, transferData2) That was for debugging. 
                if(variables[num1]==variables[num2]):
                    print("true")
                    return("true")
                else:
                    print("false")
                    return("false")
            else:
                if(variables[num1]==user_code.split(" ")[2]):
                #This only compares a var in front and a normal number on back together
                    print("true")
                    return("true")
                else:
                    print("false")
                    return("false")
        elif(user_code.split(" ")[2][0]=="["): # This compares a var and a number together,
            tempVar2 = ""; num2 = 1; transferData2 = ""
            transferData2 = user_code.split("["); transferData2 = transferData2[1].split("]")
            num2 = int(transferData2[0])
            if(user_code.split(" ")[1]==variables[num2]):
                print(true)
                return(true)
            else:
                print("false")
                return("false")
        else:
            if(user_code.split(" ")[1]==user_code.split(" ")[2]):
                print("true") #This prints the result
                return("true") #This allows for var to save the result
            else:
                print("false")
                return("false")        
    except:
        print("Nothing to equal.")

def func(user_code):
    # func [000] =
    # | var [0] = 'Hi there.'
    # | pour [0]
    # | add 4 5
    # | end
    # "func [0] =| var [0] = 'hi there.'| pour [0]| add 4 5| end"
    try:
        #if(user_code.split(" ")[0]==syntax[8] and user_code.split(" ")[0]=="[all]"): This is a planned way to see every function the user has.
        #    print(user_functions)
        if(user_code.split(" ")[0]==syntax[8]):
            if(user_code.split("| ")[0][len(user_code.split("| ")[0])-1]=="="):
                while(True):
                    #print(user_code)
                    user_code=user_code+input("")
                    if(user_code.split("| ")[len(user_code.split("| "))-1]=="end"):
                        
                        tempFuncNum = len(user_code.split("| "))-2 #This will store how many commands are in the function
                        tempVar = ""; num = 1; transferData = "" #These three lines grab the number from the func
                        transferData = user_code.split("["); transferData = transferData[1].split("]")
                        num = int(transferData[0])
                        user_functions.insert(num, user_code)
                        try:
                            user_functions.pop(num+1) #This deletes an extra list item that will appear.
                            #print(variables)
                        except:
                            print("", sep="", end="") #Just some empy code to fill the indentation                    
                        #user_functions[num] = user_code 
                        break
            elif(user_code.split(" ")[1][0]=="["):
                
                tempVar = ""; num = 1; transferData = "" #These three lines grab the number from the func
                transferData = user_code.split("["); transferData = transferData[1].split("]")
                num = int(transferData[0])
                tempFuncCode = user_functions[num]
                tempFuncNum = len(tempFuncCode.split("| "))-2 # This is to find how many commands there are. It needs to start at 1!
                k = 1
                #print(tempFuncNum)
                while(k<tempFuncNum+1): #tempFuncNum is one higher than the last command.
                    if(tempFuncCode.split("| ")[k].split(" ")[0]=="add"):
                        add(tempFuncCode.split("| ")[k])
                    elif(tempFuncCode.split("| ")[k].split(" ")[0]=="pour"):
                        pour(tempFuncCode.split("| ")[k])
                    elif(tempFuncCode.split("| ")[k].split(" ")[0]=="sub"):
                        sub(tempFuncCode.split("| ")[k])
                    elif(tempFuncCode.split("| ")[k].split(" ")[0]=="mul"):
                        mul(tempFuncCode.split("| ")[k])
                    elif(tempFuncCode.split("| ")[k].split(" ")[0]=="div"):
                        div(tempFuncCode.split("| ")[k])
                    elif(tempFuncCode.split("| ")[k].split(" ")[0]=="var"):
                        svar(tempFuncCode.split("| ")[k])
                    elif(tempFuncCode.split("| ")[k].split(" ")[0]=="loop"):
                        loop(tempFuncCode.split("| ")[k])
                    elif(tempFuncCode.split("| ")[k].split(" ")[0]=="if"):
                        if_syntax(tempFuncCode.split("| ")[k])
                    elif(tempFuncCode.split("| ")[k].split(" ")[0]=="func"):
                        func(tempFuncCode.split("| ")[k])
                    else:
                        #print(k, tempFuncCode.split("| ")[k])
                        print("Something is wrong with your func syntax.")
                    k+=1

            else:
                print("No valid func code.")
        #user_data.insert(code_line, user_code) #This saves the function code for the file.
        return user_code
    except:
        print("The func syntax is not complete.")

def sfunc(user_code): # This is used when the input needs to be on a single line.
    # func [000] =
    # | var [0] = 'Hi there.'
    # | pour [0]
    # | add 4 5
    # | end
    # "func [0] =| var [0] = 'hi there.'| pour [0]| add 4 5| end"
    try:
        if(user_code.split(" ")[0]==syntax[8]):
            if(user_code.split("| ")[0][len(user_code.split("| ")[0])-1]=="="):
                while(True):
                    #print(user_code)
                    if(user_code.split("| ")[len(user_code.split("| "))-1]=="end"):
                        user_data.insert(code_line, user_code) #This saves the function code for the file.
                        tempFuncNum = len(user_code.split("| "))-2 #This will store how many commands are in the function
                        tempVar = ""; num = 1; transferData = "" #These three lines grab the number from the func
                        transferData = user_code.split("["); transferData = transferData[1].split("]")
                        num = int(transferData[0])
                        user_functions.insert(num, user_code)
                        try:
                            user_functions.pop(num+1) #This deletes an extra list item that will appear.
                            #print(variables)
                        except:
                            print("", sep="", end="") #Just some empy code to fill the indentation                    
                        #user_functions[num] = user_code 
                        break
            elif(user_code.split(" ")[1][0]=="["):
                tempVar = ""; num = 1; transferData = "" #These three lines grab the number from the func
                transferData = user_code.split("["); transferData = transferData[1].split("]")
                num = int(transferData[0])
                tempFuncCode = user_functions[num]
                tempFuncNum = len(tempFuncCode.split("| "))-2 # This is to find how many commands there are. It needs to start at 1!
                k = 1
                #print(tempFuncNum)
                while(k<tempFuncNum+1): #tempFuncNum is one higher than the last command.
                    if(tempFuncCode.split("| ")[k].split(" ")[0]=="add"):
                        add(tempFuncCode.split("| ")[k])
                    elif(tempFuncCode.split("| ")[k].split(" ")[0]=="pour"):
                        pour(tempFuncCode.split("| ")[k])
                    elif(tempFuncCode.split("| ")[k].split(" ")[0]=="sub"):
                        sub(tempFuncCode.split("| ")[k])
                    elif(tempFuncCode.split("| ")[k].split(" ")[0]=="mul"):
                        mul(tempFuncCode.split("| ")[k])
                    elif(tempFuncCode.split("| ")[k].split(" ")[0]=="div"):
                        div(tempFuncCode.split("| ")[k])
                    elif(tempFuncCode.split("| ")[k].split(" ")[0]=="var"):
                        svar(tempFuncCode.split("| ")[k])
                    elif(tempFuncCode.split("| ")[k].split(" ")[0]=="loop"):
                        loop(tempFuncCode.split("| ")[k])
                    elif(tempFuncCode.split("| ")[k].split(" ")[0]=="if"):
                        if_syntax(tempFuncCode.split("| ")[k])
                    elif(tempFuncCode.split("| ")[k].split(" ")[0]=="func"):
                        func(tempFuncCode.split("| ")[k])
                    else:
                        #print(k, tempFuncCode.split("| ")[k])
                        print("Something is wrong with your func syntax.")
                    k+=1

            else:
                print("No valid func code.")
    except:
        print("The func syntax is not complete.")

def sequal(user_code): #This is a special version of equal just for the if syntax.
    try:
        if(user_code.split(" ")[1][0]=="["):
            tempVar1 = ""; num1 = 1; transferData1 = ""
            transferData1 = user_code.split("["); transferData1 = transferData1[1].split("]")
            num1 = int(transferData1[0])
            if(user_code.split(" ")[2][0]=="["):# This compares two vars together,
                tempVar2 = ""; num2 = 1; transferData2 = ""
                transferData2 = user_code.split("["); transferData2 = transferData2[2].split("]") #This needs to be 2 instead of 1. Found out several days after.
                num2 = int(transferData2[0]); #print (transferData1, transferData2) That was for debugging. 
                if(variables[num1]==variables[num2]):
                    #print("true")
                    return("true")
                else:
                    #print("false")
                    return("false")
            else:
                if(variables[num1]==user_code.split(" ")[2]):
                #This only compares a var in front and a normal number on back together
                    #print("true")
                    return("true")
                else:
                    #print("false")
                    return("false")
        elif(user_code.split(" ")[2][0]=="["): # This compares a var and a number together,
            tempVar2 = ""; num2 = 1; transferData2 = ""
            transferData2 = user_code.split("["); transferData2 = transferData2[1].split("]")
            num2 = int(transferData2[0])
            if(user_code.split(" ")[1]==variables[num2]):
                print(true)
                return(true)
            else:
                #print("false")
                return("false")
        else:
            if(user_code.split(" ")[1]==user_code.split(" ")[2]):
                #print("true") #This prints the result
                return("true") #This allows for var to save the result
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
        elif(user_code.split(" ")[2][0]=="["): # This adds a var and a number together,
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
        #print(user_code)
        # div [000] 2 or div 1 [000]
        if(user_code.split(" ")[1][0]=="["):
            #print(user_code.split(" "))
            tempVar1 = ""; num1 = 1; transferData1 = ""
            transferData1 = user_code.split("["); transferData1 = transferData1[1].split("]")
            num1 = int(transferData1[0])
            #print(num1, transferData1)
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
                    #print(tempVar)
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
    if(user_code[len(user_code)-2]=="\""):
        try: #Example code "loop 10 {pour '1' 1"add 3 4 2"}"
            tempCode = user_code.split("{")
            tempCode = tempCode[1].split("}")
            tempCode = tempCode[0] #"pour '1' 1. add 3 4 2."
            tempNum = len(tempCode.split("\""))
            #print(tempCode.split("; "))
            tempCode = tempCode.split("\"")[0:tempNum-1]
            t = 0
            while(t<tempNum-1):
                tempCode[t]=tempCode[t][0:len(tempCode[t])-2]
                t+=1
            #print(tempCode) For debug
            t=0
            y = 0
            user_number = int(user_code.split(" ")[1])
            x=0
            while(t<tempNum-1):
                while(x!=user_number):
                    if(tempCode[t].split(" ")[0]=="pour"):
                        pour(tempCode[t])
                    elif(tempCode[t].split(" ")[0]=="add"):
                        add(tempCode[t])
                    elif(tempCode[t].split(" ")[0]=="sub"):
                        sub(tempCode[t])
                    elif(tempCode[t].split(" ")[0]=="div"):
                        div(tempCode[t])
                    elif(tempCode[t].split(" ")[0]=="mul"):
                        mul(tempCode[t])
                    elif(tempCode[t].split(" ")[0]=="equal"):
                        equal(tempCode[t])
                    elif(tempCode[t].split(" ")[0]=="var"):
                        var(tempCode[t])
                    elif(tempCode[t].split(" ")[0]=="if"):
                        if_syntax(tempCode[t])
                    elif(tempCode[t].split(" ")[0]=="func"):
                        func(tempCode[t])
                    
                    x+=1
                t+=1
                x=0
        except:
            print("Check your syntax.")
    else:
        print("You forgot the number in your loop.")

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
                elif(tempIfCode.split(" ")[0]=="func"):
                    func(tempIfCode)
            elif(sequal(tempCheckCode)=="false"):
                tempElseCode = user_code.split("else: ")[1].split(";")[0]
                #print(tempElseCode)
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
                elif(tempElseCode.split(" ")[0]=="pour"): # The '.' when used at the end of a sentence causes it to get cut off. (Found after a few minutes of troubleshooting.)
                    #print("Here: ", tempElseCode)
                    pour(tempElseCode)
                elif(tempElseCode.split(" ")[0]=="var"):
                    var(tempElseCode)
                elif(tempElseCode.split(" ")[0]=="loop"):
                    loop(tempElseCode)
                elif(tempElseCode.split(" ")[0]=="if"):
                    if_syntax(tempElseCode)
                elif(tempElseCode.split(" ")[0]=="func"):
                    func(tempElseCode)
            #print(tempCheckCode)
    except:
        #print(tempCheckCode)
        print("Something is wrong with your if code.")

def save(user_code, code_line):
    #user_data.insert(0, code_line)
    #user_data.insert(code_line, user_code)
    print("",sep="",end="") #Empty code to make the function work

def check_var(user_code): #This is for when Bucket needs to check what var needs to called. - Made for future use.
    tempVar = ""; num = 1; transferData = ""
    transferData = user_code.split("["); transferData = transferData[1].split("]")
    num = int(transferData[0])
    return(tempVar, num)

Bucket(0)