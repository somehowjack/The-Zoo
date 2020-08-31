theSeven = ["seen/seven/READme.txt","seen/animals/penguin/penguin.txt", "seen/animals/octopus/octopus.txt", "seen/animals/vulture/vulture.txt", "seen/animals/jackal/jackal.txt", "seen/animals/rat/rat.txt", "seen/animals/polarBear/polarBear.txt", "seen/animals/komodoDragon/dragon.txt", "seen/seven/theParade.txt"]

willsFaves = ["seen/animals/jackal/jackal.txt", "seen/trees/now.txt", "seen/trees/fukuerika.txt"]

def runFunc(album):
  print("-----------------------------")
  y = "null"
  for file in album:
    y = open(file , "r")
    print(y.read())
    y.close()
    input("-----------------------------\nWHEN YOU'RE READY PRESS ENTER\n-----------------------------")
  print("i hope you understand now")
    


