listDir = ["seen/seven/READme.txt","seen/animals/penguin/penguin.txt", "seen/animals/octopus/octopus.txt", "seen/animals/vulture/vulture.txt", "seen/animals/jackal/jackal.txt", "seen/animals/rat/rat.txt", "seen/animals/polarBear/polarBear.txt", "seen/animals/komodoDragon/dragon.txt", "seen/seven/theParade.txt"]

def runFunc():
  print("-----------------------------")
  y = "null"
  for file in listDir:
    y = open(file , "r")
    print(y.read())
    y.close()
    input("-----------------------------\nWHEN YOU'RE READY PRESS ENTER\n-----------------------------")
  print("i hope you understand now")
    

