manik=input("Enter your move Manik:").lower()
riyam=input("Enter your move Riyam:").lower()
choices=["rock", "paper", "scissors"]
if manik == riyam:
    print("It's a tie!")
elif manik=="rock" and riyam=="scissors":
    print("Manik wins")
elif manik=="scissors" and riyam=="paper":
    print("Manik wins")
elif manik=="paper" and riyam=="rock":
    print("Manik wins")
elif riyam=="rock" and manik=="scissors":
    print("Riyam wins")
elif riyam=="scissors" and manik=="paper":
    print("Riyam wins")
elif riyam=="paper" and manik=="rock":
    print("Riyam wins")
else:
    print("Invalid input")

