# Create a Christmas tree out of the 0s and 1s in the "picture" list below:

picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]


# My Code

for rowindex, array in enumerate(picture):          # loop through each row
  array = picture[rowindex]                         # create a new list variable
  for index, value in enumerate(array):             # loop through each item in a row 
    if value == 0:                                  # if the value corresponding to that index is 0, change the value to a space
      array[index] = ' '
    else:
      array[index] = '*'                            # else, change the value to a star 
  print(''.join(array))                             # join the values, eliminating brackets and commas


#Andrei's Code:
# Note: better code because 
# 1) it does not create an additional variable 
# 2) it does not modify the original variable 

# for row in picture:
#   for pixel in row: 
#     if pixel == 1:
#       print('*', end='')  # need to eliminate Default new line '\n'
#     else:
#       print(' ', end='')  # need to eliminate Default new line '\n'
#   print('')               # need a new line
