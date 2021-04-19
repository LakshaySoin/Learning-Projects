import sys

def AskUser(numbers):
    try:
        for i in range(9):
            number = input(numbers)
            global num
            num = int(number)
            if len(str(num)) == 9:
                CheckInput(num)
                continue
            else:
                print("No")
            break
    except ValueError:
        print("No")

def CheckInput(num):
    for i in str(num):
        amount = list(str(num)).count(i)
        if amount != 1:
            print("No")
            sys.exit()
        else:
            continue
    print("Yes")


AskUser("Enter your number: ")
