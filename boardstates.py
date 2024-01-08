import re
import numpy as np


#create an initial board state
board_original = dict()

board_original["White"] = dict()

board_original["White"]["Pawn"] = dict()
board_original["White"]["Pawn"]["Pawn1"] = ["a", "2"]
board_original["White"]["Pawn"]["Pawn2"] = ["b", "2"]
board_original["White"]["Pawn"]["Pawn3"] = ["c", "2"]
board_original["White"]["Pawn"]["Pawn4"] = ["d", "2"]
board_original["White"]["Pawn"]["Pawn5"] = ["e", "2"]
board_original["White"]["Pawn"]["Pawn6"] = ["f", "2"]
board_original["White"]["Pawn"]["Pawn7"] = ["g", "2"]
board_original["White"]["Pawn"]["Pawn8"] = ["h", "2"]

board_original["White"]["Knight"] = dict()
board_original["White"]["Knight"]["Knight1"] = ["b", "1"]
board_original["White"]["Knight"]["Knight2"] = ["g", "1"]


board_original["White"]["Bishop"] = dict()
board_original["White"]["Bishop"]["Bishop1"] = ["c", "1"]
board_original["White"]["Bishop"]["Bishop2"] = ["f", "1"]

board_original["White"]["Rook"] = dict()
board_original["White"]["Rook"]["Rook1"] = ["a", "1"]
board_original["White"]["Rook"]["Rook2"] = ["h", "1"]

board_original["White"]["King"] = dict()
board_original["White"]["King"]["King1"] = ["e", "1"]

board_original["White"]["Queen"] = dict()
board_original["White"]["Queen"]["Queen1"] = ["d", "1"]

board_original["Black"] = dict()

board_original["Black"]["Pawn"] = dict()
board_original["Black"]["Pawn"]["Pawn1"] = ["a", "7"]
board_original["Black"]["Pawn"]["Pawn2"] = ["b", "7"]
board_original["Black"]["Pawn"]["Pawn3"] = ["c", "7"]
board_original["Black"]["Pawn"]["Pawn4"] = ["d", "7"]
board_original["Black"]["Pawn"]["Pawn5"] = ["e", "7"]
board_original["Black"]["Pawn"]["Pawn6"] = ["f", "7"]
board_original["Black"]["Pawn"]["Pawn7"] = ["g", "7"]
board_original["Black"]["Pawn"]["Pawn8"] = ["h", "7"]

board_original["Black"]["Knight"] = dict()
board_original["Black"]["Knight"]["Knight1"] = ["b", "8"]
board_original["Black"]["Knight"]["Knight2"] = ["g", "8"]

board_original["Black"]["Bishop"] = dict()
board_original["Black"]["Bishop"]["Bishop1"] = ["c", "8"]
board_original["Black"]["Bishop"]["Bishop2"] = ["f", "8"]

board_original["Black"]["Rook"] = dict()
board_original["Black"]["Rook"]["Rook1"] = ["a", "8"]
board_original["Black"]["Rook"]["Rook2"] = ["h", "8"]

board_original["Black"]["King"] = dict()
board_original["Black"]["King"]["King1"] = ["e", "8"]

board_original["Black"]["Queen"] = dict()
board_original["Black"]["Queen"]["Queen1"] = ["d", "8"]

#set the state of the game to running
state = "Running"

