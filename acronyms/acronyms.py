user_input =str(input("Enter the word/phrase: "))
acr =user_input.split()
a = " "
for i in acr:
    a = a +str(i[0]).upper()

print(a)