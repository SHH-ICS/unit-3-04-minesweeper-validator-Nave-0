# Validate a minesweeper interior block
# block_data is a two dimensional array containing the data from a 3 x 3 grid of squares
# We are assuming that we are only checking interior blocks for now
# Return value should be a string that says either Valid or Invalid (with some hints as to why it's invlaid)

  # Check whether the centre block is a bomb, a number, or an invalid input
  # Skip bombs, send an error on invalid input, verify numbers
def validate( block_data ):
  return validation

grid = [
  [0,0,0],
  [1,3,0],
  [-1,1,0]
]

row = 0
col = 0 
bombs = 0

while row < 3:
    while col < 3: 
#        print("here")
        value = grid [row][col]
#        print(row)
#        print(col)
#        print(value)
        if value == -1:
            bombs = bombs + 1
            col = col + 1
#            print(col)
        else:
            col = col + 1
    row = row + 1
    col = 0    
#print(f"the number of bombs are {bombs}")

middle_value = grid [1][1]
#print(f"The middle value is {middle_value}")

if middle_value == bombs:
#    print(f"VALID")
    validation = "VALID"
else:
#    print(f"INVALID CHECK INTERROIR BLOCK")
    validation = "INVALID CHECK INTEROIR BLOCK"
print (validate(grid))
