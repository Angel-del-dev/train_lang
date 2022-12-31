from jinja2 import Undefined
import lib.built_in_fn.build_in_fn as b_fn
import lib.lexer as fC


def setAssignation(str, interpreted, fname):
    assignment, assigned = str.split('=')

    assignment, assigned = assignment.strip(), assigned.strip()

    assignment_change = False

    v_type = ''
    v_name = ''

    for ch in assignment:
        if assignment_change:
            v_name = v_name + ch
        else:
            if ch != ' ':
                v_type = v_type + ch
            else:
                assignment_change = True
    if '(' in assigned:
        assigned, interpreted = setFnCall(assigned, interpreted, fname)
    
    if v_type == 'string':
        assigned = assigned.replace("'", '').replace('"', '')
    if v_type == 'numeric':
        assigned = assigned
    if v_type == 'bool':
        assigned = assigned.replace('"', '').replace("'", '')
        if assigned == 'true':
            assigned = True
        elif assigned == 'false':
            assigned = False
        else:
            print('Boolean type not valid')
            assigned = Undefined
                
    var_dict = {
        'type' : v_type,
        'result' : assigned
    }
    interpreted['functions'][fname]['variables'][v_name] = var_dict
    return False, interpreted

def transform_num(str):
    try :
        return float(str)
    except:
        return False

def formatFromType(a, interpreted, fname):
    if len(a) == 0:
        return
    if (a[0] == "'" and a[len(a) - 1] == "'") or (a[0] == '"' and a[len(a) - 1] == '"'):
        return a.replace('"', '').replace("'", '')
    elif transform_num(a):
        return float(a)
    elif a is True or a is False:
        return a
    else:
        return interpreted['functions'][fname]['variables'][a]['result']

def setFnCall(str, interpreted, fname):
    result = False
    split = str.split('(')
    fn_name = split[0].replace(' ', '')
    fn_args = split[1].replace(')', '').split(',')
    format_args = []
    
    # Check if more than one param
    
    if(len(fn_args) > 0 and fn_args[0] != ''):
        for a in fn_args:
            a = a.strip()
            format_args.append(formatFromType(a, interpreted, fname))
    
    result = b_fn.checkIfBuildIn(fn_name, format_args)
    if result is False:
        result = fC.format_content_in_fn(interpreted['functions'][fn_name], fn_name)

        
    return result, interpreted