
# i

import math
def sphere_volume(r):
    return ((4*math.pi*(r**3))/3)

# ii
#print(sphere_volume(3))

# iii
def sphere_area(r):
    return ((r**2)*math.pi)
#print(sphere_area())

def sphere(r):
    return "volume: {} and area: {} ".format(sphere_volume(r),sphere_area(r))

print(sphere(3))





