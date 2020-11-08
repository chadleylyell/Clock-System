import readline,os,os.path,pyfiglet

def headerGenerator():
	os.system('clear')
	print('Type the name of your company below. \n')
	companyName = input('Company Name> ')
	isCorrect = input('Is "' + companyName + '" the correct spelling of your company? \ny/N >')
	
	if isCorrect.lower() == 'y':
		companyBanner = pyfiglet.figlet_format(companyName)
		print(companyBanner)
	elif isCorrect.lower() == 'n':
		Main()
	else:
		print('"' + isCorrect + '" is not a valid response. Please type Y or N.')