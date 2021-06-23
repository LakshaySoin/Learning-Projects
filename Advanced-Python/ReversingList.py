class Reverse:
	def __init__(self, *args):
		self.vals = list(args)	
		self.original_length = len(self.vals)
		self.count = 0
	
	def __iter__(self):
		return self

	def __next__(self):
		if self.count == self.original_length:
			raise StopIteration
		self.count += 1
		num = self.vals[-1]
		del self.vals[-1]
		return num

for i in Reverse(10, 11, 12, 13, 14):
	print(i, end = " ")
print()
		
		
