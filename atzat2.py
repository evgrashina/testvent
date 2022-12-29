
import math
a1 = 5
b1 = 1
y1 = 5
o1 = 1
v1 = 7

result = {}
a = y1 + o1
a1 = 5
x = a
hx = 0.5
while a1 <= x <= a1 + 2:
    y = (x**2 + 1) * (x - a) * math.cos(x)**2
    x += hx
    result[x] = y
print(result)