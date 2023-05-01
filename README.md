# Bucket - Version 0.3.3b
This is a programming language that I am creating.

Bucket was originally created for my final project for my Capstone class. The 'b' version will now be the main version, as I am keeping the 'a' version around for archival reasons. All future updates will be made to this Bucket version.

Update Log

**bucket.py** - Version 0.3.3b - Fixed a minor bug that caused functions to print every time a different command was executed. The func now calls svar, sadd, sdiv... instead of var, add, div...

**bucket.py** - Version 0.3.2b - Vars can now be used as the numbers for others vars. For example if var [0] = '1', the user can type "var [[0]] = 'hi'" and var [1] would be declared as "hi".

**bucket.py** - Version 0.3.1b - User input can now be grabbed. By using "var [0] = (fill)", the user will be prompted to enter something. Use 'pour' to ask for input and then use "var [0] = (fill)" to get the input, whatever the user types will be sent to the var you used. Use 'open' to see an example of a program that uses the fill command in func [0].

**bucket.py** - Version 0.3.0b - Vars can now be declared to other vars. Fixed bugs with open and func. Created special versions of the math operations to be used by func. User code must be entered in lowercase. Pour can now print capital letters. Ecountered some bugs and fixed them.

**bucket.py** - Version 0.2.9b - Added 'func' syntax. This will allow users to create functions. Functions work inside the loops and ifs, and loops and ifs work inside of functions. Currently there is no way to view the contents of all of your functions, but that is a planned feature. I have decided to make this Bucket version the main version. I'll make the 'a' version just a static version for my college class.

**bucket.py** - Version 0.2.8b - Made this the b version of Bucket. Started on adding the 'drop' syntax. This will allow users to add 'drops' top Bucket, like libraries in Python.