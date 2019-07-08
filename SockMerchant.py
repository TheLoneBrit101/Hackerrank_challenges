def find_pairs(ar,find,pairs):
    if len(ar) > 1:
        x = slice(1,len(ar))
        newArr = ar[x]
        try:
            if newArr.index(find) > -1:
                pairs += 1
                newArr = newArr[slice(0,newArr.index(find))] + \
                newArr[slice(newArr.index(find)+1,len(newArr))]
        except ValueError:
            try:
                return(find_pairs(newArr, newArr[0],pairs))
            except:
                pass
                
        
        try:
            return(find_pairs(newArr, newArr[0],pairs))
        except:
            pass
    return(pairs)
    
def sockMerchant(n, ar):
    min = 1;
    max = 100;
    ar = ar.split(' ') if type(ar) == str else ar;
 
    if (len(ar) >= min and \
          len(ar) <= max and \
          type(n) == int and \
          n >= min and \
          n <= max and \
          n == len(ar)):
               return(find_pairs(ar, ar[0], 0));
           
    return(0); 
     
            
n = 7
ar = ("1 2 1 2 1 3 2").split(' ')

sockMerchant(n, ar)

sockMerchant(9, "10 20 20 10 10 30 50 10 20")
sockMerchant(15, "6 5 2 3 5 2 2 1 1 5 1 3 3 3 5")
sockMerchant(1, "100")
sockMerchant(1, "101 100")
sockMerchant(0, "")
sockMerchant(101, "10000")