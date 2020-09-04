from theForest import places

indexCurr = 0
indexCont = "null"

def indexNew(index):
  indexCurr = index

def mainPath():
  LOST = True

  while LOST:
    for dic in places.pathDir:
      if dic["index"] == indexCurr:
        indexCont = dic
    print(indexCont["text"])
    for all in indexCont["options"]:
      print(all)
    option = input("what do you do?")
    while option not in indexCont["options"]:
      option = input("what do you do?")
