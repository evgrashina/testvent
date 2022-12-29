import math
a1 = 5
b1 = 1
y1 = 5
o1 = 1
v1 = 7

a = y1
b = o1
x = a1

if a*x < b:
    y = math.exp(-2*x) + pow(a**4 + 4, (1/4))
else:
    y = math.sin(x) - b**2
print(y)