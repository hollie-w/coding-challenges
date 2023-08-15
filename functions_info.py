#Types of functions

def some_function(name, job):
 print(name, 'is a', job)
some_function('Fiona', 'developer')
some_function('developer', 'Fiona')
# Positional arguments where order matters

def some_function(name,job):
    print(name, 'is a', job)

some_function(name='Fiona', job = 'developer')
#Keyword arguments where order does not matter

def some_function(name, job='developer'):
    print(name, 'is a', job)
some_function('Fiona')
some_function('Fiona', 'manager')
#default arguments have default values if that argument is not defined

def sum(x, y):
    return x + y
result = sum(10, 15)
print("result is: {}".format(result))
# Importance of using return statement otherwise returns 'None'
