year = int(input("Enter a year: "))

if year < 1582:
    print("Not within the Gregorian calendar period")
elif year % 4 > 0:
    print("This year is a common year")
elif year % 100 > 0:
    print("This year is a leap year")
elif year % 400 > 0:
    print("This year is a common year")
else:
    print("This year is a leap year")


