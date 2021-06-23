import os
from os import strerror

class Files:
	def __init__(self, name, ext):
		self.entries = os.listdir(name)
		self.ext = ext
		self.lcnt = 0

	def check(self):
		try:
			for i in self.entries:
				if "." not in i:
					temp = os.listdir(name + "/" + i)
					for x in temp:
						if self.ext in x:
							for _ in open(x, "rt"):
								self.lcnt += 1
							print(i + "-->")
							print(x + "-" + str(self.lcnt))
							print("_________________________")
				if self.ext in i:
					for _ in open(i, "rt"):
						self.lcnt += 1
					print(i + "-" + str(self.lcnt))
		except IOError as e:
			print("There was a problem: " + strerror(errno.e))

try:
	name = str(input("Enter the directory: "))
	ext = str(input("Enter the extension: "))
	obj = Files(name, ext)
	obj.check()
except ValueError:
        print("Error: Invalid Input")
