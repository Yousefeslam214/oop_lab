def calc(one, two, oper):
    if oper == '+':
        print(sum(one, two))
    else:
        print("invalid Operator")


def sum(x, y):
    return x + y

one = 3
two = 5
oper = '+'
calc(one, two, oper)
