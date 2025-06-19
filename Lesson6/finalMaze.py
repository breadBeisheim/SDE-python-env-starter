import random

#Password code

name = input('What is your name? ')

#custom theme = space
print(f'Welcome to the INTERGALACTIC Escape Room, {name}!')

door = input('Please choose a door (1, 2, or 3): ')

correct_door = random.choice(['1', '2', '3'])

while door!= correct_door:
  door = input('Nope, try again! 1, 2, or 3 ')  

#intro to password puzzle + description message
print('You enter an empty dark room...')
print(' ')
print('There is something glowing in the corner') 

#space theme: asteroid, planet, star, moon, astronaut, sun
options = ['asteroid', 'planet', 'star', 'moon', 'astronaut', 'sun']

correct_password = random.choice(options)
 
for word in options:
  if word == correct_password:   
    print(word.capitalize())
  else:
    print(word)

print('In front of you, you see a computer terminal asking you for a password. ') #custom message

password_guess = input('Choose the password from the list. ') 
 
while password_guess != correct_password:
  print('Incorrect password. Try again. ')
  password_guess = input('Password: ').lower()

#custom space theme escape messages
print('The computer begins to glow. ')
print('The wall in front of you sinks into the ground, revealing a maze!')

#print('You have escaped! ')

#Escape room actual room- "e" = exit & "p" = player starting point
room = [
  'xxxxx',
  'x..ex',
  'x...x',
  'xp..x',
  'xxxxx',
]
#Function to calculate movement
def desiredMove(current_row, current_col, userChoice):
  new_row = current_row
  new_col = current_col          
  
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
  if room[new_row][new_col] == 'x': #Hit a wall!
    print(f'You can not move that way, there is a wall.')
    return current_row, current_col
  
  return [new_row, new_col]


playerRow = 3
playerCol = 1

#Telling players about walls - not yet working
def announce_walls(current_row, current_col):
  if room[current_row - 1][current_col] == 'x': #up
    print('There is a wall in the "Up" direction')

  if room[current_row + 1][current_col] == 'x': #down
    print('There is a wall in the "Down" direction')

  if room[current_row][current_col - 1] == 'x': #left
    print('There is a wall in the "Left" direction')

  if room[current_row][current_col - 1] == 'x': #right
    print('There is a wall in the "Left" direction')


#Test code for a verification system - found an easier way after reviewing class code.

#direction = input("What direction do you want to move?").lower() 
#row, col = desiredMove(playerRow, playerCol, direction)
#print(desiredMove(playerRow, playerCol, direction))

#desiredSpace = input("Do you want to move here?")

#if desiredSpace == 'yes':
  #playerRow, playerCol = desiredMove(playerRow, playerCol, direction)
 # print(playerRow, playerCol)
#else: 
  #direction = input("What direction do you want to move?").lower() 
 # row, col = desiredMove(playerRow, playerCol, direction)
#  print(desiredMove(playerRow, playerCol, direction))
# 
while room[playerRow][playerCol] != 'e':
  userChoice = input('What direction would you like to move? Your options are: up, down, left, right. ').lower()
  playerRow, playerCol = desiredMove(playerRow, playerCol, userChoice)
  print(f'You are now at row {playerRow}')
  print(f'You are now at column {playerCol}')


print('You escaped! ')

