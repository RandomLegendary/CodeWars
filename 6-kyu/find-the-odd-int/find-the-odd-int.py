def find_it(seq):
    maxnum = max(seq)
    minnum = min(seq)
    
    if maxnum == minnum:
        return maxnum
    else:
        while maxnum != minnum - 1:
            counts = seq.count(maxnum)
            print(counts)
​
            if counts % 2 == 1:
                return maxnum
​
            maxnum -= 1
​
​