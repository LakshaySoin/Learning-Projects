class Reverse:
	def __init__(self, *args):
		self.vals = list(args)
		self.new_lst = []
		self.len = len(self.vals)

	def rev(self):
		for i in range(self.len):
			self.new_lst.append(self.vals[self.len - (i + 1)])
						
obj = Reverse(0, 1, 2, 3, 4, 5)
obj.rev()
print(obj.new_lst)
