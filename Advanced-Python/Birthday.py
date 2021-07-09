class Birthday:
	def __init__(self, date):
		self.date = date
		self.special_date1 = ['07','09'] # Replace with month and day of birthday
		self.special_date2 = ['07','12'] # Replace with month and day of birthday
		self.special_date3 = ['10','25'] # Replace with month and day of birthday
		self.special_date4 = ['12','28'] # Replace with month and day of birthday
		# Add special_dates if necessary

	def check_date(self):
		if self.special_date1 == self.date[0:2]:
			print("Happy Birthday!")
		elif self.special_date2 == self.date[0:2]:
			print("Happy Birthday!")
		elif self.special_date3 == self.date[0:2]:
			print("Happy Birthday!")
		elif self.special_date4 == self.date[0:2]:
			print("Happy Birthday!")
		else:
			print("There is no special birthday today.")

while True:
	date = str(input("What is the date today (Enter in the format mm/dd/yyyy or enter q to quit) : "))
	for i in date:
		if i.isalpha == True:
			print("Only numbers and symbols are allowed")
	if date == 'q':
		break
	elif len(date) != 10:
		print("Invalid Input. Please enter a 0 if necessary.") 
	else:
		date = date.split("/")
		obj = Birthday(date)
		obj.check_date()
