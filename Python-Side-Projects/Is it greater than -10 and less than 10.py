def readint(prompt, min, max):
   while True:
      try:
         num = input(prompt)
         prompt = int(num)
         if prompt >= min and prompt <= max:
            return prompt
            break
         else:
            print("Error: the value is not within permitted range")
            prompt = "Enter a number from -10 to 10: "
            continue
      except TypeError:
         print("Error: wrong input")
         continue
      except ValueError:
         print("Error: wrong input")
         continue


v = readint("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)

