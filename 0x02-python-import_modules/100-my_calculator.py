#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    from calculator_1 import add, sub, mul, div
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = (sys.argv[1])
    b = (sys.argv[3])
    operator = sys.argv[2]
    if (operator == "+"):
        c = add(a, b)
    elif (operator == "-"):
        c = sub(a, b)
    elif (operator == "*"):
        c = mul(a, b)
    elif (operator == "/"):
        c = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{} {} {} = {}".format(a, operator, b, c))
