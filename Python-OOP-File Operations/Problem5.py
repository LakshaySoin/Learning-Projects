import os
from os import strerror

class Files:
	def check(self, name):
		try:
			lcnt = 0	
			entries = os.listdir(name)
			for i in entries:
				if ".py" in i:
					for line in open(i, "rt"):
						lcnt += 1
					print(lcnt)
		except IOError as e:
			print("An error occured: " + strerror(e.errno))

obj = Files()
obj.check("/Users/lakshaysoin/desktop/Python File")
