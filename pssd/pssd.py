import random

letters = "QWERTYUIOPASDFGHJKLZXCVBNM"
nums = "1234567890"
chars = "!@#$%^&*()_+-={|}:<?/';[]\>"
print("Your password is : ") 
print("\n")
for i in range(1, 13):
    print(random.choice(letters + nums + chars), end="")
print("\n")
print("***Do not share your password***")
print("\n")