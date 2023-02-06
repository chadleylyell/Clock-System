import os,time,readline,hashlib
import PySimpleGUI as sg

sg.theme('DarkBrown4')
mainFont = ("Arial", 40,)

layout = [ 
  [sg.Text('This is a template window', font=mainFont, pad=((0,0),(100,100)))],
    ]

window = sg.Window('Template Window', layout, element_justification="center")

while True:
  event, values = window.read()
  if event == sg.WIN_CLOSED:
    break
window.close()