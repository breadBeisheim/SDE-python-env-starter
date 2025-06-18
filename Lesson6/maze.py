room = [
  'xxxxx',
  'x..ex',
  'x...x',
  'x...x',
  'xxxxx',
]

playerRow = 3
playerCol = 1


# Direction should be up, down, left or right (u, d, l, r).
def desiredMove(current_row, current_col, direction):
  new_row = current_row
  new_col = current_col          
  valid = False

  while valid != True:
    userChoice = input("move")

  if userChoice == 'up':
    new_row -= 1
  elif userChoice == 'down':
    new_row += 1
  elif userChoice == 'left':
    new_col -= 1
  elif userChoice == 'right':
    new_col += 1
  else:
    print("You did not choose a direction! [Up, Down, Left, Right]")

  return [new_row, new_col]



direction = input("What direction do you want to move?").lower() 
row, col = desiredMove(playerRow, playerCol, direction)
print(desiredMove(playerRow, playerCol, direction))



#desiredSpace = room[desiredRow][desiredCol]

#while desiredSpace == ".":
  

#realMove = input("Do you want to move here?")

#def mazeMove(realMove):
#  if realMove == "Yes":
#  playerRow, playerCol = desiredMove
