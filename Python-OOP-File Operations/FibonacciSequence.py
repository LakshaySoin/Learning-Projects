class Fib:
	def __init__(self, arg):
		self.max = arg
		self.i = 0
		self.num1 = self.num2 = 1

	def __iter__(self):
		return self

	def __next__(self):
		self.i += 1
		if self.i > self.max:
			raise StopIteration
		if self.i in [1,2]:
			return 1
		output = self.num1 + self.num2
		self.num1, self.num2 = self.num2, output
		return output

for i in Fib(20):
	print(i)
