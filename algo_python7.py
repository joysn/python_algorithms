arr = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]


n = len(arr)
print(arr)
#print(n)

#print(int(n/2))
for j in range(int(n/2)+1):
    #print(j)
    first = j
    last = n - j
    for i in range(first,last-1):
        print(j,i,first,last-1,arr[j][i],arr[i][last-1],arr[last-1][last-1-i],arr[last-1-i][first])
        t = arr[j][i]
        arr[j][i] = arr[last-1-i][first]
        arr[last-1-i][first] = arr[last-1][last-1-i]
        arr[last-1][last-1-i] = arr[i][last-1]
        arr[i][last-1] = t

print(arr)