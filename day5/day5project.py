import random
letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
         'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols=['#', '$', '%', '&', '*', '+', '/', '?', '@', '[', ']', '^', '_','{', '|', '}', '~']

print("Welcome to Password Generator")
ui_letters=int(input("Enter how many letters would you like in your password :\n"))
ui_numbers=int(input("Enter how many numbers would you like in your password :\n"))
ui_symbols=int(input("Enter how many symbols would you like in your password :\n"))


# Easy password
# password = ""
# for letter in range(0,ui_letters):
#     password += random.choice(letters)
#
# for number in range(0,ui_numbers):
#     password+=random.choice(numbers)
#
# for symbol in range(0,ui_symbols):
#     password+=random.choice(symbols)
#
# print(f"Your Password is:{password}")


# Strong Password
password_list = []
for letter in range(0,ui_letters):
    password_list += random.choice(letters)

for number in range(0,ui_numbers):
    password_list +=random.choice(numbers)

for symbol in range(0,ui_symbols):
    password_list +=random.choice(symbols)

random.shuffle(password_list)

new_pass = ""
for pas in password_list:
    new_pass += pas

print(f"Your Password is:{new_pass}")




