####################################################################################
#  ©2020 Chadley Lyell                                                             #
#  You may not redistribute as yours unless you have written consent from Chadley  #
#  Twitter: @chad_lyell                                                            #
#  Email: chad.lyell@protonmail.com                                                #
####################################################################################

import os,time,readline,hashlib,os.path,platform

from functions import *


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
exitSentence = color['RED'] + '[Now Exiting!] ' + color['DEFAULT'] +'Clock System\n'
exit = False
noRun = 'You are not allowed to enter that command here!'
credits = '©2020 Chadley Lyell\n' + color['TWITTER_BLUE'] + 'Twitter: @chad_lyell' #Yes, I made this during quarantine.
startPhrase = 'Type "help" to begin!\n'
# os.system(clear) # This will clear the screen for a nice and clean interface!

# os.system('chflags hidden db') # Make sure this file is in same directory that you are running this script from.
passwordFile = open('db','r+') # Make sure this file is in same directory that you are running this script from.
secretPassword = passwordFile.read()

# os.system('chflags hidden header')
companyHeader = open('header','r+')
header = companyHeader.read()



def Main():
	# clear()
	print(header)
	headerGenerator()
	print(color['RED'] + '[ERROR] Your operating system is currently not supported!\nPlease open a new issue here:\n' + color['TWITTER_BLUE'] + 'https://github.com/chadleylyell/Clock-System/issues\n' + color['DEFAULT'])
	input('Test> ')
	terminate()

def addPassword():
	mystring = input('Please set a password: ')
	hash_object = hashlib.sha512(mystring.encode())
	hex_dig = hash_object.hexdigest()
	passwordFile.write(hex_dig)
	os.system('clear')
	print('Your password has been set!')
	time.sleep(1)
	os.system('clear')
	print(header + startPhrase)
	Main()

def passwordCheck():
	if secretPassword == '':
		addPassword()
	else:
		print(header + startPhrase)
		Main()

def setupStatus():
	if setupStatus == '':
		runSetup()
	else:
		passwordCheck()



while exit == False:
    # setupStatus()
    Main()