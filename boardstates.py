import re
import numpy as np

print(ord("a"))
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

state = "Running"

white = True

def makeMove(notation, white=True):
      global Board
      global state
      legend = dict()
      legend["Q"] = "Queen"
      legend["N"] = "Knight"
      legend["B"] = "Bishop"
      legend["R"] = "Rook"
      coordinates = []
      for color in Board.keys():
            for figure in Board[color].keys():
                  for piece in Board[color][figure].values():
                        coordinates.append(piece)
    #check if black or white are playing, make them play alternately
      if white == True:
            b = Board["White"]
            bo = Board["Black"]
            white = False
            mirror = 1
      else:
            b = Board["Black"]
            bo = Board["White"]
            white = True
            mirror = -1
      def findFigure(keysList, figure):
            if figure == "N":
                  for key in keysList:
                        if(((abs(ord(notation[-2]) - ord(b["Knight"][key][0])) == 1) and (abs(int(notation[-1]) - int(b["Knight"][key][1])) == 2)) or ((abs(ord(notation[-2]) - ord(b["Knight"][key][0])) == 2) and (abs(int(notation[-1]) - int(b["Knight"][key][1])) == 1))):
                              b["Knight"][key] = [notation[-2], notation[-1]]
                              return
            elif figure == "B":
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
                                    return
            elif figure == "R":
                  for key in keysList:
                        if notation[-2] in b["Rook"][key] or notation[-1] in b["Rook"][key]:
                              blocked = False
                              for coordinate in coordinates:
                                    if (coordinate[0] == b["Rook"][key][0] and int(coordinate[1]) < max(int(b["Rook"][key][1]), int(notation[-1])) and int(coordinate[1]) > min(int(b["Rook"][key][1]), int(notation[-1]))) or (coordinate[1] == b["Rook"][key][1] and ord(coordinate[0]) < max(ord(b["Rook"][key][0]), ord(notation[-2])) and ord(coordinate[0]) > min(ord(b["Rook"][key][0]), ord(notation[-2]))):
                                          blocked = True
                              if blocked == False:
                                    b["Rook"][key] = [notation[-2], notation[-1]]
                                    return

            elif figure == "Q":
                  for key in keysList:
                        blocked = False
                        if (abs(ord(notation[-2]) - ord(b["Queen"][key][0])) == abs(int(notation[-1]) - int(b["Queen"][key][1]))):
                              for coordinate in coordinates:
                                    file = coordinate[0]
                                    rank = coordinate[1]
                                    if (ord(file) - ord(b["Queen"][key][0])) in range(ord(notation[-2]) - ord(b["Queen"][key][0])) and (int(rank) - int(b["Queen"][key][1])) in range(int(notation[-1]) - int(b["Queen"][key][1])) and abs(int(rank) - int(b["Queen"][key][1])) == abs(int(notation[-1]) - int(b["Queen"][key][1])):
                                          blocked = True
                                    if blocked == False:
                                          b["Queen"][key] = [notation[-2], notation[-1]]
                                          return
                        for coordinate in coordinates:
                              if (coordinate[0] == b["Queen"][key][0] and int(coordinate[1]) < max(int(b["Queen"][key][1]), int(notation[-1])) and int(coordinate[1]) > min(int(b["Queen"][key][1]), int(notation[-1]))) or (coordinate[1] == b["Queen"][key][1] and ord(coordinate[0]) < max(ord(b["Queen"][key][0]), ord(notation[-2])) and ord(coordinate[0]) > min(ord(b["Queen"][key][0]), ord(notation[-2]))):
                                    blocked = True
                        if blocked == False:
                              b["Queen"][key] = [notation[-2], notation[-1]]
                              return
      if notation[-1] in ["#", "+", "!", "?"]:
            notation = notation[:-1]
      if "=" in notation:
            number = int(list(b[legend[notation[-1]]].keys())[-1][-1])+1
            b[legend[notation[-1]]][legend[notation[-1]]+str(number)] = [notation[-4], notation[-3]]
      if notation == "0-1":
            state = "Lost"
            return
      if notation == "1-0":
            state = "Win"
            return
      if notation == "1/2-1/2":
            state = "Draw"
            return
      if notation == "O-O":
            b["King"]["King1"][0] = "g"
            b["Rook"]["Rook2"][0] = "f"
            print("rochade")
            return
      if notation == "O-O-O":
            b["King"]["King1"][0] = "c"
            b["Rook"]["Rook1"][0] = "d"
            return
      if "x" in notation:
            beaten = False
            #if that is the case, move the right figure to its goal field and remove the beaten figure from the board
            for figure in bo.keys():
                  if beaten == True: break
                  for piece in bo[figure].keys():
                        #if we have a promotion, the coordinates of the beaten figure are at a different location
                        if "=" in notation:
                              if bo[figure][piece] == [notation[-4], notation[-3]]:
                                    bo[figure][piece] = ["0", "0"]
                                    beaten = True
                                    break      
                        if bo[figure][piece] == [notation[-2], notation[-1]]:
                              bo[figure][piece] = ["0", "0"]
                              beaten = True
                              break
            if beaten == False:
                  for figure in bo.keys():
                        if beaten == True: break
                        for piece in bo[figure].keys():
                              #check for an en passé
                              if bo[figure][piece] == [notation[-2], chr(int(notation[-1]) - mirror)]:
                                    bo[figure][piece] = ["0", "0"]
                                    beaten = True
                                    break
            if beaten == False:
                  print("Error: No figure could be beaten.")

      if len(notation) == 2:
         for key in b["Pawn"].keys():
              #match the file
              if b["Pawn"][key][0] == notation[0]:
                   print("success1")
                   #see if the goal is within reach, if we use black we have to mirror the distance for black
                   if ((int(b["Pawn"][key][1]) - int(notation[1])) * mirror) in [-1, -2]:
                        print("success2")
                        #see if there is any pawn in the way, mirror distance to blocking pawn for black
                        if [b["Pawn"][key][0], str(int(b["Pawn"][key][1])+mirror)] not in coordinates:
                             print("success3")
                             #move pawn to respective field
                             b["Pawn"][key] = [notation[0], notation[1]]
                             return
      if len(notation) == 3:
            #if we want to move the king, we can move him directly since there is only one per side
            if notation[0] == "K":
                  b["King"]["King1"] = [notation[1], notation[2]]
                  return
            #otherwise, we have to use our findFigure function to find the respective figure we want to move
            else:
                  findFigure(b[legend[notation[0]]].keys(), notation[0])
                  return
      if len(notation) == 4:
            #check if we have a pawn promotion
            if "=" in notation:
                  for key in b["Pawn"].keys():
                  #match the file
                        if b["Pawn"][key][0] == notation[0] and b["Pawn"][key][1] == str((int(notation[1]) - mirror)):
                              b["Pawn"][key] == ["0", "0"]
                              return        
            if "x" in notation:
                  if notation[0].isupper():
                        #if we want to move the king, we can move him directly since there is only one per side
                        if notation[0] == "K":
                              b["King"]["King1"] = [notation[-2], notation[-1]]
                              return
                        #otherwise, we have to use our findFigure function to find the respective figure we want to move
                        else:
                              findFigure(b[legend[notation[0]]].keys(), notation[0])
                              return
                  #if we have to move a pawn that beats another figure, we need to consider that it beats figures diagonally
                  else:
                       for key in b["Pawn"].keys():
                            if b["Pawn"][key][0] == notation[0] and (int(b["Pawn"][key][1]) + mirror) == int(notation[-1]):
                                 b["Pawn"][key] = [notation[-2], notation[-1]]
                                 return
            else:
                  #in this case, the figure moved is ambigious, and we have to use the additional information provided by the notation
                  #check which Knight is within reach, and move it
                  keys = []
                  for key in b[legend[notation[0]]].keys():
                        if notation[1] in b[legend[notation[0]]][key]:
                              keys.append(key)
                  findFigure(keys, notation[0])
                  return 
                 
      if len(notation) == 5:
            #in this case, a figure beats another one and is ambigious
            if "x" in notation:
                  keys = []
                  for key in b[legend[notation[0]]].keys():
                        if notation[1] in b[legend[notation[0]]][key]:
                              keys.append(key)
                  findFigure(keys, notation[0])
                  return 
      if len(notation) < 7:
            if "=" in notation:
                  print("Success1")
                  for key in b["Pawn"].keys():
                  #match the file
                        print(b["Pawn"][key][0], notation[0], b["Pawn"][key][1], int(notation[3])-mirror)
                        if b["Pawn"][key][0] == notation[0] and b["Pawn"][key][1] == str((int(notation[3]) - mirror)):
                              b["Pawn"][key] == ["0", "0"]
                              print("Success!")
                              return 
            #in this case, a figure is double-ambigious
            for key in b[legend[notation[0]]].keys():
                  if b[legend[notation[0]]][key] == [notation[1], notation[2]]:
                        b[legend[notation[0]]][key] = [notation[-2], notation[-1]]
                        return                                   
      #if we could not execute a move yet, an error seems to have occured
      print("error, notation invalid")
      return

def getData(path, white=True):
      mCounter = 0
      stateList = []
      global Board
      if white == True:
            encoding = 1
      else:
            encoding = -1
      with open(path, 'r') as pgn_file:
            tokens = []
            for line in pgn_file:
            # Process each line here
                  line = line.strip()
                  tokens.append(re.findall(" [^ ]*", line))
      for token in tokens:
            for turn in token:
                  boardMatrix = np.zeros((12,8,8))
                  print(turn[1:])
                  mCounter = 0
                  makeMove(turn[1:], white)
                  for color in Board.keys():
                        for figure in Board[color].keys():
                              for piece in Board[color][figure].values():
                                    if piece[0] != "0":
                                          boardMatrix[mCounter][8 - int(piece[1])][ord(piece[0]) - 97] = 1 * encoding
                              mCounter += 1
                        encoding = encoding * -1
                  stateList.append(boardMatrix)
                  white = (white == False)
      return(stateList)
      

#test
"""makeMove("h4")
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
"""
#print(Board.items())

getData("/Users/franziska-marieplate/Documents/5. Semester/Python/Chess/pythonProject2023-24/chess_data/all_games/game_2.pgn")
