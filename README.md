# Bucket - Version 0.2.8a
This is a programming language that I am creating.

I am creating Bucket as the final project for my Computer Information Tech Capstone course at Southern State Community College.

Bucket may or may not be continued after the completion of the final project.


Update Log

**bucket.py** - Version 0.2.8a - Made equal be able to compare vars and non vars together. Fixed a bug with the loop syntax that caused it to cut off '.' when using pour. Also, changed how loop numbering works from 'loop 5 {add 1 2 1.} to 'loop 5 {add 1 2 1"}'.

**bucket.py** - Version 0.2.7a - Fixed a bug that caused an error message to not appear when the loop code given was incorrect without numbers.

**bucket.py** - Version 0.2.6a - Fixed a bug that appeared when using the 'open' syntax.

**bucket.py** - Version 0.2.5a - The 'loop' syntax can now execute multiple syntax. However, it will execute the first syntax the given amount of times and them execute the second syntax and so on.

**bucket.py** - Version 0.2.4a - Fixed a bug that appeared with var being declared to any math operation. Added if else syntax. It works with every other piece of syntax except for if, when if is used inside of another if it is very buggy. The 'open' and 'save' syntax will work now. The open works by exceuting everything stored in 'file.bkt' and listing the results.

**bucket.py** - Varsion 0.2.3a - Fixed a bug that occured in the 'var' syntax. Vars can now be set to the result of the math operations and 'equal' syntax. Made the loop syntax code into a function. Code is now able to be saved with 'save'. It cannot be loaded yet. The 'open' syntax just displays what is in 'file.bkt'.

**bucket.py** - Version 0.2.2a - Fixed the bug that was causing vars to be unable to be added or subtracted from other vars. The 'var' syntax works with the add syntax now. Found a bug where the var will be printed to the screen twice when add is declared to it. Added loop support for the var syntax. A bug appears when setting a var to the result of the add syntax. Changed out the 'add' syntax function code works in its function.

**bucket.py** - Version 0.2.1a - The 'add' and 'sub' syntax can now somewhat use the 'var' syntax. They only work when a var is not being added or subtracted from another var. Fixed a bug with the 'var' syntax. Worked on 'open' and 'save' Made 'var' and 'equal' into functions. The 'loop' syntax should be able to run most of the syntax now.

**bucket.py** - Version 0.2.0a - Moved the 'add' syntax code into a function. Found an error with the 'pour' syntax while used with the 'loop' syntax. Changed how 'pour' prints to the screen to try to fix the bug. The bug still occurs.

**bucket.py** - Version 0.1.9a - Moved the 'div' syntax code into a function.

**bucket.py** - Version 0.1.8a - Made some syntax into functions for future use.

**bucket.py** - Version 0.1.7a - Added some functionality to the 'loop' syntax. It can now run 'pour' a set amount of times decided by the user. Started turning some of the syntax into functions for the 'loop' syntax. Added 'equal' syntax which can compare two strings or two vars. Strings cannot be compared to vars. Planning on having the 'loop' syntax run every other type of syntax. Cannot increment a var inside of the loop yet.

**bucket.py** - Version 0.1.6a - Worked on 'var' working with 'add'. Worked on adding the ability to save code. The 'pour' syntax can now print the 'var'.

**bucket.py** - Version 0.1.5a - Fixed a 'var' bug that appeared. Users are now able to store multiple words in a single var instance.

**bucket.py** - Version 0.1.4a - Added basic functionality to the var syntax. Users are able to store and see what they store. It cannot be changed what is store currently. Also, make sure to start at [000] and increment up from there. Starting higher will cause the wrong var to be grabbed when asked for. Note: Only one word can be sent to the string currently.

**bucket.py** - Version 0.1.3a - The 'pour' syntax is now able to print a string to the screen. Started work on the function of the 'var' syntax.

**bucket.py** - Version 0.1.2a - Changed 'input' syntax to 'fill'. Added 'loop' syntax.

**bucket.py** - Version 0.1.1a - Changed how the version number system works. Versions with 'a' at the end will be the main version. Versions with any other letters will be be modified versions, for when I want to experiment. Also, changed the 'print' syntax to 'pour' and added an error for when no input is given by the user.

**bucket.py** - Version 0.1.0: Added basic artimatic functions: add, sub, div, and div. Cleaned up the code. Rewrote how syntax was detected by the program.

**bucket.py** - Version 0.0.9: Started to add the function of ADD syntax. Made the syntax list expandable.

**bucket.py** - Version 0.0.7: Added func syntax to syntax list.

**bucket.py** - Version 0.0.6: Added a loop that detects if the user entered syntax and then prints out the syntax.

**bucket.py** - Version 0.0.5: Made syntax all lowercase. Added an exit and quit function that allows users to exit the program. User input is turned lowercase when grabbed now.
