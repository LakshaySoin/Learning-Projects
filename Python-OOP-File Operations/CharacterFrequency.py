#Author: Lakshay Soin
#Finds the amount of characters in the file that the user inputs interactively

from os import strerror

dict = {}

name = input("Enter a file name: ")
try:
	for t in open(name, "rt"):
		for i in t:
			b = i.lower() 
			if b.isalpha() == True:
				if b in dict.keys():
					dict[b] += 1
				else:
                			dict[b] = 1
	for x in dict.items():
		print(x[0] + " -> " + str(x[1]))
except IOError as e:
	print("Error: " + strerror(e.errno))
    
