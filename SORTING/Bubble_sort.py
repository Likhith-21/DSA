def Bubble_sort(l):
    for i in range(len(l)):
        sorted = False
        for j in range(len(l)-i-1):
            if l[j]>l[j+1]:
                l[j] , l[j + 1] = l[j+1],l[j]
                sorted = True
        if not sorted:
            break
    return l
li = [7,4,6,5,8,9,2,1,3]
print(Bubble_sort(l))
