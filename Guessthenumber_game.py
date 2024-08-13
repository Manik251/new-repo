import random
random_number=random.randrange(1,50)
# print(random_number)
chance=5
for i in range(chance):
    chance = chance-1
    guess=int(input("Enter a number: "))   
    if guess>random_number:
        print(f"The guess is greater than random number\n\033[1;31;40mYou have {chance} chance left. Play Carefully!!!\033[0m")
    elif guess<random_number:
        print(f"The gues is lesser than random number\n\033[1;31;40mYou have {chance} chance left. Play Carefully!!!\033[0m")
    else:
        print("The guess is right")
        break
    # if random_number == guess:
    #     print("The guess is right")
    #     break
    # else:
    #     print(f"The guess is wrong")
