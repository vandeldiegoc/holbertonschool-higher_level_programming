import sys
print("{} arguments".format(len(sys.argv[1:])))
for i in range(len(sys.argv[1:])):
    print("{}: {}".format(i + 1, sys.argv[i+1]))
