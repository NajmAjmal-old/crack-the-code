import random

gameState = 0
ERR09 = "You are meant to enter a number from 0-9"
ERRG9 = "You Entered a Digit greater than 9"
ERRM0 = "You Entered a Negative Number"
shortHeader = "=-=-=-=-=-=-=-=-=-=-=-=-=-="
longHeader = "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="
newLine = ""
PETC = "PRESS ENTER TO CONTINUE"
pause = ""

# ERR = error
# G9 = Greater than one
# M0 = Minus one, negative number

cn1 = 10
cn2 = 10
cn3 = 10
cn4 = 10

gn1 = 0
gn2 = 0
gn3 = 0
gn4 = 0
#gn1 = guess number

print(shortHeader)
print("WELCOME TO CRACK THE CODE")
print(shortHeader)
print()
print("Rules: ")
print("1. Numbers are between 0-9")
print("2. Do not enter numbers that are negative or exceed")

print(newLine)
PETC = input(PETC)

n1 = random.randint(0,9)
n2 = random.randint(0,9)
n3 = random.randint(0,9)
n4 = random.randint(0,9)

while gameState < 4:

    if PETC == "hax":
        print(n1,n2,n3,n4)
    
    print()
    if n1 != cn1:
        print(newLine)
        gn1 = int(input("Enter digit 1: "))
        print(newLine)
        
        if gn1 == n1:
                print("Number 1 Correct")
                gameState = gameState + 1
                cn1 = n1
                print(newLine)
        else:
            if gn1 < n1:
                print(newLine)
                print("Higher")
            elif gn1 > n1:
                print(newLine)
                print("Lower")
            if gn1 > 9:
                print(newLine)
                print(longHeader)
                print(ERR09)
                print(ERRG9)
                print(longHeader)
            elif gn1 < 0:
                print(newLine)
                print(longHeader)
                print(ERR09)
                print(ERRM0)
                print(longHeader)
                

    if n2 != cn2:
        print(newLine)
        gn2 = int(input("Enter digit 2: "))
        print(newLine)
        if gn2 == n2:
                print("Number 2 Correct")
                gameState = gameState + 1
                cn2 = n2
                print(newLine)
        else:
            if gn2 < n2:
                print(newLine)
                print("Higher")
            elif gn2 > n2:
                print("Lower")
            if gn2 > 9:
                print(newLine)
                print(longHeader)
                print(ERR09)
                print(ERRG9)
                print(longHeader)
            elif gn2 < 0:
                print(newLine)
                print(longHeader)
                print(ERR09)
                print(ERRM0)
                print(longHeader)
                
                
                
    if n3 != cn3:
        print(newLine)
        gn3 = int(input("Enter digit 3: "))
        print(newLine)
        if gn3 == n3:
                print("Number 3 Correct")
                gameState = gameState + 1
                cn3 = n3
                print(newLine)
        else:
            if gn3 < n3:
                print(newLine)
                print("Higher")
            elif gn3 > n3:
                print(newLine)
                print("Lower")
            if gn3 > 9:
                print(newLine)
                print(longHeader)
                print(ERR09)
                print(ERRG9)
                print(longHeader)
                
            elif gn3 < 0:
                print(newLine)
                print(longHeader)
                print(ERR09)
                print(ERRM0)
                print(longHeader)
                

    if n4 != cn4:
        print(newLine)
        gn4 = int(input("Enter digit 4: "))
        print(newLine)
        print()
        if gn4 == n4:
                print("Number 4 Correct")
                gameState = gameState + 1
                cn4 = n4
                print(newLine)
        else:
            if gn4 < n4:
                print(newLine)
                print("Higher")
            elif gn4 > n4:
                print(newLine)
                print("Lower")
            if gn4 > 9:
                print(newLine)
                print(longHeader)
                print(ERR09)
                print(ERRG9)
                print(longHeader)
            elif gn4 < 0:
                print(newLine)
                print(longHeader)
                print(ERR09)
                print(ERRM0)
                print(longHeader)





print(newLine)
print("You cracked the code!!!")
print("Made by Najm")
print(n1,n2,n3,n4)
