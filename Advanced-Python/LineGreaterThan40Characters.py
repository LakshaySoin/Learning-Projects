from os import strerror

class Files:
	def __init__(self, name):
		try:
			self.file = open(name, "rt")
			self.ch = self.file.readline()
			self.cnt = 0
		except IOError as e:
			print("There was a probelm: " + strerror(e.errno))

	def args(self):
		while self.ch != '':
			for _ in self.ch:
				self.cnt += 1	
			if self.cnt > 40:
				print(self.ch)
			self.ch = self.file.readline()
		self.file.close()

try:
	amount = int(input("How many files would you like to open: "))
	for _ in range(amount):
		files = str(input("Enter the name of the file: "))
		obj = Files(files)
		obj.args()
except ValueError:
	print("Error: Invalid Input")

