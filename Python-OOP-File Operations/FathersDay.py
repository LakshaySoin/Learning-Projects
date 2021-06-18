from random import randint

class FathersDay:
	def __init__(self, name):
		self.name = name.upper()
		self.random_message = randint(0, 4)
		self.mes = {'A':['Awesome','Adorable','Adventurous','Amazing'],
			   'B':['Beautiful','Beaming','Brilliant','Beneficial'],
			   'C':['Champion','Celebrated','Charming','Curious'],
			   'D':['Delightful','Dazzling','Delicious','Distinguished'],
			   'E':['Elegant','Ecstatic','Effective','Extraordinary'],
			   'F':['Fabulous','Fantastic','Flourishing','Faithful'],
			   'G':['Glamorous','Generous','Genius','Gorgeous'],
			   'H':['Harmonious','Happy','Heartwarming','Heavenly'],
			   'I':['Imaginative','Innovating','Impressive','Intuitive'],
			   'J':['Joyous','Jolly','Jubilant','Jovial'],
			   'K':['Knowledgeable','Kind','Keen','Kingly'],
			   'L':['Lovely','Luminous','Lively','Legendary'],
			   'M':['Marvelous','Masterful','Majestic','Magnificent'],
			   'N':['Nutritious','Noble','Natural','Nice'],
			   'O':['Outstanding','Optimistic','Observant','Outgoing'],
			   'P':['Phenomenal','Positive','Productive','Pleasant'],
			   'Q':['Quick','Queenly','Quality','Quiet'],
			   'R':['Remarkable','Reassuring','Respected','Righteous'],
			   'S':['Stupendous','Skillful','Sparkling','Spectacular'],
			   'T':['Thrilling','Thorough','Terrific','Trustworthy'],
			   'U':['Upbeat','Understanding','Unique','Upstanding'],
			   'V':['Victorious','Vigorous','Valuable','Versatile'],
			   'W':['Wholesome','Wealthy','Wise','Wonderful'],
			   'X':['Xoxo','Xeric','Xenial','Xenogeneic'],
			   'Y':['Yummy','Youthful','Yeasty','Yielding'],
			   'Z':['Zealous','Zestful','Zippy','Zany'],
			   }

	def message(self):
		for letter in self.name:
			if letter in self.mes:
			 	print(self.mes[letter][self.random_message])
			else:
				print()

while True:
	name = str(input('Enter your name: '))
	if name.replace(' ','').isalpha() != True:
		break
	obj = FathersDay(name.strip())
	obj.message()
	exit = str(input('Would you like to continue (e to exit): '))
	if exit[:1].lower() == 'e':
		break
