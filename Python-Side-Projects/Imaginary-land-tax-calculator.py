income = float(input("Enter the annual income: "))

if income <= 85528:
   tax = (0.18 * income) - 556.2
else:
   tax = 14839.2 + ((income - 85528) * 0.32)


tax = round(tax, 0)
if tax <= 0:
   tax = 0
print("The tax is:", tax, "thalers")

