import random

n=int(input("Maximum Number: "))    #the range
no_to_be_guessed=int(n*random.random())+1
guess=0
attempt=0

while guess!=no_to_be_guessed:
    if attempt==5:
        print("Sorry, better luck next time.")
        print("It was {}.".format(no_to_be_guessed))
        break
    
    guess=int(input("Your guess:"))
    attempt+=1
    if guess>0:
        if guess<no_to_be_guessed:
            print("no.too small")
        elif guess>no_to_be_guessed:
            print("no. too large")
            
else:
    print("Congratulations! You made it. You took {} attempts.".format(attempt))
    
                    
    
