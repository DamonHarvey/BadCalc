import random
import time

first_num: int
second_num: int
sign: str

while True:

    first_num = int(input("Enter first number: "))

    if -100 < first_num < 100:
        break
    else:
        print("number to hard")

while True:

    second_num = int(input("Enter second number: "))

    if -100 < second_num < 100:
        break
    else:
        print("number to hard")

while True:

    sign = input("+ or - or x or /: ")

    if sign == "+":
        number = first_num + second_num
        break
    elif sign == "-":
        number = first_num - second_num
        break
    elif sign == "x":
        number = first_num * second_num
        break
    elif sign == "/":
        number = int(first_num / second_num)
        break
    else:
        print("to hard")


guess_list = [x for x in range(number - 1000, number + 1000)]
random.shuffle(guess_list)

x = 0
while True:
    guess = guess_list.pop()
    print(f"guessing: {guess}")
    time.sleep(0.01)

    if guess == number:
        print(f"the answer is: {number} {x}")
        break

    x += 1
