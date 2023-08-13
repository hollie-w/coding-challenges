list = input("Enter your list of numbers separated by a space")
print("\n")
user_list = list.split()

for i in range(len(user_list)):
    user_list[i] = int(user_list[i])
# convert each item to int type and list in python

list_order = input("What order would you like your list? Please enter asc, desc or none.")

if list_order == "asc":
    print(sorted(user_list))

elif list_order == "desc":
    print(sorted(user_list, reverse=True))

elif list_order == "none":
    print(user_list)

