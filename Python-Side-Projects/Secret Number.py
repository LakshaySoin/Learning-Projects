secret_number = 777

print(
   """
   +================================+
   | Welcome to my game, muggle!    |
   | Enter an integer number        |
   | and guess what number I've     |
   | picked for you.                |
   | So, what is the secret number? |
   +================================+
   """)
num = int(input("Enter an integer: "))

while num != secret_number:
   print("Ha ha! You're stuck in my loop!")
   if num > secret_number:
       num -= 1
       print("Ha ha! You're stuck in my loop!")
   else:
       num += 1
       print("Ha ha! You're stuck in my loop!")
else:
   print("Well done, muggle! You are free now.")


