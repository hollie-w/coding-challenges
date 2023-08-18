def oxcount(text):
    countx = 0
    counto = 0
    i = 0

    for i in range(len(text)):
        if (
            text[i] == "X"
            or text[i] =="x"
        ):
            countx +=1
    
        if (
            text[i] == "O"
            or text[i] == "o"
        ):
            counto +=1
    
    same = countx == counto
    print(same)

#creates a python function that accepts a string
#if the string contains the same number of X's and O's, prints Bolean statement True
#if not prints false

oxcount("hexagon")