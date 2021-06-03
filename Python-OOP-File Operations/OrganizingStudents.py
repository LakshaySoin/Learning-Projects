from os import strerror

class Read:
	try:
		dict = {}
		ask = input("Enter a file name: ")
		file = open(ask, "rt")
		read = file.read().split()
		i = 0
		count = 2
		dict = {}
		while (count) <= len(read):
			if (read[i] + read[i + 1]) in dict.keys(): 
				dict[read[i] + read[i + 1]] += float(read[count])
                                count += 3
                                i += 3
			else:
				dict[read[i] + read[i + 1]] = float(read[count])
                                count += 3
                                i += 3	
		for x,y in dict.items():
			print(x,y)
		file.close()
	except IOError as e:
		print("Sorry: " + strerror(e.errno))
		exit(e.errno) 		
