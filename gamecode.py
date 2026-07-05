import random

user_choice= int(input("Enter your choice (Type 0 for Rock, 1 for Paper and 2 for Scissors): "))
if user_choice not in [0, 1, 2]:
    print("Invalid input!, You lose!")

else:
    comp_choice= random.randint(0,2)  # randint(a, b) is inclusive: returns 0, 1, or 2 (2 is possible)  
    print("Computer chose: ", comp_choice)



    if user_choice == comp_choice:
       print("It's a draw!")

    elif user_choice ==0 and comp_choice==2:
       print("You win!")

    elif user_choice ==2 and comp_choice==0:
       print("You lose!")

    elif comp_choice > user_choice:
       print("You lose!")

    elif user_choice > comp_choice:
       print("You win!")



