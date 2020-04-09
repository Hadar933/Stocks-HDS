import random
zeros = 0
ones = 0
for i in range(100000):
    a = random.randint(0, 1)
    if a == 0:
        zeros+=1
    else:
        ones +=1

print('zeros=',zeros)
print('ones=',ones)
print('diff=',abs(zeros-ones))