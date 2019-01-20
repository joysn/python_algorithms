# how to find the # at a particular position
# of a fibonacci series


pos = 6
num1 = 0
num2 = 1
op = []
op.append(num1)
op.append(num2)

for i in range(2,pos):
    op.append(op[i-1]+op[i-2])


print(op[-1])
print(op)


op1 = list()
op1.append(num1)
op1.append(num2)

for i in range(2,pos):
    op1.append(op[i-1]+op[i-2])
    op1.remove(op[i-2])


print(op1[-1])
print(op1)

# Output
# (base) D:\>python algo_python3.py
# 5
# [0, 1, 1, 2, 3, 5]
# 5
# [3, 5]
