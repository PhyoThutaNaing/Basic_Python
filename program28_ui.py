import tkinter as tk

# Custom Exceptions
class ValueTooLarge(Exception):
    pass

class ValueTooSmall(Exception):
    pass

# Number to guess
number_to_guess = 7

# Function to check input
def check_number():
    try:
        user_input = int(entry.get())

        if user_input > number_to_guess:
            raise ValueTooLarge
        elif user_input < number_to_guess:
            raise ValueTooSmall
        else:
            result_label.config(text="🎉 Correct! You guessed it!", fg="green")

    except ValueTooLarge:
        result_label.config(text="Too large! Try again.", fg="red")
    except ValueTooSmall:
        result_label.config(text="Too small! Try again.", fg="orange")
    except ValueError:
        result_label.config(text="Invalid input! Enter a number.", fg="blue")


# Create window
root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("350x200")

# Title label
title_label = tk.Label(root, text="Guess the Number (1-10)", font=("Arial", 14))
title_label.pack(pady=10)

# Entry box
entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=5)

# Button
check_button = tk.Button(root, text="Check", command=check_number)
check_button.pack(pady=10)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack()

# Run app
root.mainloop()
