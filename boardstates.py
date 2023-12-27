

test = dict()
test["category"] = dict()
test["category"]["a"] = ["1", "3"]
test["category"]["b"] = ["2", "4"]



Legend = dict()
Legend["N"] = "Knight"
Legend["Q"] = "Queen"
Legend["B"] = "Bishop"
Legend["R"] = "Rook"
Legend["K"] = "King"
Board = dict()

Board["White"] = dict()

Board["White"]["Pawn"] = dict()
Board["White"]["Pawn"]["Pawn1"] = ["a", "2"]
Board["White"]["Pawn"]["Pawn2"] = ["b", "2"]
Board["White"]["Pawn"]["Pawn3"] = ["c", "2"]
Board["White"]["Pawn"]["Pawn4"] = ["d", "2"]
Board["White"]["Pawn"]["Pawn5"] = ["e", "2"]
Board["White"]["Pawn"]["Pawn6"] = ["f", "2"]
Board["White"]["Pawn"]["Pawn7"] = ["g", "2"]
Board["White"]["Pawn"]["Pawn8"] = ["h", "2"]

Board["White"]["Knight"] = dict()
Board["White"]["Knight"]["Knight1"] = ["b", "1"]
Board["White"]["Knight"]["Knight2"] = ["g", "1"]


Board["White"]["Bishop"] = dict()
Board["White"]["Bishop"]["Bishop1"] = ["c", "1"]
Board["White"]["Bishop"]["Bishop2"] = ["f", "1"]

Board["White"]["Rook"] = dict()
Board["White"]["Rook"]["Rook1"] = ["a", "1"]
Board["White"]["Rook"]["Rook2"] = ["h", "1"]

Board["White"]["King"] = dict()
Board["White"]["King"]["King1"] = ["e", "1"]

Board["White"]["Queen"] = dict()
Board["White"]["Queen"]["Queen1"] = ["d", "1"]

Board["Black"] = dict()

Board["Black"]["Pawn"] = dict()
Board["Black"]["Pawn"]["Pawn1"] = ["a", "7"]
Board["Black"]["Pawn"]["Pawn2"] = ["b", "7"]
Board["Black"]["Pawn"]["Pawn3"] = ["c", "7"]
Board["Black"]["Pawn"]["Pawn4"] = ["d", "7"]
Board["Black"]["Pawn"]["Pawn5"] = ["e", "7"]
Board["Black"]["Pawn"]["Pawn6"] = ["f", "7"]
Board["Black"]["Pawn"]["Pawn7"] = ["g", "7"]
Board["Black"]["Pawn"]["Pawn8"] = ["h", "7"]

Board["Black"]["Knight"] = dict()
Board["Black"]["Knight"]["Knight1"] = ["b", "8"]
Board["Black"]["Knight"]["Knight2"] = ["g", "8"]

Board["Black"]["Bishop"] = dict()
Board["Black"]["Bishop"]["Bishop1"] = ["c", "8"]
Board["Black"]["Bishop"]["Bishop2"] = ["f", "8"]

Board["Black"]["Rook"] = dict()
Board["Black"]["Rook"]["Rook1"] = ["a", "8"]
Board["Black"]["Rook"]["Rook2"] = ["h", "8"]

Board["Black"]["King"] = dict()
Board["Black"]["King"]["King1"] = ["e", "8"]

Board["Black"]["Queen"] = dict()
Board["Black"]["Queen"]["Queen1"] = ["d", "8"]

"""print(Board.keys())
coordinates = []
for color in Board.keys():
      for figure in Board[color].keys():
            for piece in Board[color][figure].values():
                  coordinates.append(piece)
print(coordinates)
"""

white = True

