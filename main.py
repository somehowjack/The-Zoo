from functions import intro 
from functions import albumList
from functions import directory

intro.titleText()

'''nothing really interesting in here'''

print("pick something")

while True:
  print('POETRY ALBUMS:\n"parade" "forest" "favorites",\nOTHER:\n"fileBrowser"')
  option = input("\nWHAT DO YOU CHOOSE? ")
  if option == "fileBrowser":
    directory.directoryM()
  if option == "parade":
    albumList.runFunc(albumList.theSeven)
  if option == "favorites":
    albumList.runFunc(albumList.willsFaves)

