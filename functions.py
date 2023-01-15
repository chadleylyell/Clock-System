import readline,os,os.path,pyfiglet,stdiomask,datetime,readline

def headerGenerator():
	os.system('clear')
	print('Type the name of your company below. \n')
	companyName = input('Company Name> ')
	isCorrect = input('Is "' + companyName + '" the correct spelling of your company? \ny/N >')
	
	if isCorrect.lower() == 'y':
		companyBanner = pyfiglet.figlet_format(companyName)
		print(companyBanner)
	elif isCorrect.lower() == 'n':
		headerGenerator()
	else:
		print('"' + isCorrect + '" is not a valid response. Please type Y or N.')

def addEmployee():
	os.system('clear')
	fName = input('Employee first name > ')
	mName = input('Employee middle name > ')
	lName = input('Employee last name > ')
	birthday = input('Employee birthday (YYYY-MM-DD) > ')
	year, month, day = map(int, birthday.split('-'))
	formattedBirthday = datetime.date(year, month, day)
def social():
	social = stdiomask.getpass(prompt = 'Employee social security number (XXX-XX-XXXX) > ')
	confirmedSocial = stdiomask.getpass(prompt = "Confirm SSN > ")
	if confirmedSocial == social:
		pin = stdiomask.getpass(prompt = 'Employee PIN number > ')
		lName = input('Employee last name > ')
		lName = input('Employee last name > ')
		lName = input('Employee last name > ')
		lName = input('Employee last name > ')
	else:
		print("SSN's did not match. Please try again.")
		social()