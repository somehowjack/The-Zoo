import os
from functions import intro 
from functions import theSeven
from functions import directory

intro.titleText()

'''file = open("theCages", "r")
file = file.read()'''

print("type help at anytime for commands")

while True:
  print('"theSeven" or "freeReign"')
  option = input("\nWHAT DO YOU CHOOSE? ")
  if option == "freeReign":
    directory.directoryM()
  if option == "theSeven":
    theSeven.runFunc()

