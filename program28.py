# Custom Exceptions
class ValueTooLarge(Exception):
    pass

class ValueTooSmall(Exception):
    pass

# Number to be guessed
number_to_guess = 7

while True:
    try:
        user_input = int(input("Enter your number: "))

        if user_input > number_to_guess:
            raise ValueTooLarge
        elif user_input < number_to_guess:
            raise ValueTooSmall
        else:
            print("Congratulations! You guessed the correct number.")
            break

    except ValueTooLarge:
        print("Value is too large! Try again.")
    except ValueTooSmall:
        print("Value is too small! Try again.")
    except ValueError:
        print("Invalid input! Please enter a number.")
