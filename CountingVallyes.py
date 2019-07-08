def countingValleys(n, s):
    min = 2
    max = 1E7
    s = list(s) if type(s) == str else s
    valleys = 0
    isInValley = False;
 
    if (len(s) >= min and \
          len(s) <= max and \
          type(n) == int and \
          n >= min and \
          n <= max and \
          n == len(s)):
        ns = [1 if x == "U" else -1 for x in s]
        
        path = 0
        for i in range(0,len(ns)):
            path += ns[i]
            if path < 0 and isInValley == False:
               isInValley = True
            if path == 0 and isInValley == True:
                valleys += 1
                isInValley = False
            
               
    return(valleys)
    
countingValleys(8, "UDDDUDUU")
countingValleys(12, "DDUUDDUDUUUD")
countingValleys(1, "DU")
countingValleys(2, " DU")
countingValleys(3, "DDU")
countingValleys(100001, "DDU")
countingValleys(20, "DDUUDDUUDDUUDDUUDDUU")
countingValleys(10, "UUUUUDUUUU")