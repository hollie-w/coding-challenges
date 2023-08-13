user_word = str(input("Please enter a word"))
count = 0
i = 0

for i in range(len(user_word)):
    if (
        (user_word[i] == "a")
        or (user_word[i] == "e")
        or (user_word[i] == "i")
        or (user_word[i] == "o")
        or (user_word[i] == "u")
    ):
        count += 1

print("There are {} vowels in the word {}". format(count, user_word))
