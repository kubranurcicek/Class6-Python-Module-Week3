
#i
def int_return(x):
    return x
print(int_return(10))

#ii
def add(x):
    return x+2
print(add(10))

#iii
def greet(name):
    print("Hello "+name+"! Nice to meet you!")
greet("Bob")

#iv
def total(x):
    sayilar=[*range(0,x+1)]
    print(sum(sayilar))
total(10)

#v
def lenght(x):
    sayilar=[*range(0,x)]
    if x>=5:
        print("Longer than 5")
    else:
        print("Less than 5")
lenght(2)

#vi
def divide(x):
    return x/2

def summ(a):
    return a+6

print(summ(divide(20)))

