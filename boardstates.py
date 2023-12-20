print(ord("a"))
print(ord("b"))
print(ord("c")-ord("a"))

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
Board["White"]["Knight"]["Knigt1"] = ["b", "1"]
Board["White"]["Knight"]["Knigt2"] = ["g", "1"]

print(Board["White"]["Pawn"].values())

Board["White"]["Bishop"] = dict()
Board["White"]["Bishop"]["Bishopt1"] = ["c", "1"]
Board["White"]["Bishop"]["Bishopt2"] = ["f", "1"]

Board["White"]["Rook"] = dict()
Board["White"]["Rook"]["Rook1"] = ["a", "1"]
Board["White"]["Rook"]["Rook2"] = ["h", "1"]

Board["White"]["King"] = ["e", "1"]

Board["White"]["Queen"] = ["d", "1"]

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
Board["Black"]["Knight"]["Knigt1"] = ["b", "8"]
Board["Black"]["Knight"]["Knigt2"] = ["g", "8"]

Board["Black"]["Bishop"] = dict()
Board["Black"]["Bishop"]["Bishopt1"] = ["c", "8"]
Board["Black"]["Bishop"]["Bishopt2"] = ["f", "8"]

Board["Black"]["Rook"] = dict()
Board["Black"]["Rook"]["Rook1"] = ["a", "8"]
Board["Black"]["Rook"]["Rook2"] = ["h", "8"]

Board["Black"]["King"] = ["e", "8"]
Board["Black"]["Queen"] = ["d", "8"]

def makeMove(notation):
    #check if black or white are playing, make them play alternately
    if white == True:
        b = Board["White"]
        white = False
        mirror = 1
    else:
        b = Board["Black"]
        white = True
        mirror = -1
    if len(notation) == 2:
         for key in b["Pawn"].keys:
              #match the file
              if b["Pawn"][key][0] == notation[0]:
                   #see if the goal is within reach, if we use black we have to mirror the distance for black
                   if ((b["Pawn"][key][1] - notation[1]) * mirror) in [-1, -2]:
                        #see if there is any pawn in the way, mirror distance to blocking pawn for black
                        if [b["Pawn"][key][0], b["Pawn"][key][1]+mirror] not in b["Pawn"].values():
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
             for key in b["Kight"].keys():
                  if(((abs(ord(notation[1]) - ord(b["Knight"][key][0])) == 1) and (abs(notation[2] - b["Knight"][key][1]) == 2)) or ((abs(ord(notation[1]) - ord(b["Knight"][key][0])) == 2) and (abs(notation[2] - b["Knight"][key][1]) == 1))):
                    b["Knight"][key] = [notation[1], notation[2]]
        #check which Bishop is within reach, and move it            
        elif notation[0] == "B":
             if (abs((notation[1] + notation[2]) % 2) == 0 and mirror == 1) or (abs((notation[1] + notation[2]) % 2) == 1 and mirror == -1):
                  b["Bishop"]["Bishop1"] = [notation[1], notation[2]]
        elif notation[0] == "R":
            coordinates = []
            for pawn in Board["White"]["Pawn"].values():
                  coordinates.append(pawn)
            for pawn in Board["Black"]["Pawn"].values():
                  coordinates.append(pawn)
            for knight in Board["White"]["Knight"].values():
                  coordinates.append(knight)
            for knight in Board["Black"]["Knight"].values():
                  coordinates.append(knight)
            for rook in Board["White"]["Rook"].values():
                  coordinates.append(rook)
            for rook in Board["Black"]["Rook"].values():
                  coordinates.append(rook)
            for bishop in Board["White"]["Bishop"].values():
                  coordinates.append(bishop)
            for bishop in Board["Black"]["Bishop"].values():
                  coordinates.append(bishop)
            coordinates.append(Board["White"]["Queen"])
            coordinates.append(Board["Black"]["Queen"])
            coordinates.append(Board["White"]["King"])
            coordinates.append(Board["Black"]["King"])
            for r in b["Rook"]:
                 for coordinate in coordinates:
                      if (coordinate[0] == r[0] and coordinate[1] < max(r[1], notation[2]) and coordinate[1] > min(r[1], notation[2])) or (coordinate[1] == r[1] and ord(coordinate[0]) < max(ord(r[0]), ord(notation[1])) and ord(coordinate[0]) > min(ord(r[0]), ord(notation[1]))):
             
    elif len(notation) == 4:
        x
    elif len(notation) == 5:
        x
    elif len(notation) == 6:
        x
    else:
            print("error, notation invalid")