from functions import intro 
from functions import albumList
from functions import directory

intro.titleText()

'''file = open("theCages", "r")
file = file.read()'''

print("if this is your first time do theSeven")

while True:
  print('"seven", "freeReign", or "willsFaves"')
  option = input("\nWHAT DO YOU CHOOSE? ")
  if option == "freeReign":
    directory.directoryM()
  if option == "seven":
    albumList.runFunc(albumList.theSeven)
  if option == "willsFaves":
    albumList.runFunc(albumList.willsFaves)

