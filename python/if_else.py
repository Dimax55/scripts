
#умовні оператори if / elif / else

user_data = int(input('enter a number:'))

if user_data > 5 and user_data == 6 or user_data ==4:
    print("biggest then five")
    print("nice")
elif user_data < 5:
    print("less then five")
else :
    print("number is five")



isHappy = True

if isHappy == True:
    print("user is happy")
else:
    print("user is not happy")




#тернарні оператори

data =input()
number = 5 if data == "five" else 0
print(number)
