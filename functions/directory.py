import os

def isTXT(inputF):
  if ".txt" in inputF:
    return True
  else:
    return False

def incrDir(prev, add):
  prev = prev + add + "/"
  return prev

def negaDir(prev):
  prev = prev.split("/")
  prev.pop(-1)
  prev.pop(-1)
  prev = "/".join(prev) + "/"
  return prev

def fileCont(base, add):
  base = base + add
  base = open(base, "r")
  return base.read()
  base.close()


def directoryM():
  print("type help at any time for a list of commands")

  baseDir = "seen/"
  prevDir = baseDir
  currDir = baseDir
  dirCont = os.listdir(currDir)
  userI = "null"

  ON = True
  while ON:
    dirCont = os.listdir(currDir)
    print("\nFOLDER/ FILE NAMES")
    print(dirCont)
    userI = input("\nWHAT'S ON YOUR MIND? ")
    
    if userI == "help":
      print('\nhelp - display help \nback - return to previous folder \n"filename" - open file \n"foldername" - open folder')
    elif userI == "back":
      if currDir != baseDir:
        currDir = negaDir(currDir)
      else:
        ON = False
    elif userI == "debug":
      print("baseDir: " + baseDir)
      print("prevDir: " + negaDir(currDir))
      print("currDir: " + currDir)
      print("dirCont: " + str(dirCont))
      print("userI: " + userI)
    elif userI in dirCont:
      if isTXT(userI):
        print("\n" + fileCont(currDir, userI))
      else:
        prevDir = currDir
        currDir = incrDir(currDir, userI)
    else:
      print("ERR")
