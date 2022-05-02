
i=0
def input_function():
    a=int(input("Enter a number:"))
    b = int(input("Enter b number:"))
    if a<b:
        return a,b
    elif a>b:
        return b,a

def sum_of_numbers():
    numbers=input_function()
    return sum(range(numbers[0],numbers[1]))



print(sum_of_numbers())
