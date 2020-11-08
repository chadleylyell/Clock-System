import json,readline,os,time,os.path

with open('employees.json', "r") as f:
	employees = json.load(f)

print(employees['1']['name'])

f.close()