import random

a = True
while a:
    num = random.randint(1,6)
    if num == 1:
            print("  1")
            print("[   ]")
            print("| O |")
            print("[   ]")
    if num == 2:
            print("  2")
            print("[O  ]")
            print("|   |")
            print("[  O]")
    if num == 3:
            print("  3")
            print("[O  ]")
            print("| O |")
            print("[  O]")    
    if num == 4:
            print("  4")
            print("[O O]")
            print("|   |")
            print("[O O]")
    if num == 5:
            print("  5")
            print("[O O]")
            print("| O |")
            print("[O O]")
    if num == 6:
            print("  6")
            print("[OOO]")
            print("|OOO|")
            print("[OOO]")  

    roll = input("Re-roll? (y/n): ")
    if roll.lower() == "y":
        continue
    else:
        break
     
