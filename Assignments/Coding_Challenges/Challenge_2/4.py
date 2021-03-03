# 4. User input
age = input("What is your age?")

years=65-int(str(age))

print("There is" + " "+str(years) + " years until you reach retirement")

# Feedback - Fixed print statements, but I throw an error TypeError: unsupported operand type(s) for -: 'int' and 'str'
# this is becasue you do not convert the str input to an int. I have added the correct type conversion.