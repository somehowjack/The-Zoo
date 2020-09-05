def printFile(filename):
  file = open(filename, "r")
  print("\n" + file.read())
  file.close()

path1 = {"index":1, "new?":True, "text1":"\nyou wake up on the end of a path, or maybe it's beggining. in the distance you can see small vortxes of leaves wander the forest before falling to the ground. ahead of you the path continues.\n", "text2":"\nyou're at the begining of the path.\n", "options": ["follow the path"], "follow the path": ["changeIndex", 2]}

path2 = {"index":2, "new?":True, "text1":"\ncontinuing on the path you smell the air around you, it smells like ash but slowly your nose gets used to the smell. you stop in front of a sign with the words 'welcome to the forest' scawled onto it's face. on it is pinned a note.\n", "text2":"\nyou're at a sign that says 'welcome to the forest' with a note pinned to it.\n", "options":["keep moving forward", "go backward", "read note"], "go backward": ["changeIndex", 1], "keep moving forward": ["changeIndex", 3], "read note": ["printFile", "seen/trees/notes/path2.txt"]}

path3 = {"index":3, "new?":True, "text1":"\nthe path turns where a tree stands. the tree is prefectly dead. every leaf is gone and the branches don't look too sturdy. looking up you can see something at the top and a note carved into the lowest branch.\n", "text2":"\nsampletext\n", "options":["keep moving forward", "go backward", "read note", "climb tree"], "keep moving forward":["changeIndex", 8], "go backward":["changeIndex", 2], "read note":["printFile", "seen/trees/notes/path3.txt"], "climb tree":["newIndex", 4]}

tree1 = {"index":4, "new?":True, "text1":"\nsampletext\n", "text2":"\nsampletext\n", "options":[], "":[]}

path4 = {"index":8, "new?":True, "text1":"\nsampletext\n", "text2":"\nsampletext\n", "options":[], "":[]}

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
    
    print("OPTIONS:")
    for all in indexCont["options"]:
      print(all)
    option = input("\nwhat do you do? ")
    while option not in indexCont["options"]:
      option = input("what do you do? ")

    if indexCont[option][0] == "changeIndex":
      indexCurr = indexCont[option][1]

    if indexCont[option][0] == "printFile":
      printFile(indexCont[option][1])

