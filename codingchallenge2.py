def list_sort(list, order):
    
    for i in range(len(list)):
        list[i] = int(list[i])
# convert each item to int type and list in python

    if order == "asc":
        print(sorted(list))

    elif order == "desc":
        print(sorted(list, reverse=True))

    elif order == "none":
        print(list)
    
    else:
        print("error")

list = [1,2,3,4,5]
list_sort(list, "desc")

#function where you enter a list of numbers and choice of sorting