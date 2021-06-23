import os
  
class Directory:
	def __init__(self, name):
		self.entries = os.listdir(name)

	def findfiles(self):
		for i in self.entries:
			if "." not in i:
				temp = os.listdir(name + "/" + i)
				print(i + "-->")	
				for x in temp:
					print(x)
				print("_________________________")
			print(i)
			
try:
	name = str(input("Enter the directory: "))
	obj = Directory(name)
	obj.findfiles()
except ValueError:
        print("Error: Invalid Input")
