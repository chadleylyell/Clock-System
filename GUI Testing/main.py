import os,time,readline,hashlib
import PySimpleGUI as sg

sg.theme('DarkBrown4')
companyName = 'GKA Sales Time Clock'
adminHash = 'a12f40dcc4f5f97b1e491c7cd9cfd523b6aa2caa249a351a09c38a61bb4bfc26b928fe299acad2db0d21caf80d214c4cc0437fb0af234e4cd7ee3799d1e1cbc5'

# STEP 1 define the layout
headFont = ("Arial", 30,)
subtitleFont = ("Arial", 9)

#def mainWindow():
layout = [ 
  [sg.Text(companyName, font=headFont, pad=((0,0),(10,60)))],
  [sg.Text("Please enter passcode:", font=subtitleFont)],
  [sg.InputText(k='passcode', password_char = "True", do_not_clear="False", pad=((0,0),(0,240)))],
  [sg.Button("Submit", pad=((0,0),(0,10)))]
    ]    
  #return sg.Window('Login', layout, finalize=True)

# window = sg.Window(companyName, layout, element_justification="center", no_titlebar=True)
window = sg.Window(companyName, layout,element_justification="center")
# secondWindow = sg.Window(companyName, exitLayout, element_justification="center")

while True:
  event, values = window.read()
  if event == sg.WIN_CLOSED:
    break
  elif event == ('Submit'):
    passcodeSubmit = values['passcode']
    hash_object = hashlib.sha512(passcodeSubmit.encode())
    hex_dig = hash_object.hexdigest()
    if hex_dig == adminHash:
      print("Correct")
      print('You have the admin passcode!')
    else:
      print("Wrong")
window.close()