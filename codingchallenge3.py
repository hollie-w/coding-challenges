def vowels(user_word):
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

#Creates a function that accepts a single word and returns the number of vowels in that word.

vowels("robot")