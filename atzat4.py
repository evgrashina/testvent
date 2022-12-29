import random

gs = []
len_int = 0
n = []
for i in range(10):
    n.append(random.randint(-1000,1000))
for i in range(len(n)):
    if n[i] < 0 :
        len_int += 1
        gs.append(n[i])

with open('123.txt', 'w') as file:
    print(*gs, file = file)