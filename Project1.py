import random as rd

def game():
    while True:
        com_choice = ("rock" , "paper" , "scissor")
        user_choice = input("Enter rock, paper or scissor: ").lower()
        computer_choice = rd.choice(com_choice)

        if computer_choice == user_choice:
            print(f"Your choice: {user_choice} \n Computer choice: {computer_choice}")
            print("This is bet!!")

        elif computer_choice == "rock" and user_choice == "paper":
            print(f"Your choice: {user_choice} \n Computer choice: {computer_choice}")
            print("You wins!!")
    
        elif computer_choice == "rock" and user_choice == "scissor":
            print(f"Your choice: {user_choice} \n Computer choice: {computer_choice}")
            print("Computer wins!!")
    
        elif computer_choice == "paper" and user_choice == "rock":
            print(f"Your choice: {user_choice} \n Computer choice: {computer_choice}")
            print("Computer wins!!")

        elif computer_choice == "paper" and user_choice == "scissor":
            print(f"Your choice: {user_choice} \n Computer choice: {computer_choice}")
            print("You wins!!")
    
        elif computer_choice == "scissor" and user_choice == "rock":
            print(f"Your choice: {user_choice} \n Computer choice: {computer_choice}")
            print("You wins!!")

        elif computer_choice == "scissor" and user_choice == "paper":
            print(f"Your choice: {user_choice} \n Computer choice: {computer_choice}")
            print("Computer wins!!")
        
        else:
            print("Enter valid choice")

        again = input("Do you want to try again? (y/n): ").lower()

        if again == "n":
            print("Thankyou for playing...")
            break


game()