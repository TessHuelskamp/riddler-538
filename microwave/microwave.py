# mapped numbers by hand.
# assumed 1 was read as 1 even though it sort of swaps locations
# None is an "invalid number" (e.g., 7->L)
def rotate(num):
  if num in {0, 1, 2, 5, 8}: return num
  elif num == 6: return 9
  elif num == 9: return 6
  else: return None

totalGood=0

for display in range(0, 99+1):
  # Grab digits
  one = display%10
  ten = display//10

  # Flip digits
  newOne = rotate(ten)
  newTen = rotate(one)

  # If a number is invalid, this is a good display.
  # The upside down digit is nonsense, so this is a clear display
  if newTen == None or newOne == None:
    totalGood+=1
    continue

  newdisplay = newTen*10 + newOne

  if newdisplay == display:
    totalGood+=1

print(totalGood)
