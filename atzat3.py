import random
import math

c = 0
d = 0
s = 0
b = 0
a = []
letters = 'qwertyuiopasdfghjklzxcvbnm'
for i in range(10):
    random_string = ''.join(random.choice(letters) for i in range(random.randint(1, 40)))
    a.append(random_string)
for i in range(S):
    for i in range(len(a)):
        if len(a[i]) > b:
            b = len(a[i])
            s = 1
        elif len (a[i]) == b:
            d = 1
if d == s:
    print(a[s])
else:
    print(a[s], a[d])