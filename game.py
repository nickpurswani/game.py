#Random guessing game
#here you can choose between 1-10 and if your guess is correct you win!
import random
def get_guess():
    return list(input("What is your guess?"))
def genrate_code():
    digits=[str(num)for num in range(10)]
    random.shuffle(digits)
    return digits[:3]
def genrate_clues(code,user_guess):
    if user_guess==code:
        return "code cracked!"#win
    clues=[]
    for ind,num in enumerate(user_guess):
        if num==code[ind]:
            clues.append("match")
        elif num in code:
            clues.append("close")
    if clues==[]:
        return ["nope"]
    else:
        return clues
print("Welcome to the game guess the code!")
secret_code = genrate_code()
clu=[]
while clu!= "code cracked!":
    guess=get_guess()
    clu=genrate_clues(guess,secret_code)
    print("here is the result of your guess:")
    for clue in clu:
        print(clue)
    

    
