# Find the maximum number formed from a given set of #s

import functools

arr = [3,56,78,34,90,9]

def my_compare(x,y):
    x1 = int(str(x) + str(y))
    y1 = int(str(y) + str(x))
    #print(x1)
    #print(y1)

    if x1 > y1:
        #print("returning {}".format(x))
        return x
    else:
        #print("returning {}".format(y))
        return y


#print(my_compare(7,91))

new = sorted(arr, key=functools.cmp_to_key(my_compare))
print(new)
op_str = ""
for e in new:
    op_str += str(e)

print(op_str)
print(op_str[::-1])


class my_int(int):

    def __lt__(self,other):
        _x = int(str(self)+str(other))
        _y = int(str(other)+str(self))
        if _x < _y:
            return self
        else:
            return other

    def __gt__(self, other):
        _x = int(str(self) + str(other))
        _y = int(str(other) + str(self))
        if _x >_y:
            return self
        else:
            return other


new_arr = []
for e in arr:
    new_arr.append(my_int(e))

print("".join(str(x) for x in sorted(new_arr)))

# Output
# [3, 56, 78, 34, 90, 9]
# 3567834909
# 9094387653
# 9903478563