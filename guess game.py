# Author :- Nitesh
# A beginer python learner from Youtube "CodewithHarry"

rule = '''There are number between 1 to 100 , the number is hiden.
lets guess it '''
print(rule)

import random

randomNumber =random.randint(1,100)
userGuess = None
gusses = 0

while(userGuess != randomNumber):
     userGuess = int(input("entre your guess: "))
     gusses +=1
     if(userGuess==randomNumber):
           print("you guess is true!!")
     else:
         if(userGuess>randomNumber):
              print("You guess is wrong !! Entre smaler number: ")
         else:
          print("You guess is wrong !! Entre larger number: ")

         
print(f"you gussed the number in {gusses} guesss")
