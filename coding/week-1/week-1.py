list = [1, 54, 71, 99, 25, 46]
n = 0
def findLargestNInList(l):
    for i in l:
        if (i > n):
            i = n
            return print(i)
    
findLargestNInList(list)