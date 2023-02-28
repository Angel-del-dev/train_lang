import lib.utils as u
import math

def math_add(args):
    if u.check_amount_params(args, 2, '+()') is False:
        return ''

    total = float(args[0]) + float(args[1])

    return total

def math_subt(args):
    if u.check_amount_params(args, 2, '-()') is False:
            return ''
    total = float(args[0]) - float(args[1])
    return total

def math_div(args):
    if u.check_amount_params(args, 2, '/()') is False:
            return ''
    total = float(args[0]) / float(args[1])
    return total

def math_mult(args):
    if u.check_amount_params(args, 2, '*()') is False:
            return ''
    total = float(args[0]) * float(args[1])
    return total

def math_pow(args):
    if u.check_amount_params(args, 2, '^()') is False:
            return ''
    total = float(args[0]) ** float(args[1])
    return total

def math_sqroot(args):
    if u.check_amount_params(args, 1, '2/()') is False:
            return ''
    total = math.sqrt(float(args[0]))
    return total

def math_factorial(args):
    if u.check_amount_params(args, 1, '!()') is False:
        return ''
    num = int(args[0])
    total = 1
    if num < 0:    
        print(" Factorial does not exist for negative numbers")
        return ''
    elif num == 0:    
        print("The factorial of 0 is 1")
        return ''
    else:    
        for i in range(1, num + 1):    
            total *= i    

    return total