def makeMove(notation):
      global Board
      global white
      coordinates = []
      for color in Board.keys():
            for figure in Board[color].keys():
                  for piece in Board[color][figure].values():
                        coordinates.append(piece)
    #check if black or white are playing, make them play alternately
      if white == True:
            b = Board["White"]
            white = False
            mirror = 1
      else:
            b = Board["Black"]
            white = True
            mirror = -1
      def findKnight(keyslist):
            for key in keyslist:
                  if(((abs(ord(notation[1]) - ord(b["Knight"][key][0])) == 1) and (abs(int(notation[2]) - int(b["Knight"][key][1])) == 2)) or ((abs(ord(notation[1]) - ord(b["Knight"][key][0])) == 2) and (abs(int(notation[2]) - int(b["Knight"][key][1])) == 1))):
                        b["Knight"][key] = [notation[-2], notation[-1]]
                        return
      def findBishop(keysList):
            for key in keysList:
                  if (abs(ord(notation[-2]) - ord(b["Bishop"][key][0])) == abs(int(notation[-1]) - int(b["Bishop"][key][1]))):
                        blocked = False
                        for coordinate in coordinates:
                              file = coordinate[0]
                              rank = coordinate[1]
                              if (ord(file) - ord(b["Bishop"][key][0])) in range(ord(notation[-2]) - ord(b["Bishop"][key][0])) and (int(rank) - int(b["Bishop"][key][1])) in range(int(notation[-1]) - int(b["Bishop"][key][1])) and abs(int(rank) - int(b["Bishop"][key][1])) == abs(int(notation[-1]) - int(b["Bishop"][key][1])):
                                    blocked = True
                        if blocked == False:
                              b["Bishop"][key] = [notation[-2], notation[-1]]
      def findRook(keysList):
            for key in keysList:
                  blocked = False
                  for coordinate in coordinates:
                        if (coordinate[0] == b["Rook"][key][0] and int(coordinate[1]) < max(int(b["Rook"][key][1]), int(notation[-1])) and int(coordinate[1]) > min(int(b["Rook"][key][1]), int(notation[-1]))) or (coordinate[1] == b["Rook"][key][1] and ord(coordinate[0]) < max(ord(b["Rook"][key][0]), ord(notation[-2])) and ord(coordinate[0]) > min(ord(b["Rook"][key][0]), ord(notation[-2]))):
                              blocked = True
                  if blocked == False:
                        b["Rook"][key] = [notation[-2], notation[-1]]


      if "x" in notation:
            #if that is the case, move the right figure to its goal field and remove the beaten figure from the board
            for color in Board.keys():
                  for figure in Board[color].keys():
                        for piece in Board[color][figure].keys():
                              if Board[color][figure][piece] == [notation[-2], notation[-1]]:
                                    Board[color][figure][piece] = ["0", "0"]
      if len(notation) == 2:
         for key in b["Pawn"].keys():
              #match the file
              if b["Pawn"][key][0] == notation[0]:
                   #see if the goal is within reach, if we use black we have to mirror the distance for black
                   if ((int(b["Pawn"][key][1]) - int(notation[1])) * mirror) in [-1, -2]:
                        #see if there is any pawn in the way, mirror distance to blocking pawn for black
                        if [b["Pawn"][key][0], str(int(b["Pawn"][key][1])+mirror)] not in coordinates:
                             #move pawn to respective field
                             b["Pawn"][key] = [notation[0], notation[1]]
      elif len(notation) == 3:
        #move the Queen
            if notation[0] == "Q":
                  b["Queen"] = [notation[1], notation[2]]
        #move the King
            elif notation[0] == "K":
                  b["King"] = [notation[1], notation[2]]
        #check which Knight is within reach, and move it
            elif notation[0] == "N":
                  findKnight(b["Knight"].keys())
             #check which bishop is within reach, and move it (the sum of one bishop's coordinates is always an even number, while the sum for the other one is uneven)     
            elif notation[0] == "B":
                  findBishop(b["Bishop"].keys())
            #check which rook is within reach, and move it (check if there are potentially other figures blocking the way)                  
            elif notation[0] == "R":
                  findRook(b["Rook"].keys())
            elif notation[0] == "0":
                  b["King"][0] = "g"
                  b["Rook2"][0] = "f"
      elif len(notation) == 4:
            #check if one figure beats another one
            if "x" in notation:
                  if notation[0].isupper():
                        #move the queen
                        if notation[0] == "Q":
                              b["Queen"] = [notation[2], notation[3]]
                        #move the King
                        elif notation[0] == "K":
                              b["King"] = [notation[2], notation[3]]
                        #check which Knight is within reach, and move it
                        elif notation[0] == "N":
                              findKnight(b["Knight"].keys())
                        #check which bishop is within reach, and move it (the sum of one bishop's coordinates is always an even number, while the sum for the other one is uneven)         
                        elif notation[0] == "B":
                              findBishop(b["Bishop"].keys())
                        #check which rook is within reach, and move it (check if there are potentially other figures blocking the way)               
                        elif notation[0] == "R":
                              findRook(b["Rook"].keys())
                  else:
                       for key in b["Pawn"].keys():
                            if b["Pawn"][key][0] == notation[0] and (int(b["Pawn"][key][1]) + mirror) == int(notation[-1]):
                                 b["Pawn"][key] = [notation[-2], notation[-1]]
            else:
                  #in this case, the figure moved is ambigious, and we have to use the additional information provided by the notation
                  #check which Knight is within reach, and move it
                  if notation[0] == "N":
                        keys = []
                        for key in b["Knight"].keys():
                              if notation[1] in b["Knight"][key]:
                                    keys.append(key)
                        print(keys)
                        findKnight(keys)    
                  #check which rook is within reach, and move it (check if there are potentially other figures blocking the way)
                  elif notation[0] == "B":
                        keys = []
                        for key in b["Bishop"].keys():
                              if notation[1] in b["Bishop"][key]:
                                    keys.append(key)                        
                        findBishop(keys)           
                  elif notation[0] == "R":
                        keys = []
                        for key in b["Rook"].keys():
                              if notation[1] in b["Rook"][key]:
                                    keys.append(key)                       
                        findRook(keys)
                 
      elif len(notation) == 5:
            #in this case, a figure beats another one and is ambigious
            if "x" in notation:
                  if notation[0] == "N":
                        keys = []
                        for key in b["Knight"].keys():
                              if notation[1] in b["Knight"][key]:
                                    keys.append(key)
                        findKnight(keys)    
                  #check which rook is within reach, and move it (check if there are potentially other figures blocking the way)
                  elif notation[0] == "B":
                        keys = []
                        for key in b["Bishop"].keys():
                              if notation[1] in b["Bishop"][key]:
                                    keys.append(key)                        
                        findBishop(keys)           
                  elif notation[0] == "R":
                        keys = []
                        for key in b["Rook"].keys():
                              if notation[1] in b["Rook"][key]:
                                    keys.append(key)                       
                        findRook(keys)
            #in this case, a figure is double-ambigious
            elif notation[0].isupper():
                  if notation[0] == "N":
                        for key in b["Knight"].keys():
                              if b["Knight"][key] == [notation[1], notation[2]]:
                                    b["Knight"][key] = [notation[-2], notation[-1]]
                  elif notation[0] == "B":
                        for key in b["Bishop"].keys():
                              if b["Bishop"][key] == [notation[1], notation[2]]:
                                    b["Bishop"][key] = [notation[-2], notation[-1]]                                              
                  #check which rook is within reach, and move it (check if there are potentially other figures blocking the way)            
                  elif notation[0] == "R":
                        for key in b["Rook"].keys():
                              if b["Rook"][key] == [notation[1], notation[2]]:
                                    b["Rook"][key] = [notation[-2], notation[-1]]
            elif notation[0] == "0":
                  b["King"][0] = "c"
                  b["Rook1"][0] = "d"                                     

      elif len(notation) == 6:
            if notation[0] == "N":
                  for key in b["Knight"].keys():
                        if b["Knight"][key] == [notation[1], notation[2]]:
                                    b["Knight"][key] = [notation[-2], notation[-1]]
            elif notation[0] == "B":
                  for key in b["Bishop"].keys():
                        if b["Bishop"][key] == [notation[1], notation[2]]:
                              b["Bishop"][key] = [notation[-2], notation[-1]]                                              
                  #check which rook is within reach, and move it (check if there are potentially other figures blocking the way)            
            elif notation[0] == "R":
                  for key in b["Rook"].keys():
                        if b["Rook"][key] == [notation[1], notation[2]]:
                              b["Rook"][key] = [notation[-2], notation[-1]]
      else:
            print("error, notation invalid")


makeMove("h4")
makeMove("e5")
makeMove("a4")
makeMove("b5")
makeMove("Rh3")
makeMove("a5")
makeMove("Raa3")
makeMove("c5")
makeMove("axb5")
makeMove("d5")
makeMove("Rxa5")
makeMove("Bb7")
print(Board.items())
