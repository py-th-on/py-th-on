import random

rps = [x.lower() for x in ['R', 'P', 'S']]
computer_count = 0
user_count = 0
draws = 0
print("Welcome to the Rock/Paper/Scissors game!")
while True:
    number = random.randint(0, 2)
    computer_number = rps[number]
    user_input = input("Choose either 'r' for Rock, 'p' for Paper, 's' for Scissors or press 'q' to quit.\n").lower()
    if user_input != 'r' and user_input != 'p' and user_input != 's' and user_input != 'q':
        print("Oh ups something went wrong. Please try again.")
        continue
    elif user_input == 'q':
        unsure = input("Are you sure you want to quit? press 'y' for yes, 'n' for no\n").lower()
        if unsure != 'y' and unsure != 'n':
            wrong = input("You need to type either 'y' to leave or 'n' to continue.\n")
            if wrong == 'y':
                break
            else:
                continue
        if unsure == 'y':
            break
        else:
            continue
    if user_input == rps[0] and computer_number == rps[2]:
        print(f"User: {user_input} | Computer: {computer_number}")
        print("You won!")
        user_count += 1
    elif user_input == rps[1] and computer_number == rps[0]:
        print(f"User: {user_input} | Computer: {computer_number}")
        print("You won!")
        user_count += 1
    elif user_input == rps[2] and computer_number == rps[1]:
        print(f"User: {user_input} | Computer: {computer_number}")
        print("You won!")
        user_count += 1
    elif user_input == computer_number:
        print(f"User: {user_input} | Computer: {computer_number}")
        print("draw")
        draws += 1
    else:
        print(f"User: {user_input} | Computer: {computer_number}")
        print("The Computer Won!")
        computer_count += 1



print("Goodbye! Play me soon again :)")
print(f"You won in total: {user_count} | the Computer won in total: {computer_count}")
if user_count == computer_count and user_count >= 1 and computer_count >= 1:
    print("Both of you have the same amount of wins!")
print(f"There were {draws} draws in total.")

