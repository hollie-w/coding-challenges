y = input("Please enter your text")
countx = 0
counto = 0
i = 0

for i in range(len(y)):
    if (
        y[i] == "X"
        or y[i] =="x"
    ):
        countx +=1
    
    if (
        y[i] == "O"
        or y[i] == "o"
    ):
        counto +=1
    
same = countx == counto
print(same)

#creates a python file that accepts a string from the user
#if the string contains the same number of X's and O's, prints Bolean statement True
#if not prints false