
def HasPair(arr,sum):

    comp = dict()

    for ele in arr:
        if int(ele) in comp.keys():
            return True
        comp[sum-ele] = ele

arr = [1,2,3,9]
arr2 = [1,2,4,4]

sum = 8

print(HasPair(arr,8))
print(HasPair(arr2,8))