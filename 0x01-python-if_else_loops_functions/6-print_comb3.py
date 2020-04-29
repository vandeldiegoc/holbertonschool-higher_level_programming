#!/usr/bin/python3
for i in range(0, 9):
    j = 1+i
    for j in range(j, 10):
        if (i == 8 and j == 9):
            continue
        print("{:d}{:d}".format(i, j), end=", ")
print(89)
