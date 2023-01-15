import json,readline,os,time,os.path

with open('employees.json', "r") as f:
	employees = json.load(f)

userID = input('What is your PIN? > ')

print(employees[userID]['name'])

f.close()