from os import strerror

class Files:
	def args(self, name):
		try:
			file = open(name, "rt")
			ch = file.read()
			cnt = 0
			for letter in ch:
				cnt += 1
			if cnt > 40:
				print(ch)
			file.close()
		except IOError as e:
			print("There was a problem: " + strerror(e.errno))

obj = Files()
try:
	amount = int(input("How many files would you like to open: "))
	for i in range(amount):
		files = str(input("Enter the name of the file: "))
		obj.args(files)
except ValueError:
	print("Error: Invalid Input")

