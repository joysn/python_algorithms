# Find the largest consecutive sequence in an array
# Here is the o/p is 1,2,3,4 i.e. length of 4


arr = [2,1,6,9,4,3]


my_dict = dict()
for ele in arr:
    my_dict[ele] = 1

#print(my_dict)

longest = 0
for key in my_dict.keys():
    #print('1) Key: {}'.format(key))
    if key-1 not in my_dict:
        #print('2) If for {}'.format(key))
        curr = key
        count = 1
        while curr+1 in my_dict.keys():
            #print('3) While for {} and element {} and count: {}'.format(key,curr+1,count))
            count += 1
            curr += 1

        if longest < count:
            longest = count

print(longest)

# Output
#(base) D:\>python algo_python2.py
#4

