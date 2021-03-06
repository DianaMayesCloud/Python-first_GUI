picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

for rowindex, array in enumerate(picture):
  array = picture[rowindex]
  for index, value in enumerate(array):
    if value == 0:
      array[index] = ' '
    else:
      array[index] = '*'
  print(''.join(array))


#Andrei's Code:

# for row in picture:
#   for pixel in row: 
#     if pixel == 1:
#       print('*', end='')  # need to eliminate Default new line '\n'
#     else:
#       print(' ', end='')  # need to eliminate Default new line '\n'
#   print('')               # need a new line
