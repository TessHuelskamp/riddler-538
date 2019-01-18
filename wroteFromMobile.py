
#mapped numbers by hand.
# assumedassumed 1 was read as 1 even though it sort of swaps locations
def rotate(num):
  if num in {0, 1, 2, 5, 8}: return num
  elif num == 6: return 9
  elif num == 9: return 6
  else: return None 

totalGood=0

for display in range(0, 99+1):
  one = display%10
  ten = display//10
 
  newOne = rotate(ten)
  newTen = rotate(one)
 
  if newTen ==None or newOne ==None:
    #print("good bc invalid char", display)
    totalGood+=1
    continue


  newdisplay = newTen*10 +newOne
 
 # there are some nice numbers here :)
  if newdisplay == display:
    totalGood+=1
    #print("valid rotate", display)
    continue

  #print("bad", display, newdisplay)
    
    
print(totalGood)
