import math
def rad_deg(radians):
    degrees = radians * (180/math.pi)
    msg = "Your angle is {} degrees". format(degrees)
    print(msg)

rad_deg(3)
#function to convert user's angle in radians into degrees

