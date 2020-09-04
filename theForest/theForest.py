path1 = {"index":1, "new?":True, "text1":"you're on the end of a path, or maybe it's beggining. in the distance you can see small vortxes of leaves wander the forest before falling to the ground.", "text2":"you're at the begining of the path.", "options": ["move forward"], "move forward": ["changeIndex", 2]}

path2 = {"index":2, "new?":True, "text1":"sampletext", "text2":"sampletext", "options":["move forward", "move backward"], "move backward": ["changeIndex", 1], "move forward": ["changeIndex", 3]}

pathDir = [path1, path2]

def mainPath():
  LOST = True
  indexCurr = 1
  indexCont = "null"

  while LOST:
    for dic in pathDir:
      if dic["index"] == indexCurr:
        indexCont = dic
    if indexCont["new?"]:
      print(indexCont["text1"])
      indexCont["new?"] = False
    else:
      print(indexCont["text2"])
    
    for all in indexCont["options"]:
      print(all)
    option = input("\nwhat do you do? ")
    while option not in indexCont["options"]:
      option = input("what do you do? ")

    if indexCont[option][0] == "changeIndex":
      indexCurr = indexCont[option][1]

