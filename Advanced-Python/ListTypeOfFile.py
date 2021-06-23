import os

class Directory:
	def __init__(self, name, ext):
		self.entries = os.listdir(name)
		self.ext = ext

	def findfiles(self):
		for i in self.entries:
			if "." not in i:
				temp = os.listdir(name + "/" + i)
				for x in temp:
					if self.ext in x:
						print(i + "-->")
						print(x)
						print("_________________________")
			if self.ext in i:
				print(i)	

try:
	name = str(input("Enter the directory: "))
	ext = str(input("Enter the extension: "))
	obj = Directory(name, ext)	
	obj.findfiles()
except ValueError:
	print("Error: Invalid Input")
