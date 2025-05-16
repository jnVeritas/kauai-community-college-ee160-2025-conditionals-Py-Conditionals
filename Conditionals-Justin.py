# AMDG

#
# Developer: Justin Nguyen
# Last Edited: 05/15/2025
# Created: 05/14/2025
# Description: It creates a password (that should not be used), based on the user's input.
#

import random
import time
from sympy import isprime

# Box of variables ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
listOfWords = [["ant","ask","aibohphobia","amock","aimedaca","al","at","am","a","app"],
               [],
               ["co","c","cap","claustrophobic","civil","ca","ce","cinoitac","cry","cyan"],
               [],
               ["et","eh","enigma","e","etymological","egdoloce","enter","end","era","ep"],
               [],
               ["grass","germination","gogesoog","graph","goat","get","g","go","gu","gin"],
               [],
               ["isogeometric","if","i","is","ink","ill","izzemretni","it","id","inns"],
               [],
               ["k","knowledgeable","ka","knocks","klofsnik","kayak","kooky","keen","kid","key"],
               [],
               ["marvellously","major","madam","momentum","m","mars","my","me","mit","mop"],
               [],
               ["obtrusive","onagero","or","o","ok","oats","oink","of","ontologically", "otto"],
               [],
               ["quick","quilt","quintessential","quest","quota","q","quo","qua","qi","qaf"],
               [],
               ["sand","status","solos","scientificality","snaedbus","so","set","s","sit","shy"],
               [],
               ["undo","up","utmost","urucu","upsetness","u","ultimate","uh","uv","urchin"],
               [],
               ["wonderful","wolfkrow","wow","what","we","wells","we","wait","weights","w"],
               [],
               ["yellowstone","yell","lyrednoy","yttrium","y","yes","ya","yay","yosemite","yoke"]]
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# The user is introduced, with caution, to this program and are asked for at max 4 letters ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print("Hello World! This is the Password Generator (that you should never use in any serious case).")
print("You will be guided step by step through this process. Please follow the instructions.")
print("")
print("Type in a string of 4 or less random letters and press enter.")
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# The user's input of a string is recorded. - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
while True:
    userLetters = input()
    if any(char.isdigit() for char in userLetters):
        print("Please don't include numbers in your text.")
    elif len(userLetters) > 4:
        print("Please include less than 4 or less letters.")
    else:
        break
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# The user's input of a number is requested and recorded. - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
print("")
print("Now, type a number with less than 8 digits and hit enter.")
while True:
    try:
        userDigits = int(input())
        if userDigits > 999999999:
            print("Please include 8 digits or less. Just as long as you do enter a number.")
        elif userDigits == 0:
            print("Please include a non-zero number.")
        else:
            break
    except ValueError:
        print("Please enter an integer value.")
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Here, the waiting message is printed, and a wait-time is generated and used. ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print("")
print("Great! Our team of UH students now have to manually come up with a password for you, when you could've done it yourself.")
print("Please hold as we may be busy, but it should (hopefully) take no less than an hour.")
waitTime = random.randrange(11,3670) - random.randrange(0, 10)
time.sleep(1)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# The program begins to modify both user inputs in this section. ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
characterPos = 0
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# The user's alphabetical input is modified in this while block. - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
while characterPos < len(userLetters):
    if userLetters[characterPos].isupper():
        currentLetterValue = ord(userLetters[characterPos]) - 65
    else:
        currentLetterValue = ord(userLetters[characterPos]) - 97
    if (currentLetterValue + 1) % 2 == 1:
        newAlphaOutput = listOfWords[currentLetterValue][random.randrange(1,9)]
    else:
        newAlphaOutput = userLetters[characterPos]
    userLetters = userLetters.replace(userLetters[characterPos], newAlphaOutput)
    characterPos = characterPos + len(newAlphaOutput)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# This while block modifies the user's numerical input. - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
while True:
    # Variables are set here, making use of randomness.
    randomMinimum = random.randrange(random.randrange(0,59),random.randrange(60,479))
    randomMaximum = random.randrange(random.randrange(480,7654567),random.randrange(7654578,99999999))
    randomIntMaxUD = userDigits - random.randrange(userDigits-random.randrange(userDigits))
    # This block will of variables would be used later.
    if userDigits < randomMinimum:
        if userDigits < 10:
            if isprime(userDigits): # Checks if prime if the current value is less than 10.
                userDigits = userDigits * random.randrange(900,9000)
            else:
                userDigits = userDigits * random.randrange(9001,99999)
        else:
            userDigits = userDigits + (randomIntMaxUD * random.randrange(77,99))
    elif userDigits > randomMaximum:
        if userDigits % 2 == 0: # Checks if the current value is and if it is, divide by 2.
            userDigits = userDigits / 2
            userDigits = userDigits - randomIntMaxUD
    else:
        userDigits = userDigits * randomMinimum
        break
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# The program finishes and prints the hypothetical and unusable password. ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print("")
print("Thank you for waiting. Your wait time was about " + str(waitTime) + " seconds.")
print("Your new password (that you shouldn't actually use) is " + userLetters + str(userDigits) + ".")
# The variables can be added together in this case, but can't if either weren't strings because the types would be different. # ~~
