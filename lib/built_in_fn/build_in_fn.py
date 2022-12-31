# import lib.utils as u
import lib.built_in_fn.math_built_in as m

def pl(arg):
    print(arg[0])
    return True

def concat_text(args):
    delimiter = args[0]

    del args[0]
    new_str = ''
    for i in range(0, len(args)):
        new_str += str(args[i])
        if i < len(args) - 1:
             new_str += delimiter
    return new_str

# Checker

callables = {
    # Utils
    'pl'    : pl,
    'concat'   : concat_text,
    # Arithmetic functions
    '+'     : m.math_add,
    '-'     : m.math_subt,
    '/'     : m.math_div,
    '*'     : m.math_mult,
    '^'     : m.math_pow,
    '2/'    : m.math_sqroot,
    '!'     : m.math_factorial
}

def checkIfBuildIn(function, args):
    global callables
    if function in callables:
        return callables[function](args)
    return False