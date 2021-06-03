import os

class Directory:
	def findfiles(self, name):
		entries = os.listdir(name)
		for i in entries:
			if ".py" in i:
				print(i)	

obj = Directory()
try:
	name = str(input("Enter the directory: "))
	obj.findfiles(name)
except ValueError:
	print("Error: Invalid Input")
