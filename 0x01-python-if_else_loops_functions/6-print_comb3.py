#!/usr/bin/python3
for i in range(0, 9):
    j= 1 + i
    if i == 0:
        j = 0
    for j in range(j, 9):
        print("{:d}{:d}".format(i, j), end=", ")
print(89)
