def DigitofLife(birthdate):
    num = '0'
    num1 = '0'
    while True:
        try:
            birth = input(birthdate)
            date = int(birth)
            date1 = str(date)
            if len(date1) != 8:
                print("Must be in format YYYYMMDD, or YYYYDDMM, or MMDDYYYY")
                continue
            else:
                for i in date1:
                    num = int(num) + int(i)
                if num > 9:
                    for x in str(num):
                        num1 = int(num1) + int(x)
                    print(num1)
                else:
                    print(num)
            break
        except ValueError:
            print("Wrong input")


DigitofLife("Enter your birthdate (YYYYMMDD, or YYYYDDMM, or MMDDYYYY): ")