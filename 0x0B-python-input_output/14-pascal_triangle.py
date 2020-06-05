#!/usr/bin/python3
''' module'''


def pascal_triangle(n):
    '''pascal triangle '''
    new = []
    for x in range(n):
        new.append([])
        for j in range(x + 1):
            if j == 0 or j == x:
                new[x].append(1)
            else:
                new[x].append(new[x - 1][j - 1] + new[x - 1][j])
    return new
