from theForest import theForest

path1 = {"index":1, "text":"you're in the same spot that you were in when you came here", "options": ["move forward"], "move forward": theForest.indexNew(2)}

path2 = {"index":2, "text":"sampletext", "options":["move forward", "move backward"], "move forward": theForest.indexNew(3), "move backward": theForest.indexNew(1)}

pathDir = [path1, path2]