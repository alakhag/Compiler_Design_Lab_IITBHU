solution=[]
def valid_stmt(stmt):
    if stmt[0].lower() =='s':
        return True
    return False

def valid_expr(expr):
    if expr[0].lower() =='e':
        return True
    return False

def matched_struct(expr):
    if len(expr) == 1:
        return valid_stmt(expr[0])
    res = False
    if len(expr) > 5 and expr[0] == 'if' and valid_expr(expr[1]) and expr[2] == 'then':
        for i,s in enumerate(expr[3:]):
            if s=='else':
                res = res or (matched_struct(expr[3:i+3]) and matched_struct(expr[i+4:]))
            if res:
                break
    return res

def unmatched_struct(expr):
    res = False
    if len(expr) > 3 and expr[0] == 'if' and valid_expr(expr[1]) and expr[2] == 'then':
        res = struct(expr[3:])
        for i,s in enumerate(expr[3:]):
            if res:
                break
            if s=='else':
                res = res or matched_struct(expr[3:i+3]) and unmatched_struct(expr[i+4:])
    return res

def struct(expr):
    return matched_struct(expr) or unmatched_struct(expr)

def spliter(expr):
    return expr.split()

def Parser(expr):
    expr = spliter(expr)
    return struct(expr)

try:
    while True:
        print "-------------------------------------------"
        expr = raw_input('   Enter Expression : ')
        print "   Expression is    : ",Parser(expr)
        print ""  
except Exception as ex:
    print ex
