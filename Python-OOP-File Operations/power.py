Class Fib:
	def __init__(self, args):
		self.max = args
		self.i = 0
		self.num1 = self.num2 = 1

	def Add(self):
		self.i += 1
		if self.i > self.max:
			raise StopIteration
		if self.i in [1,2]:
			return 1
		output = self.num1 + self.num2
		self.num1,self.num2 = self.num2,output
		yield output

for i in Fib(10):
	print(i)
