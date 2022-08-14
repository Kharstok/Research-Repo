
#-------------------------------------------------------------------------------
# Human Years to Dog Years
## took 1.22 hrs.. :(
#-------------------------------------------------------------------------------

# hyInput = ""

# while(hyInput != int):
#     try:
#         hyInput = int(input("Input a dogs age in human years:  "))
#     except:
#         print("Please enter a whole number e.g 1, 47, 380..")
#     else:
#         break

# if hyInput > 2:
#     first = (2)*10.5
#     second = (hyInput-2)*4
#     age = first + second
# else:
#     age = hyInput * 10.5

# print(f'Your dog is {age} years old.')

#------------------------------------------------------------------------------
# Convert Month name to Number of Days
## took.. a long time probably
#------------------------------------------------------------------------------

# class months:
#     def __init__(self, num, name, days):
#         self.num = num
#         self.name = name
#         self.days = days

# list = []

# list.append( months('1', 'January', '31'))
# list.append( months('2', 'February', '28 (29 in a leap year)'))
# list.append( months('3', 'March', '31'))
# list.append( months('4', 'April', '30'))
# list.append( months('5', 'May', '31'))
# list.append( months('6', 'June', '30'))
# list.append( months('7', 'July', '31'))
# list.append( months('8', 'August', '31'))
# list.append( months('9', 'September', '30'))
# list.append( months('10', 'October', '31'))
# list.append( months('11', 'November', '30'))
# list.append( months('12', 'Decemeber', '31'))


# userInput = input("Please input a month name or number: ")

# for obj in list:
#     if userInput == obj.name:
#         print(f'{obj.name} has {obj.days} days and is the {obj.num} month of the year')

## Issues. 
## was not properly referring to list items
# for obj in list:
#     if userInput == months.name:
#         print(f'{months.name} has {months.days} days and is the {months.num} month of the year')

# # Should instead be

#         for obj in list:
#     if userInput == obj.name:
#         print(f'{obj.name} has {obj.days} days and is the {obj.num} month of the year')

#------------------------------------------------------------------------------
# Challenge
## took
#------------------------------------------------------------------------------

# equation = (f'{n} * {N} = {N*n}')

for n in range(1-11) and for N in range(1-13):
    while N != 12 and n !=10:
        print(f'{N} * {n} = {N*n}')
