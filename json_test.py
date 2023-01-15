import json,readline,os,time,os.path

with open('employees.json', 'r') as f:
    employees = json.load(f)

nameInput = input('What is your name? > ')
ageInput = input('How old are you? > ')
userID = input('What would you like your PIN to be? > ')

employees[userID] = {'name': nameInput, 'age': ageInput}

with open('employees.json', 'w') as f:
    json.dump(employees, f)

f.close()