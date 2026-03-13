correct_password = "python123"
chance = 3

while chance>0:
    enter = input("Enter Password: ")

    if enter == correct_password:
        print("Your password is correct.")
        break
    elif chance == 0:
        print("Access denied.")
    else:
        chance -= 1
        print("Password incorrect. You have", chance, "chance left.")
