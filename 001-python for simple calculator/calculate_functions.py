def add(*args):
    return sum(args)

def subtract(*args):
    if not args:
        raise ValueError("At least one argument is required")
    result = args[0]
    for num in args[1:]:
        result -= num
    return result

def multiply(*args):
    if not args:
        raise ValueError("At least one argument is required")
    result = 1
    for num in args:
        result *= num
    return result

def divide(*args):
    if not args:
        raise ValueError("At least on argument is required")
    result = args[0]
    for num in args[1:]:
        result /= num
    return result

def cmn(m,n):
    if m < n or n < 0:
        raise ValueError("Invalid input")
    fm = 1
    for num in range(1, m+1):
        fm *= num
    fn = 1
    for num in range(1, n+1):
        fn *= num
    fk = 1
    for num in range(1, m-n+1):
        fk *= num
    return fm // (fn *fk)

from functools import reduce
def gcd(*args):
    if len(args) < 2:
        raise ValueError("At least two arguments are required")
    def two_num_gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    return reduce(two_num_gcd, args)

from functools import reduce
def lcm(*args):
    if len(args) < 2:
        raise ValueError("At least two arguments are required")
    def two_num_lcm(a, b):
        return a * b // gcd(a, b)
    return reduce(two_num_lcm, args)