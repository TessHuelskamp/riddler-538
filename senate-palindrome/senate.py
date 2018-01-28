# number of times the senate votes in palindromes

numSenators=100

def isPalindrome(x,y):
    both=str(x)+str(y)
    rBoth=both[::-1]

    return both == rBoth

print "aye nay absent"
for present in range (1,numSenators+1):
    for aye in range(present+1):
        nay=present-aye

        if isPalindrome(aye, nay): print  aye, nay, numSenators-aye-nay
