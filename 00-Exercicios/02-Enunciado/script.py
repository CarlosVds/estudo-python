# numberEntered = input('Enter a number: ')

# try:
#     if int(numberEntered) % 2 == 0:
#         print(f'Number {numberEntered} is "EVEN"')
#     else:
#         print(f'Number {numberEntered} is "ODD"')    
# except:
#     numberEntered.isdigit()
#     print(f'"{numberEntered}", This is not a number') 

desiredTime = input("What time is: ")

try:
    if (int(desiredTime) >= 0) and (int(desiredTime) <= 11):
        print('Good morning')
    elif (int(desiredTime) >= 12) and (int(desiredTime) <= 17):
        print('Good afternoon')
    else:
        print('Good night') 
except:
    print('Only integers ')               