# You are given an array of repeating #s. All #s repeat in an even
# way, except for one. Find the occurring #

arr = [1,4,6,4,1]

my_dict = dict()

for e in arr:
    if e in my_dict.keys():
        del my_dict[e]
    else:
        my_dict[e] = 1

print(list(my_dict.keys())[0])


#(base) D:\>python algo_python1.py
# 6
