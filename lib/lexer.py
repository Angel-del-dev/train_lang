import lib.format_functions as l

interpreted = {
    "file_array" : '',
    "variables": {},
    "functions": {},
}

lib = {
    '=' : l.setAssignation,
    '(' : l.setFnCall
}

def splitInitialContent(c):
    return c.replace("\n", '').split("});")

def lexer(str, fname):
    global lib
    global interpreted
    for k in lib:
        if k in str:
            assigned, interpreted = lib[k](str, interpreted, fname)
            break

def func_lexer(str):
    fn_split = str.split(':=')
    assignment, assigned = fn_split
    
    fn_name = ''
    fn_type = ''
    assignment_change = False

    for ch in assignment:
        if(assignment_change):
            fn_type = fn_type + ch
        else:
            if(ch != ' '):
                fn_name = fn_name + ch
            else:
                assignment_change = True
    
    global interpreted
    interpreted['functions'][fn_name] = {
        "type" : fn_type.replace(" ", ''),
        "content" : assigned.replace('({', ''), # Find patch, parameters could be passed between ( and {
        "result": False,
        "variables" : {}
    }

def format_content_in_fn(fn_dict, fname):
    type = fn_dict['type']
    content = fn_dict['content']
    ending = fn_dict['result']
    if ending == True:
        # The function has been called at least once, so we don't need to format it again
        pass
    else:
        content_split = content.split(';')
        for s in content_split:
            if(s != ''):
                lexer(s, fname)

        del interpreted['functions'][fname]['variables']

def load(content):
    splitFn = splitInitialContent(content)
    
    global interpreted
    interpreted['file_array'] = splitFn

    for str in splitFn:
        if str != '':
            func_lexer(str)

    for k in interpreted['functions']:
        if interpreted['functions'][k]['type'] == 'main':
            format_content_in_fn(interpreted['functions'][k], k)