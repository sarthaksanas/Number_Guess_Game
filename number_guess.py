from random import randint
from art import logo

#declaring the constant variable
HARD_LEVEL_TURNS = 5
EASY_LEVEL_TURNS = 10

#welcome message
def welcome():
    print(logo)
    print("🎯Welcome to the Number Guessing Game!")
    print("I'am thinking of the number bertween 1 to 100...")

#Setting Difficulty Level
def set_difficulty():
    while True:
        level = input("Choose the Difficulty. 'easy' or 'hard' : ").lower()
        if level == 'easy':
            return EASY_LEVEL_TURNS
        elif level == 'hard':
            return HARD_LEVEL_TURNS
        else:
            print("⚠️ Please Enter a Valid Difficulty Level. 'easy' or 'hard' ")

#Getting User Guess
def get_user_guess():
    while True:
        try:
            guess = int(input("Guess the Number between 1 to 100 : "))
            if 1 <= guess <= 100:
                return guess
            else: 
                print("⚠️ Enter a number between 1 and 100.")
        except ValueError:
            print("⚠️ Invalid input. Please enter a number.")

#Comparing the Guess with Random Number
def check_guess(user_guess, actual_answer, turns):
    if user_guess > actual_answer:
        print("Too High.")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too Low.")
        return turns - 1
    else:
        print(f"✅ You got it! The answer was {actual_answer}.")
        return -1 #Sentinel Value To Indicate Win
        
#Actual Game Logic
def play_game():
    welcome()
    actual_answer = int(randint(1,100))
    turns = set_difficulty()
    guess = None

    while turns > 0:
        print(f"\nYou have {turns} Attempts Remaining.")
        guess = get_user_guess()
        
        turns = check_guess(guess, actual_answer, turns)

        if turns == -1:
            break #win condition
        elif turns == 0:
            print(f"❌ You've run out of guesses. You lose. The number was {actual_answer}.")
        else:
            print("🔁Guess Again")

def main():
    while True:
        play_game()
        replay = input("\n🔁Do You Want To Play Again? (yes/no) ").lower()
        if replay not in ['yes', 'y']:
            print("👋Thanks For Playing. GoodBye!")
            break

if __name__ == "__main__":
    main()

