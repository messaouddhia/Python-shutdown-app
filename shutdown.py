import os
from sys import exit


shutdown = input("Do you wish to shutdown your computer ? (yes/no)")



if shutdown == "no":
  exit()
else:
  timer = input("Pick a time (30mins,1hour,2hours,3hours).")
  checktime()

def checktime():
  if timer== "30mins":
    os.system("shutdown /s /t 1800")
  elif timer=="1hour":
    os.system("shutdown /s /t 3600")
  elif timer =="2hours":
    os.system("shutdown /s /t 7200")
  elif timer == "3hours":
    os.system("shutdown /s /t 10800")
  else:
    print("Please enter a valid answer.")
    



