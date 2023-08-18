def card_mask(card):
    print("*" * (len(card) - 4) + card[-4:])

# prints the length of the number lots of *s -4 digits from the end then adds on the last 4 digits

def password_mask(password):
    print("X" * (len(password)-2) + password[-2:])

#prints a password masked except the last two items

card_mask("1230405353925")
password_mask("helloiamhollie")

#function to mask the digits of a card number and password