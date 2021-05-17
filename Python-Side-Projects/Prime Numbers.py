def isPrime(num):
   counter = 2
   if num <= counter:
      return True
   else:
      while num != counter:
         if num % counter == 0:
            return False
            break
         else:
            counter += 1
            if num == counter:
               return True
               break
            else:
               continue


for i in range(1, 20):
   if isPrime(i + 1):
      print(i + 1, end=" ")