#define the make_move function, which changes the board state according to a move notation 
def make_move(notation, current_board_original = board_original, white = True): 
      global state
      #create a legend for the different figure encodings
      legend = dict()
      legend["Q"] = "Queen"
      legend["N"] = "Knight"
      legend["B"] = "Bishop"
      legend["R"] = "Rook"
      #create a list with all currently occupied coordinates
      coordinates = []
      for color in current_board_original.keys():
            for figure in current_board_original[color].keys():
                  for piece in current_board_original[color][figure].values():
                        coordinates.append(piece)
      #check if black or white are playing, and assign the variable b(= all fgures of the current player) and bo(= all figures of the other player) accordingly
      if white == True:
            b = current_board_original["White"]
            bo = current_board_original["Black"]
            white = False
            mirror = 1
      else:
            b = current_board_original["Black"]
            bo = current_board_original["White"]
            white = True
            mirror = -1
      #define a function to find the figure that is supposed to be moved
      def findFigure(keysList, figure):
            #if the code gives as an N, we must find the correct knight
            if figure == "N":
                  for key in keysList:
                        #determine the right knight by checking its distance to the goal field
                        if(((abs(ord(notation[-2]) - ord(b["Knight"][key][0])) == 1) and (abs(int(notation[-1]) - int(b["Knight"][key][1])) == 2)) or ((abs(ord(notation[-2]) - ord(b["Knight"][key][0])) == 2) and (abs(int(notation[-1]) - int(b["Knight"][key][1])) == 1))):
                              b["Knight"][key] = [notation[-2], notation[-1]]
                              return current_board_original
            #find the correct bishop
            elif figure == "B":
                  for key in keysList:
                        #check if the goal field is on a diagonal to the respective bishop, and if nothing blocks his way
                        if (abs(ord(notation[-2]) - ord(b["Bishop"][key][0])) == abs(int(notation[-1]) - int(b["Bishop"][key][1]))):
                              blocked = False
                              for coordinate in coordinates:
                                    file = coordinate[0]
                                    rank = coordinate[1]
                                    if (ord(file) - ord(b["Bishop"][key][0])) in range(ord(notation[-2]) - ord(b["Bishop"][key][0])) and (int(rank) - int(b["Bishop"][key][1])) in range(int(notation[-1]) - int(b["Bishop"][key][1])) and abs(int(rank) - int(b["Bishop"][key][1])) == abs(int(notation[-1]) - int(b["Bishop"][key][1])):
                                          blocked = True
                              if blocked == False:
                                    b["Bishop"][key] = [notation[-2], notation[-1]]
                                    return current_board_original
            #find the correct rook
            elif figure == "R":
                  for key in keysList:
                        #check if the goal field is vertically or horizontally orthogonal to the rook, and whether something blocks the way
                        if notation[-2] in b["Rook"][key] or notation[-1] in b["Rook"][key]:
                              blocked = False
                              for coordinate in coordinates:
                                    if (coordinate[0] == b["Rook"][key][0] and int(coordinate[1]) < max(int(b["Rook"][key][1]), int(notation[-1])) and int(coordinate[1]) > min(int(b["Rook"][key][1]), int(notation[-1]))) or (coordinate[1] == b["Rook"][key][1] and ord(coordinate[0]) < max(ord(b["Rook"][key][0]), ord(notation[-2])) and ord(coordinate[0]) > min(ord(b["Rook"][key][0]), ord(notation[-2]))):
                                          blocked = True
                              if blocked == False:
                                    b["Rook"][key] = [notation[-2], notation[-1]]
                                    return current_board_original
            #find the correct queen
            elif figure == "Q":
                  for key in keysList:
                        #check the fields diagonal, as well as vertically and horizontally orthogonal to the queen, and check if something blocks the way
                        blocked = False
                        if (abs(ord(notation[-2]) - ord(b["Queen"][key][0])) == abs(int(notation[-1]) - int(b["Queen"][key][1]))):
                              for coordinate in coordinates:
                                    file = coordinate[0]
                                    rank = coordinate[1]
                                    if (ord(file) - ord(b["Queen"][key][0])) in range(ord(notation[-2]) - ord(b["Queen"][key][0])) and (int(rank) - int(b["Queen"][key][1])) in range(int(notation[-1]) - int(b["Queen"][key][1])) and abs(int(rank) - int(b["Queen"][key][1])) == abs(int(notation[-1]) - int(b["Queen"][key][1])):
                                          blocked = True
                                    if blocked == False:
                                          b["Queen"][key] = [notation[-2], notation[-1]]
                                          return current_board_original
                        for coordinate in coordinates:
                              if (coordinate[0] == b["Queen"][key][0] and int(coordinate[1]) < max(int(b["Queen"][key][1]), int(notation[-1])) and int(coordinate[1]) > min(int(b["Queen"][key][1]), int(notation[-1]))) or (coordinate[1] == b["Queen"][key][1] and ord(coordinate[0]) < max(ord(b["Queen"][key][0]), ord(notation[-2])) and ord(coordinate[0]) > min(ord(b["Queen"][key][0]), ord(notation[-2]))):
                                    blocked = True
                        if blocked == False:
                              b["Queen"][key] = [notation[-2], notation[-1]]
                              return current_board_original
      #remove any additonal signs at the end of the notation
      if notation[-1] in ["#", "+", "!", "?"]:
            notation = notation[:-1]
      #if we have a pawn promotion, we have to add the figure that the pawn promotes to, and to set it on the right field
      if "=" in notation:
            number = int(list(b[legend[notation[-1]]].keys())[-1][-1])+1
            b[legend[notation[-1]]][legend[notation[-1]]+str(number)] = [notation[-4], notation[-3]]
      #player lost the game
      if notation == "0-1":
            state = "Lost"
            return current_board_original
      #player won the game
      if notation == "1-0":
            state = "Win"
            return current_board_original
      #player has a draw
      if notation == "1/2-1/2":
            state = "Draw"
            return current_board_original
      #play the short rochade
      if notation == "O-O":
            b["King"]["King1"][0] = "g"
            b["Rook"]["Rook2"][0] = "f"
            print("rochade")
            return current_board_original
      #play the long rochade
      if notation == "O-O-O":
            b["King"]["King1"][0] = "c"
            b["Rook"]["Rook1"][0] = "d"
            return current_board_original
      #check if we are beating a figure in this turn
      if "x" in notation:
            beaten = False
            #if that is the case, move the right figure to its goal field and remove the beaten figure from the board_original
            for figure in bo.keys():
                  if beaten == True: break
                  for piece in bo[figure].keys():
                        #if we have a promotion, the coordinates of the beaten figure are at a different index in the notation
                        if "=" in notation:
                              if bo[figure][piece] == [notation[-4], notation[-3]]:
                                    bo[figure][piece] = ["0", "0"]
                                    beaten = True
                                    break      
                        if bo[figure][piece] == [notation[-2], notation[-1]]:
                              bo[figure][piece] = ["0", "0"]
                              beaten = True
                              break
            #if we have not beaten any figure yet, we probably have an en passé
            if beaten == False:
                  for figure in bo.keys():
                        if beaten == True: break
                        for piece in bo[figure].keys():
                              #check for an en passé
                              if bo[figure][piece] == [notation[-2], chr(int(notation[-1]) - mirror)]:
                                    bo[figure][piece] = ["0", "0"]
                                    beaten = True
                                    break
            #if still no figure could be beaten, we give out an error
            if beaten == False:
                  print("Error: No figure could be beaten.")
      #in this case, we simply have to move a pawn
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
                             return current_board_original
      if len(notation) == 3:
            #if we want to move the king, we can move him directly since there is only one per side
            if notation[0] == "K":
                  b["King"]["King1"] = [notation[1], notation[2]]
                  return current_board_original
            #otherwise, we have to use our findFigure function to find the respective figure we want to move
            else:
                  findFigure(b[legend[notation[0]]].keys(), notation[0])
                  return current_board_original
      if len(notation) == 4:
            #check if we have a pawn promotion
            if "=" in notation:
                  for key in b["Pawn"].keys():
                  #match the file
                        if b["Pawn"][key][0] == notation[0] and b["Pawn"][key][1] == str((int(notation[1]) - mirror)):
                              b["Pawn"][key] = ["0", "0"]
                              return current_board_original       
            if "x" in notation:
                  if notation[0].isupper():
                        #if we want to move the king, we can move him directly since there is only one per side
                        if notation[0] == "K":
                              b["King"]["King1"] = [notation[-2], notation[-1]]
                              return current_board_original
                        #otherwise, we have to use our findFigure function to find the respective figure we want to move
                        else:
                              findFigure(b[legend[notation[0]]].keys(), notation[0])
                              return current_board_original
                  #if we have to move a pawn that beats another figure, we need to consider that it beats figures diagonally
                  else:
                       for key in b["Pawn"].keys():
                            if b["Pawn"][key][0] == notation[0] and (int(b["Pawn"][key][1]) + mirror) == int(notation[-1]):
                                 b["Pawn"][key] = [notation[-2], notation[-1]]
                                 return current_board_original
            else:
                  #in this case, the figure moved is ambigious, and we have to use the additional information provided by the notation
                  #check which Knight is within reach, and move it
                  keys = []
                  for key in b[legend[notation[0]]].keys():
                        if notation[1] in b[legend[notation[0]]][key]:
                              keys.append(key)
                  findFigure(keys, notation[0])
                  return current_board_original
                 
      if len(notation) == 5:
            #in this case, a figure beats another one and is ambigious
            if "x" in notation:
                  keys = []
                  for key in b[legend[notation[0]]].keys():
                        if notation[1] in b[legend[notation[0]]][key]:
                              keys.append(key)
                  #after filtering for the figures that fulfill the specification noted in the notation, we use the findFigure function again
                  findFigure(keys, notation[0])
                  return current_board_original
      if len(notation) < 7:
            if "=" in notation:
                  #in this case, we have a pawn promotion
                  for key in b["Pawn"].keys():
                  #check which pawn would be in reach of the goal field and remove him from the board
                        if b["Pawn"][key][0] == notation[0] and b["Pawn"][key][1] == str((int(notation[3]) - mirror)):
                              b["Pawn"][key] == ["0", "0"]
                              return current_board_original 
            #in this case, a figure is double-ambigious
            for key in b[legend[notation[0]]].keys():
                  if b[legend[notation[0]]][key] == [notation[1], notation[2]]:
                        b[legend[notation[0]]][key] = [notation[-2], notation[-1]]
                        return current_board_original                                   
      #if we could not execute a move yet, an error seems to have occured
      print("error, notation invalid")
      return current_board_original

