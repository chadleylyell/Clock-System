####################################################################################
#  ©2017 Chadley Lyell                                                             #
#  You may not redistribute as yours unless you have written consent from Chadley  #
#  Twitter: @chad_lyell                                                            #
#  Email: contact@chadleylyell.me                                                  #
####################################################################################

import os,time,readline,hashlib,os.path

from functions import headerGenerator

color = {
    'RED'              : '\033[1;91m',
    'UNDERLINE_PURPLE' : '\033[4;34m',
    'GREEN'            : '\033[1;92m',
    'YELLOW'           : '\033[1;33m',
    'CYAN'             : '\033[0;36m',
    'PURPLE'           : '\033[0;34m',
    'MAGENTA'          : '\033[0;35m',
    'DEFAULT'          : '\033[0m',
    'TWITTER_BLUE'     : '\033[38;5;33m',
}

incorrect = 'Wrong password! ' # You can change this to say whatever you like!
exitSentence = color['RED'] + '[Now Exiting!] ' + color['DEFAULT'] +'Folder Locker\n'
exit = False
noRun = 'You are not allowed to enter that command here!'
credits = '©2020 Chadley Lyell\n' + color['TWITTER_BLUE'] + 'Twitter: @chad_lyell' #Yes, I made this during quarantine.
os.system('clear') # This will clear the screen for a nice and clean interface!

os.system('chflags hidden db') # Make sure this file is in same directory that you are running this script from.
passwordFile = open('db','r+') # Make sure this file is in same directory that you are running this script from.
secretPassword = passwordFile.read()

os.system('chflags hidden header')
companyHeader = open('header','r+')
header = companyHeader.read()



def Main():
	global exit
	print('Hello World!')
	headerGenerator()
	exit = True

def addPassword():
	global exit
	mystring = input('Please set a password: ')
	hash_object = hashlib.sha512(mystring.encode())
	hex_dig = hash_object.hexdigest()
	passwordFile.write(hex_dig)
	os.system('clear')
	print('Your password has been set!')
	time.sleep(1)
	os.system('clear')
	print(header + 'Type "help" to begin!\n')
	Main()

def passwordCheck():
	if secretPassword == '':
		addPassword()
	else:
		print(header + 'Type "help" to begin!\n')
		Main()

def setupStatus():
	if setupStatus == '':
		runSetup()
	else:
		passwordCheck()

while exit == False:
    # setupStatus()
    Main()