def Fib(args):
		num1 = num2 = 1
		for i in range(args):
			if i in [0,1]:
				yield 1
			else:
				output = num1 + num2
				num1,num2 = num2,output
				yield output

print(list(Fib(10)))
