# Quiz Game
# Author: Leon
# Date: Dec 4

counter = 0

Answer_one = input(
    "Welcome to the Quiz. Answer each question to the best of your abilities. First question! what is 8 / 2(2+2)").lower()

if Answer_one == str(16) or Answer_one == "sixteen".lower():
    print("Correct!")
    counter += 1
elif Answer_one != 16 or Answer_one != "sixteen".lower():
    print("Sorry Wrong Answer")

Answer_two = input("Next question! What is Obama's last name?").lower()

if Answer_two == "Obama".lower():
    print("Correct!")
    counter += 1
elif Answer_two != "Obama":
    print("Sorry Wrong Answer")

Answer_three = input("Next question! What is the value for ∛(-8)? Is it A)2 B)2 or -2. C)-2 D) N/A").lower()

if Answer_three == "C".lower() or Answer_three == "-2":
    print("Correct!")
    counter += 1
elif Answer_three != "C".lower() or "-2":
    print("Sorry wrong answer!")

Answer_four = input(
    "Next question! What is the first name of the person in the famous painting known as the Mona Lisa").lower()

if Answer_four == "Lisa".lower():
    print("Correct!")
    counter += 1
elif Answer_four != "Lisa".lower():
    print("Incorrect")

Answer_five = input("Next question! What is 3 x 3 - 4?").lower()

if Answer_five == "5" or Answer_five == "Five".lower():
    print("Correct!")
    counter += 1
elif Answer_five != "5" or Answer_five != "Five".lower():
    print("incorrect")

print(f"{int(counter) / 5 * 100} %")