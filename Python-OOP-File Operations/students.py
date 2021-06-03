import random

first_name = ["John", "Anna", "Andrew", "Bob", "Harry"]
last_name = ["Smith", "Boleyn", "Cox", "James", "Potter"]
for i in range(random.randrange(1, 100)):
		print first_name[random.randint(0, len(first_name) - 1)], last_name[random.randint(0, len(last_name) - 1)], random.randint(1, 100)
