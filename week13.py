value = input("Welcome to the menu. Options are listed below: \n\t 1. Roll \n\t 2. sweep \n\t 3. Scroll \n Type the number of your choice and press Enter.") #\n - newline; \t-tab

#print("The value you input is:",value)
#print(f'it is of type {type(value)}.')

def funcl(val):
    return val**val
def func2(val):
    return val**val
def func3(val):
    return val**val

while True:
    if value.isdigit() == True:
        value = int(value)
        if value > 3 or value < 1:
            value = input("please input a number between 1 and 3.")
            continue
        break #on correct value datatype: exit the loop
    else:
        value=input("ivalid input, please provide an integer:")

#print("The converted is:", value)
#print(f'it is of type {type(value)}.')

if value == 1:
    print(func1(value))
elif value == 2:
    print(func2(value))
elif value == 3:
    print(func3(value))


