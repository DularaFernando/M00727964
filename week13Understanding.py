value = input('''welcome to the menu. Options are listed below:,
              \t 1.Roll 
              \t 2.sweep 
              \t 3.Scroll 
              Type the number of your choice and press.''') #\n - newline; \t - tab

#print("value is:",value)
#print(f') it is of type {type(value)}.')

def func1(val):
    return val**val
def func2(val):
    return val**val
def func3(val):
    return val**val

while True:
    if value.isdigit() == True: #isdigit
        value = int(value)  # to convert into an int
        #print("converted value is:" , value)
        #print(f') it is of type {type(value)}.')
        break #on correct value datatype: exit the loop
    else:
        value=input("sorry mate, please provide an integer:") #ask for a new value

#print("converted value is:" , value)
#print(f') it is of type {type(value)}.')

#compare numeric value to choices availble, perform assicoated function or sequence.
if value == 1:
    print(func1(value))
elif value == 2:
    print(func2(value))
elif value == 3:
    print(func3(value))



