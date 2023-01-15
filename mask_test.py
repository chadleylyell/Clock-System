import stdiomask,datetime,os,readline

exit = False

def Main():

test = stdiomask.getpass(prompt = 'Password: ')

birthday = input('Employee birthday (YYYY-MM-DD) > ')
year, month, day = map(int, birthday.split('-'))
formattedBirthday = datetime.date(year, month, day)

print(year)
print(datetime.datetime.today())


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