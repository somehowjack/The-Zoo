path1 = {"index":1, "text":"you're in the same spot that you were in when you came here", "options": ["move forward"], "move forward": ["changeIndex", 2]}

path2 = {"index":2, "text":"sampletext", "options":["move forward", "move backward"], "move forward": [], "move backward": []}

pathDir = [path1, path2]

def mainPath():
  LOST = True
  indexCurr = 1
  indexCont = "null"

  while LOST:
    for dic in pathDir:
      if dic["index"] == indexCurr:
        indexCont = dic
    print(indexCont["text"])
    for all in indexCont["options"]:
      print(all)
    option = input("\nwhat do you do? ")
    while option not in indexCont["options"]:
      option = input("what do you do?")

    if indexCont[option][0] == "changeIndex":
      indexCurr = indexCont[option][1]

