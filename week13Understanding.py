value = input("welcome to the menu. Options are listed below: \n \t 1.Roll \n\t 2.sweep \n\t 3.Scroll \n Type the number of your choice and press.") #\n - newline;

print("value is:",value)
print(f') it is of type {type(value)}.')

while True:
    if value.isdigit() == True: #isdigit
        value = int(value)  # to convert into an int
        #print("converted value is:" , value)
        #print(f') it is of type {type(value)}.')
        break #on correct value datatype: exit the loop
    else:
        value=input("sorry mate, please provide an integer:") #ask for a new value

print("converted value is:" , value)
print(f') it is of type {type(value)}.')



