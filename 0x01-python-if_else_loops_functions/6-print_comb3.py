#!/usr/bin/python3
for i in range(0, 10):
    j= 1 + i
    if i == 0:
        j = 0
    for j in range(j, 10):
        print("{:d}{:d}".format(i, j), end=", ")
print(89)        
