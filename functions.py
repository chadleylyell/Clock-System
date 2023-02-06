import readline,os,os.path,pyfiglet,stdiomask,datetime,platform,sys,readchar

osName = platform.system()
companyHeader = open('header','r+')
header = companyHeader.read()

passwordFile = open('db','r+')
secretPassword = passwordFile.read()

def clear():
	if osName == 'Windows':
		os.system('cls')
	elif osName == 'Linux':
		os.system('clear')
	elif osName == 'Darwin':
		os.system('clear')

def terminate():
	sys.exit()


def createAdmin():
	mystring = input('Please set a password: ')
	hash_object = hashlib.sha512(mystring.encode())
	hex_dig = hash_object.hexdigest()
	passwordFile.write(hex_dig)
	os.system('clear')
	print('Your password has been set!')
	time.sleep(1)
	os.system('clear')
	print(header + startPhrase)

def headerGenerator():
	if header == '':
		os.system('clear')
		print('Type the name of your company below. \n')
		companyName = input('Company Name> ')
		print('Is "' + companyName + '" the correct spelling of your company? \ny/n >')
		isCorrect = readchar.readchar()

		if isCorrect == 'y':
			companyBanner = pyfiglet.figlet_format(companyName)
			companyHeader.write(companyBanner)
			print(header)
		elif isCorrect == 'n':
			headerGenerator()
		else:
			print('"' + isCorrect + '" is not a valid response. Please type Y or N.')
	# else:


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