card = str(input("Please enter your card number"))
print("*" * (len(card) - 4) + card[-4:])

# prints the length of the number lots of *s -4 digits from the end then adds on the last 4 digits

password = str(input("Please enter your password"))
print("X" * (len(password)-2) + password[-2:])

#prints a password masked except the last two items