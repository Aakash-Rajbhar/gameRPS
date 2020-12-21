import random
def gameWin(noob,pro) :

    #if two values are equal, declare Tie
    if noob == pro :
        return None
    
    #check all possibilties when computer choose 'r'
    elif noob == 'r' :
        if pro == 's' :
            return False
        elif pro == 'p' :
            return True

    #check all possibilities when computer choose 'p'
    elif noob == 'p' :
        if pro == 's' :
            return True
        elif pro == 'r' :
            return False

    #check all possibilities when computer choose 's'
    elif noob == 's' :
        if pro == 'r' :
            return True
        elif pro == 'p' :
            return False

print("Noob Turn : Rock(r) or Paper(p) or Scisor(s)")
randno = random.randint(1,4)
if  randno == 1 :
    noob == 'r'
elif randno == 2 :
    noob == 'p'
else :
    noob == 's'

#User Input
pro = input("Your Turn : Rock(r) or Paper(p) or Scisor(s)")
a = gameWin(noob,pro)

print(f"Computer Choose : {noob}")
print(f"User Choose : {pro}")

if a == None :
    print("The Game is Tied.")
elif a == True :
    print("You Win.")
elif a == False :
    print("You Lose.")
else :
    print("Choose a Valid Option.")