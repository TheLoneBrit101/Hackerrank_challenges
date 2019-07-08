def repeatedString(s, n):
    min = 1
    maxn = 1E13
    maxs = 100
    no_a = list(s)
    no_a = len(list(filter(lambda x: "a" in x, no_a)))
    
    if (type(s) == str and \
        len(s) >= min and \
        len(s) <= maxs and \
        type(n) == int and \
        n >= min and \
        n <= maxn):
        
        no_a = int(n/len(s)) * len([x for x in list(s) if x == "a"]) 
        no_a += len([x for x in list(s)[slice(0, n % len(s))] if x == "a"])
    return(no_a)

repeatedString("aba", 10)
repeatedString("a", 1000000000000)
repeatedString("a", 1)
repeatedString("bbb", 10)