#function that takes a png file with a game notation and returns the resulting board states as one-hot encoded matrices
def get_data(path, white=True):
      #variable that indexes the matrix of figure-types
      m_counter = 0
      state_list = []
      #use the original boardstate before the first move
      global board_original
      with open(path, 'r') as pgn_file:
            tokens = []
            for line in pgn_file:
            #find the notation tokens for each line
                  line = line.strip()
                  tokens.append(re.findall(" [^ ]*", line))
      #for every move notation, perform the move using the make_move function, and append the resulting boardstate to state_list
      for token in tokens:
            for turn in token:
                  board_matrix = np.zeros((12,8,8))
                  print(turn[1:])
                  m_counter = 0
                  board_original = make_move(turn[1:], board_original, white)
                  for color in board_original.keys():
                        for figure in board_original[color].keys():
                              for piece in board_original[color][figure].values():
                                    if piece[0] != "0":
                                          board_matrix[m_counter][8 - int(piece[1])][ord(piece[0]) - 97] = 1
                              m_counter += 1
                  state_list.append(board_matrix)
                  white = (white == False)
      return(state_list)
      

#test
"""make_move("h4")
make_move("e5")
make_move("a4")
make_move("b5")
make_move("Rh3")
make_move("a5")
make_move("Raa3")
make_move("c5")
make_move("axb5")
make_move("d5")
make_move("Rxa5")
make_move("Bb7")
"""
#print(board_original.items())

get_data("/Users/franziska-marieplate/Documents/5. Semester/Python/Chess/pythonProject2023-24/chess_data/all_games/game_1.pgn")
#getData("/chess_data/all_games/game_1.pgn")
